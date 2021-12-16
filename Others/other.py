'''
Author:         Otto F. Proaño
Created:        15/09/2021
'''

import pandas as pd
import numpy as np
import functions as fn


def main():
    
    vac_col = ['fecha_vacunacion', 'id_vacuna', 'dosis', 'edad']
    fal_col = ['FECHA_FALLECIMIENTO', 'EDAD_DECLARADA', 'SEXO',
                    'DEPARTAMENTO', 'PROVINCIA', 'DISTRITO']
    
    df_vacunados = fn.read_largeCSV_file(vacunados_url, ',', vac_col)
    df_fallecido = fn.read_largeCSV_file(fallecido_url, ';', fal_col)
        
    # Codify our datasets
    vacunados = filtro_vacunados(df_vacunados)
    fallecido = filtro_fallecidos(df_fallecido)
    
    return df_vacunados, df_fallecido
'''
    df, df_head = concat_dataframes(vacunados, fallecido)
    del fallecido
    del vacunados
    df.to_csv('vacunados+fallecidos(21M).csv', index=False, header=True, 
              encoding='utf8')'''



def filtro_vacunados(df):
    
    fn.variable_fecha_ymd(df, 'fecha_vacunacion')
    fn.date_to_epiweek(df, 'fecha_vacunacion')      # Añadimos año y fecha epi
    fn.variable_edad(df, 'edad')                    # Categorizamos edad

    print(fn.missing_values(df))   # Imprimimos la cantidad de missing values 
    # df = df.dropna()             # Eliminar filas con missing values
    
    # Guardamos un nuevo csv con todas las variables codificadas
    '''df.to_csv("vacunados_covid_CODIFICADAS.csv", index=False, header=True,
    encoding='utf8')'''
    return df
    


def filtro_fallecidos(df):
    
    fn.variable_fecha(df, 'FECHA_FALLECIMIENTO')    # Formato fecha
    fn.variable_edad(df,'EDAD_DECLARADA')           # Categorizamos edad
    df = fn.variable_sexo(df)                       # CategorIzamos sexo
    fn.date_to_epiweek(df,'FECHA_FALLECIMIENTO')    # Añadimos año y fecha epi
    #df = fn.añadir_UBIGEO(df, url_ubigeo)          # Añadimos Lat y Lng
    
    print(fn.missing_values(df))   # Imprimimos la cantidad de missing values 
    df = df.dropna()             # Activar para eliminar filas con missing values
    
    # Guardamos un nuevo csv con todas las variables codificadas
    # df.to_csv("fallecidos_covid_CODIFICADAS.csv", index=False, header=True, encoding='utf8')
    
    return df



def concat_dataframes(vacunados, fallecido):
    
    # Leer los dataframes filtrados de fallecidos y vacunados para unirlos

    # Renombramos columnas
    vacunados.rename(columns={'fecha_vacunacion': 'fecha'}, inplace=True)
    fallecido.rename(columns={'FECHA_FALLECIMIENTO': 'fecha'}, inplace=True)

    fallecido.rename(columns={'EDAD_DECLARADA': 'edad'}, inplace=True)

    # Creamos una variable para diferenciar nuestros  datasets
    vacunados['vacunado'] = 1      # Asignamos un 1 si es un paciente vacunado
    fallecido['fallecido'] = 1     # Asignamos un 1 si es un paciente fallecido

    # Borramos variables que no se comparten
    del fallecido['SEXO']

    # Concatenamos en un solo df fallecidos y vacunados
    df = pd.concat([fallecido,vacunados])

    # Llenamos de 0 todos los valores vacíos en los identificadores de los dataset
    df['fallecido'] = df['fallecido'].fillna(value=0)
    df['vacunado'] = df['vacunado'].fillna(value=0)

    # Colocamos en orden las columnas
    df.insert(0, 'vacunado', df.pop('vacunado'))
    df.insert(1, 'fallecido', df.pop('fallecido'))
    df.insert(8, 'dosis', df.pop('dosis'))
    df.info()
    df['fecha'] = df['fecha'].dt.date

    df_head = df.head(1000)
    # df.to_csv('vacunados+fallecidos(21M).csv', index=False, header=True, encoding='utf8')
    
    return df, df_head


#%% CODE

# Dirección de csv o url de vacunados y fallecidos por covid19 en Perú
vacunados_url = 'C:/Users/otto0/Documents/DATA/COVID-19/TB_VACUNACION_COVID19.csv'
fallecido_url = 'C:/Users/otto0/Documents/DATA/COVID-19/fallecidos_covid.csv'
    
if __name__ == '__main__':
    vac,fal = just_dates(vacunados_url, fallecido_url)

del vacunados_url, fallecido_url


