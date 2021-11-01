'''
Author:         Otto F. Proaño
Created:        25/10/2021
'''

import pandas as pd
import numpy as np
import functions as fn


def just_cities(fal_url):
    """
    Función para filtrar a cada fallecido reportado en su año
    y semana epidemiológica en ciudad (Fallecidos = fal, Vacunados = vac)
    """                                 
    fal_col = ['FECHA_FALLECIMIENTO', 'DEPARTAMENTO']
    df_fal = fn.read_largeCSV_file(fal_url, ';', fal_col)
    fn.variable_fecha(df_fal, 'FECHA_FALLECIMIENTO')
    fn.date_to_epiweek(df_fal,'FECHA_FALLECIMIENTO')
    df_fal['fallecido'] = 1                                         
    df_fal['fallecido'].apply(np.int8) 
    df_fal.info()
    
    return df_fal



fal_url = 'C:/Users/otto0/Documents/DATA/COVID-19/fallecidos_covid.csv'
df = just_cities(fal_url)
del fal_url



epi_ciudades = pd.crosstab(index=[df['epi_year'],
                                 df['epi_week']],
                          columns=[df['fallecido'],
                                 df['DEPARTAMENTO']],
                          margins = True)



fal_ciudades = pd.crosstab(index = df['DEPARTAMENTO'],
                           columns = df['fallecido'])
fal_ciudades.columns = ['fallecidos']
fal_ciudades.loc['PERÚ',:] = fal_ciudades.sum(axis = 0)

# https://es.wikipedia.org/wiki/Anexo:Departamentos_del_Per%C3%BA_por_poblaci%C3%B3n
no_habitantes = [426806,
                 1180638,
                 430736,
                 1497438,
                 668213,
                 1453711,
                 1129854,
                 1357075,
                 365317,
                 760267,
                 975182,
                 1361467,
                 2016771,
                 1310785,
                 10628470,
                 1027559,
                 173811,
                 192740,
                 271904,
                 2047954,
                 1237997,
                 899648,
                 370974,
                 251521,
                 589110]

no_habitantes.append(sum(no_habitantes))
fal_ciudades['no_habitantes'] = no_habitantes
del no_habitantes

fal_ciudades['tasa_mortalidad'] = (fal_ciudades['fallecidos']/fal_ciudades['no_habitantes'])*100

epi_ciudades.to_csv('fallecidosXciudadesXsemanasEpi.csv')
fal_ciudades.to_csv('TOTAL_fallecidosXciudades.csv')
