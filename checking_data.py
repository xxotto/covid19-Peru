'''
Author:         Otto F. Proaño
Created:        25/10/2021
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# https://pythonspeed.com/articles/pandas-load-less-data/

df = pd.read_csv('semanas_epi.csv')

print('Total de fallecidos: ' + str(sum(df['fallecidos'])))
print('Total de vacunados: ' + str(sum(df['vacunados'])))  

#%% Add percentajes
def percentage_of_column(df, new_col_name, your_col):
    df[new_col_name] = (df[your_col] / df[your_col].sum())*100

percentage_of_column(df, 'fallecidos_%', 'fallecidos')
percentage_of_column(df, 'vacunados_%', 'vacunados')

#%% Filter for 2021
df = df.loc[(df['epi_year'] == 2021)]  # Only 2021

#%% Graph of TOTAL DECEASED
y_pos = np.arange(len(df['epi_week']))

# Create bars
plt.bar(y_pos, df['fallecidos'], color='maroon', edgecolor='black')

# Create names on the x-axis
plt.xticks(y_pos, df['epi_week'])
plt.yticks(np.arange(0, 6000, 500))

# Labels
plt.title('FALLECIDOS por COVID-19 confirmados')
plt.xlabel('Semana epidemiógica')
plt.ylabel('Número de fallecidos')
plt.tick_params(axis='x', labelsize=6)

# 01/12/2020 en semana 49 empieza la segunda ola
plt.axvline(x=39, color='black', linestyle='dotted', linewidth=1.5)

plt.text(23, 5100, r'Primera ola', fontsize=11)
plt.text(43, 5100, r'Segunda ola', fontsize=11)

# Configure grid
plt.grid(True, axis = 'y', color = "grey", linewidth = "1", linestyle = "-")
plt.rcParams['axes.axisbelow'] = True

# Show graphic
plt.show()

#%% Graph of VACCINATED 
y_pos = np.arange(len(df['epi_week'].iloc[49:]))

plt.tick_params(axis='x', labelsize=9)
plt.tick_params(axis='y', labelsize=9)

# Create bars
plt.bar(y_pos, df['vacunados'].iloc[49:], color='blue', edgecolor='black')

# Create names on the x-axis
plt.xticks(y_pos, df['epi_week'].iloc[49:])
plt.yticks(np.arange(0, 2500000, 200000))

# Labels
plt.title('Vacunados contra COVID-19 confirmados')
plt.xlabel('Semana epidemiógica 2021')
plt.ylabel('Número de vacunados')

# Configure grid
plt.grid(True, axis = 'y', color = "grey", linewidth = "1", linestyle = "-")
plt.rcParams['axes.axisbelow'] = True

# Show graphic
plt.show()


#%% Graph of EPIWEEKS
df['epi_week'].iloc[44:]
x = np.arange(len(df['epi_week']))
width = 0.35  # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - width/2, df['vacunados_%'], 
                width, label='Vacunados',
                color = 'blue', edgecolor='black')
rects2 = ax.bar(x + width/2, df['fallecidos_%'], 
                width, label='Fallecidos', 
                color = 'red', edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('% por semana epidemiológica')
ax.set_xlabel('Semana epidemiológica')
ax.set_title('Porcentaje (%) de fallecidos y vacunados por semana epidemiológica')
ax.set_xticks(x)
ax.set_xticklabels(df['epi_week'])
ax.legend()
plt.tick_params(axis='x', labelsize=6)

# Configure grid
plt.grid(True, axis = 'y', color = "grey", linewidth = "1", linestyle = "-")
plt.rcParams['axes.axisbelow'] = True

# 01/12/2020 en semana 49 empieza la segunda ola
plt.axvline(x=39, color='black', linestyle='dotted', linewidth=1.5)

ax.text(25, 6.35, r'Primera ola', fontsize=12)
ax.text(45, 6.35, r'Segunda ola', fontsize=12)

# Uncomment to see titles in bars
'''
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)'''

fig.tight_layout()
plt.show()

#%%
df = pd.read_csv('TOTAL_fallecidosXciudades.csv')

y_pos = np.arange(len(df['DEPARTAMENTO']))

# Create bars
bh = plt.barh(y_pos, df['tasa_mortalidad'], 
              color='silver', edgecolor='black')

# Create names on the x-axis
plt.xticks(np.arange(0, 1, 0.05))
plt.yticks(y_pos, df['DEPARTAMENTO'], fontsize=9)

# Labels
plt.title('Fallecidos por COVID-19 por DEPARTAMENTOS del PERÚ', fontsize=12)
plt.xlabel('Tasa de mortalidad por 100 habitantes',  fontsize=10)
plt.tick_params(axis='x', labelsize=9)

# 01/12/2020 en semana 49 empieza la segunda ola
plt.axvline(x=0.6123714780640244, color='black', 
            linestyle='dashed', linewidth=1)

plt.text(0.62, 20, r'Tasa de mortalidad', fontsize=10)
plt.text(0.62, 19, r'general (0.61)', fontsize=10)

# Configure grid
plt.grid(True, axis = 'x', color = "grey", linewidth = "1", linestyle = "-")
plt.rcParams['axes.axisbelow'] = True

bh[25].set_color('r')

# Show graphic
plt.show()