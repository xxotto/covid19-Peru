import pandas as pd
import functions as fn

fal_url = 'RawData/fallecidos_covid.csv'

df_fal = fn.complete_largeCSV_file(fal_url, ';')

#%% Data info
df_fal.info()

#%% Checking missing values
missing_fal = fn.missing_values(df_fal)

#%% FECHA_CORTE
fal_cor = df_fal['FECHA_CORTE'].value_counts().sort_index()
print(fal_cor)
# Todos los valores son iguales, variale no necesaria

#%% FECHA_FALLECIMIENTO
date_a = pd.DataFrame({'date':[df_fal['FECHA_FALLECIMIENTO'].min()]})
date_a = pd.to_datetime(date_a['date'], format = '%Y%m%d').dt.date
print(f'Fecha inicial: {date_a[0]}')
del date_a
# Fecha del 1er fallecido 2020-03-03 

date_b = pd.DataFrame({'date':[df_fal['FECHA_FALLECIMIENTO'].max()]})
date_b = pd.to_datetime(date_b['date'], format = '%Y%m%d').dt.date
print(f'Fecha última: {date_b[0]}')
del date_b
# Fecha del último fallecido 2021-12-08

#%% EDAD_DECLARADA
fal_edad = df_fal['EDAD_DECLARADA'].value_counts().sort_index()

print('Edad: no_casos\n')
lst = []

for idx, edad in enumerate(fal_edad):
    index = fal_edad.index
    lst.append(f'{index[idx]}: {edad}')
    
chunks = [lst[x:x+30] for x in range(0, len(lst), 30)]
df = pd.DataFrame.from_records(chunks)
df = df.transpose()    
print(df)

del fal_edad, chunks, df, lst

#%% SEXO
fal_sexo = df_fal['SEXO'].value_counts().sort_index()

for idx, sex in enumerate(fal_sexo):
    index = fal_sexo.index
    print(f'{index[idx]}: {sex}')
# Hay puntos en lugar de vacíos

#%% CLASIFICACION_DEF
fal_cla = df_fal['CLASIFICACION_DEF'].value_counts().sort_index()

for idx, clase in enumerate(fal_cla):
    index = fal_cla.index
    print(f'{index[idx]}: {clase}')
# Se encuentran los 7 criterios de clasificación, corregir tíldes

#%% DEPARTAMENTO
fal_dep = df_fal['DEPARTAMENTO'].value_counts().sort_index()

for idx, dep in enumerate(fal_dep):
    index = fal_dep.index
    print(f'{index[idx]}: {dep}')
# Se encuentran los 7 criterios de clasificación, corregir tíldes

print(f'\nTotal fallecidos: {fal_dep.sum()}')

#%% DISTRITOS
fal_dis = df_fal['DISTRITO'].value_counts().sort_index()

print('Fallecidos por provincias: \n')
for idx, dis in enumerate(fal_dis):
    index = fal_dis.index
    print(f'{index[idx]}: {dis}')
print(f'\nTotal fallecidos: {fal_dis.sum()}')

del fal_dis
#%%






vac_url = 'RawData/TB_VACUNACION_COVID19.csv'


