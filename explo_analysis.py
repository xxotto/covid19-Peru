
import pandas as pd
import numpy as np
import functions as fn


vac_url = 'C:/Users/otto0/Documents/DATA/COVID-19/TB_VACUNACION_COVID19.csv'
fal_url = 'C:/Users/otto0/Documents/DATA/COVID-19/fallecidos_covid.csv'

vac = pd.read_csv(vac_url, nrows = 10000)
fal = pd.read_csv(fal_url, nrows = 10000, sep = ';')

del vac_url
del fal_url

a = fal['DEPARTAMENTO'].unique()
print(len(a))
