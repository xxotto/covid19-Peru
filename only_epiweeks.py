'''
Author:         Otto F. Proaño
Created:        25/10/2021
'''

import pandas as pd
import numpy as np

import functions as fn



def just_dates(vac_url, fal_url):
    """
    Función para filtrar a cada vacunado y fallecido reportado en su año
    y semana epidemiológica (Fallecidos = fal, Vacunados = vac)
    """
    vac_col = ['fecha_vacunacion']                                  # Seleccionar solamente la columna de fechas
    fal_col = ['FECHA_FALLECIMIENTO']

    df_vac = fn.read_largeCSV_file(vac_url, ',', vac_col)           # Leemos los datasets
    df_fal = fn.read_largeCSV_file(fal_url, ';', fal_col)

    fn.variable_fecha_ymd(df_vac, 'fecha_vacunacion')               # Transformamos a formato fecha (datetime64[ns])
    fn.variable_fecha(df_fal, 'FECHA_FALLECIMIENTO')
        
    fn.date_to_epiweek(df_fal,'FECHA_FALLECIMIENTO')                # Obtenemos semana epidemiológica de fallecidos

    lst_vac = fn.df_into_chunks(df_vac)                             # Dividimos en chunks de 500 000 de filas

    for chunk in lst_vac:                                           # Obtenemos semana epidemiológica de vacunados para cada chunk
        chunk = fn.date_to_epiweek(chunk, 'fecha_vacunacion')
    
    df_fal['fallecido'] = 1                                         # Creamos columnas de 1 para contabilizar cada caso
    df_fal['fallecido'].apply(np.int8) 
    df_fal.info()

    for chunk in lst_vac:                                        
        chunk['vacunado'] = 1
        chunk['vacunado'].apply(np.int8)
        del chunk
    
    return lst_vac, df_fal
    


def epiweeks(df_fal):
    """
    Devuelve un dataframe con el total de fallecidos por semana y año 
    epidemiológico
    """
    epi_fal = pd.crosstab(index=[df_fal['epi_year'],
                                 df_fal['epi_week']],
                          columns=df_fal['fallecido'])
    # epi_fal.reset_index(inplace=True)
    epi_fal.columns = ['fallecidos']    
    
    return epi_fal
    
  
    
def epiweeks_chunks(dfs_vac):
    """
    Devuelve un dataframe con el total de vacunados por semana y año 
    epidemiológico (recibe una lista de dataframes o chunks)
    """
    var_holder = {}                                                 # Diccionario para guardar nombres
    lst_epi_vac = []                                                # Lista de dfs para cada sumatoria de chunks

    for i, chunk in enumerate(dfs_vac):
        var_holder['epi_vac_' + str(i)]= pd.crosstab(index=[chunk['epi_year'],
                                                            chunk['epi_week']],
                                                     columns=chunk['vacunado'])
        lst_epi_vac.append(var_holder['epi_vac_' + str(i)])
    
    merged_epivac = pd.concat(lst_epi_vac, axis=1)                  # Unimos todos los dfs sumados en uno solo

    epi_vac = pd.DataFrame(merged_epivac.sum(numeric_only=True, axis=1))
    epi_vac.columns = ['vacunados']
    
    return epi_vac
  
    
  
def merged_epiweeks(epi_vac, epi_fal):
    """
    Junta 2 dataframes del total de vacunados y fallecidos por semana
    epidemiológica
    """
    merged_epiweeks = pd.concat([epi_fal, epi_vac], axis=1)         # Concatenamos ambos dataframes (hay Nan values)
    merged_epiweeks = merged_epiweeks.fillna(value = 0)
    merged_epiweeks = merged_epiweeks.astype('Int64')               # Porque hay Nan values se cambia a float64 automáticamente
    
    return merged_epiweeks
    
   

# =============================================================================
# MAIN CODE  
# =============================================================================
vac_url = 'C:/Users/otto0/Documents/DATA/COVID-19/TB_VACUNACION_COVID19.csv'
fal_url = 'C:/Users/otto0/Documents/DATA/COVID-19/fallecidos_covid.csv'

if __name__ == '__main__':
    dfs_vac,df_fal = just_dates(vac_url, fal_url)
    
    epi_fal = epiweeks(df_fal)
    epi_vac = epiweeks_chunks(dfs_vac)
  
    epiweeks = merged_epiweeks(epi_vac, epi_fal)
    
del vac_url, fal_url

epiweeks.to_csv('epi_weeks.csv')
