import pandas as pd
import numpy as np
# import time

from epiweeks import Week
from dask import dataframe as dd


# Funciones para transformar variables



def read_largeCSV_file(url, separator, cols):

    # Read large CSV files using dask
    #start = time.time()
    dask_df = dd.read_csv(url, sep = separator, 
                          dtype={'UBIGEO': 'object',
                                 'id_persona': 'float64',
                                 'FECHA_FALLECIMIENTO': 'int64',
                                 'DEPARTAMENTO': 'category',
                                 'dosis': 'int8'},
                          usecols = cols)
    pd_df = dask_df.compute()   # conver to df format
    #end = time.time()
    #print("Read csv with dask: ",(end-start),"sec")
    #pd_df.info(verbose=False, memory_usage="deep")
    
    return pd_df



def df_into_chunks(df):
    
    n = 500000  #size of chunks
    list_df = [df[i:i+n] for i in range(0,df.shape[0],n)]
    
    return list_df



def variable_fecha(df, date_name):
    
    # Función que cambia el formato de fechas de YYYYMMDD a yyyy/mm/dd
    df[date_name] = pd.to_datetime(df[date_name], 
                                   format = '%Y%m%d')
    


def variable_fecha_ymd(df, date_name):
    
    # Toma una fecha en dd/mm/yyyy y la transforma a yyyy-mm-dd
    df[date_name] = pd.to_datetime(df[date_name], 
                                   format = '%d/%m/%Y')
    
    
    
def variable_edad(df, name_age_variable):

    # Función que crea 2 variables categorizadas de la variable EDAD
    
    # Categorizamos la variable EDAD en 8 categorías de acuerdo a grupos etáreos
    c = name_age_variable
    conditions = [(df[c]< 18),
                  (df[c]>=18) & (df[c]<30),
                  (df[c]>=30) & (df[c]<40),
                  (df[c]>=40) & (df[c]<50),
                  (df[c]>=50) & (df[c]<60),
                  (df[c]>=60) & (df[c]<70),
                  (df[c]>=70) & (df[c]<80),
                  (df[c]>=80)]
    choices = [0,1,2,3,4,5,6,7]
    
    # La 1era en grupos etáreos (EDAD_CAT)
    df['edad_cat'] = np.select(conditions, choices, default=np.nan) 

    # y la 2nda en mayores de edad (EDAD_CAT_18)
    #df['edad_cat_18'] = np.where(df[name_age_variable]<18,0,1)
    
    
    
def variable_sexo(df):
        
    # Función para codificar la variable SEXO
    
    # Verificamos el % de 'MASCULINO' Y 'FEMENINO' para ver si no existe otro 
    # nombre como 'Indeterminado' que es común se coloque
    df.SEXO.value_counts() / len(df)
    # Creamos un diccionario para la variable SEXO
    df['SEXO'].replace({'INDETERMINADO':0,'INDETERMINAD':0, '.':0,
                        'MASCULINO':1,'FEMENINO':2}, inplace=True)
    # Eliminamos pacientes cuyo sexo se desconoce (no son más de un 0.00001%)
    # df = df.drop(df[df.SEXO == 0].index)
    
    return df   



def añadir_UBIGEO(df):
    
    # Función para añadir latitudes (LAT) y Longuitudes(LNG) según UBIGEO
    
    ''' Cambiamos los valores no validos de UBIGEO con 'nan' values
        Recordar que UBIGEO es un número o ID para identificar ciudades, 
        en este caso existen inconsistencias por eso se decide 
        eliminar filas si no tienen un ID'''
        
    df['UBIGEO'] = pd.to_numeric(df['UBIGEO'], errors='coerce')

    ''' Ahora agregamos las latitudes (LAT) y Longuitudes(LNG) de los ubigeos
        IMPORTANTE: en la página de datos abiertos el diccionario dice que 
        UBIGEO es el código de ubigeo_inei'''
    
    # Leemos el csv de UBIGEOS con sus códigos
    url_ubigeo = 'https://raw.githubusercontent.com/xxotto/covid19-Peru/main/Data/TB_UBIGEOS.csv' 
    cols = ['ubigeo_inei', 'departamento_inei', 'latitud', 'longitud']
    df_ubigeos = pd.read_csv(url_ubigeo, usecols=cols, encoding='utf8')

    # Renombramos nuestros ubigeos del df de fallecidos de UBIGEO a ubigeo_inei
    df.rename(columns = {'UBIGEO':'ubigeo_inei'}, inplace = True)

    # Mezclamos los df de acuerdo a su UBIGEO de izquierda a derecha df to df_ubigeos
    df = df.merge(df_ubigeos, on = 'ubigeo_inei', how = 'left')
    
    return df



def date_to_epiweek(df, date_name):
    '''
    Transformamos nuestra fecha dd/mm/yyyy objeto a formato fecha 
    por defeto en un Dtype datetime64[ns]
    Transformamos nuevamente dicha fecha a un Dtype objeto pero en un formato 
    de fecha adecuado para el paquete epiweeks

    Transformamos de formato fecha (yyyy-mm-dd) a objeto en formato 'Week'
    Usando .weektuple() se obtiene una tupla con su año y semana epidemiológica
    Es decir vamos de 07/05/2021 [date type] a una tupla (2021,18) [tuple type]
    
    Separamos la tupla en 2 variables, una con el año y otra con la semana epi
    Y guardamos en un nuevo csv
    '''
    df[['epi_year','epi_week']] = df[date_name].apply(lambda date_name : Week.fromdate(date_name).weektuple()).tolist()

    df['epi_year'] = df['epi_year'].apply(np.int16)
    df['epi_week'] = df['epi_week'].apply(np.int8)
    
    del df[date_name]

    
    
def missing_values(df):
    
    # Función que devuelve un df con los % de datos faltantes
    percent_missing = df.isnull().sum() * 100 / len(df)
    missing_value_df = pd.DataFrame({'percent_missing': percent_missing}).reset_index()

    return missing_value_df
