import pandas as pd
import numpy as np
import time

from epiweeks import Week
from dask import dataframe as dd


#######################################################
# Funciones para transformar variables
#######################################################



def complete_largeCSV_file(url, separator):
    # Read a complete large CSV files using dask
    
    start = time.time()
    dask_df = dd.read_csv(url, sep = separator, 
                          dtype={'FECHA_CORTE' : 'category',
                                 'FECHA_FALLECIMIENTO' : 'category',
                                 'EDAD_DECLARADA' : 'int64',
                                 'SEXO' : 'category',
                                 'CLASIFICACION_DEF' : 'category',
                                 'DEPARTAMENTO' : 'category',
                                 'PROVINCIA' : 'category',
                                 'DISTRITO' : 'category',
                                 'UBIGEO': 'category',
                                 'id_persona': 'float64',
                                 'id_vacunados_covid19': 'float64',
                                 'fecha_vacunacion' : 'category',
                                 'id_eess' : 'category',
                                 'id_centro_vacunacion' : 'category',
                                 'id_vacuna' : 'category',
                                 'id_grupo_riesgo' : 'category',
                                 'dosis': 'int8',
                                 'edad' : 'in64'})
    pd_df = dask_df.compute()   # conver to df format
    end = time.time()
    print("Read csv with dask: ",(end-start),"sec")
    pd_df.info(verbose=False, memory_usage="deep")
    
    return pd_df



def read_largeCSV_file(url, separator, cols):
    # Read large CSV files using dask
    
    dask_df = dd.read_csv(url, sep = separator, 
                          dtype={'FECHA_CORTE' : 'category',
                                 'FECHA_FALLECIMIENTO' : 'int64',
                                 'EDAD_DECLARADA' : 'int64',
                                 'SEXO' : 'category',
                                 'CLASIFICACION_DEF' : 'category',
                                 'DEPARTAMENTO' : 'category',
                                 'PROVINCIA' : 'category',
                                 'DISTRITO' : 'category',
                                 'UBIGEO': 'category',
                                 'id_persona': 'float64',
                                 'id_vacunados_covid19': 'float64',
                                 'fecha_vacunacion' : 'int64',
                                 'id_eess' : 'category',
                                 'id_centro_vacunacion' : 'category',
                                 'id_vacuna' : 'category',
                                 'id_grupo_riesgo' : 'category',
                                 'dosis': 'category',
                                 'edad' : 'int64'},
                          usecols = cols)
    pd_df = dask_df.compute()   # conver to df format
    
    return pd_df



def df_into_chunks(df):
    # Separar df en una lista de dfs de tamaño n
    
    n = 500000  #size of chunks
    list_df = [df[i:i+n] for i in range(0,df.shape[0],n)]
    
    return list_df



def variable_fecha(df, date_name):
    # Función que cambia el formato de fechas de YYYYMMDD a yyyy/mm/dd
    
    df[date_name] = pd.to_datetime(df[date_name], format = '%Y%m%d')
    

 
def variable_fecha_ymd(df, date_name):
    # Toma una fecha de dd/mm/yyyy y la transforma a yyyy-mm-dd
    
    df.loc[:,date_name] = pd.to_datetime(df.loc[:,date_name], format = '%d/%m/%Y')

    

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




def date_to_epiweek(df, date_name):
    '''Recibe un dataframe y el nombre (en str) de la columna fecha, a convertir 
    en semana epidemiológica'''
    
    df[['year','epi_week']] = df[date_name].apply(lambda date_name : Week.fromdate(date_name).weektuple()).tolist()

    
    
def missing_values(df):
    # Función que devuelve un df con los % de datos faltantes
    
    percent_missing = df.isnull().sum() * 100 / len(df)
    missing_value_df = pd.DataFrame({'percent_missing': percent_missing}).reset_index()

    return missing_value_df