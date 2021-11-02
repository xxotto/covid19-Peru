"""
Author:         Otto F. Proaño
Created:        25/10/2021
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# https://pythonspeed.com/articles/pandas-load-less-data/

df = pd.read_csv("Data/epi_weeks.csv")

print("Total deceased: " + str(sum(df["deceased"])))
print("Total vaccinated: " + str(sum(df["vaccinated"])))


# Add a new col of percentages of each row from the any variable
def colPercent(dataset, new_name, col_name):
    dataset[new_name] = (dataset[col_name] / dataset[col_name].sum()) * 100


colPercent(df, "deceased_%", "deceased")
colPercent(df, "vaccinated_%", "vaccinated")


# Barplot of TOTAL DECEASED
def plot_deceased():
    fig = plt.figure()
    y_position = np.arange(len(df["epi_week"]))  # y labels
    plt.bar(y_position, df["deceased"], color="gray", edgecolor="black")  # Create bars
    plt.xticks(y_position, df["epi_week"])  # Create names on the x-axis
    plt.yticks(np.arange(0, 6000, 500))  # y range
    plt.title("Deaths confirmed by COVID-19")  # Labels
    plt.xlabel("Epidemiological week")
    plt.ylabel("Number of deceased")
    plt.tick_params(axis="x", labelsize=6)
    plt.axvline(x=39, color="brown", linestyle="dotted", linewidth=1.5)  # In week 49 start the new wave (01/12/2020)
    plt.text(23, 5100, r"First wave", fontsize=11)
    plt.text(43, 5100, r"Second wave", fontsize=11)
    plt.grid(True, axis="y", color="grey", linewidth="1", linestyle="-")  # Configure grid
    plt.rcParams["axes.axisbelow"] = True
    return fig


# Barplot of TOTAL VACCINATED
def plot_vaccinated():
    fig = plt.figure()
    y_position = np.arange(len(df["epi_week"].iloc[49:]))
    plt.tick_params(axis="x", labelsize=9)
    plt.tick_params(axis="y", labelsize=9)
    plt.bar(y_position, df["vaccinated"].iloc[49:], color="blue", edgecolor="black")  # Create bars
    plt.xticks(y_position, df["epi_week"].iloc[49:])  # Create names on the x-axis
    plt.yticks(np.arange(0, 2500000, 200000))
    plt.title("vaccinated contra COVID-19 confirmados")  # Labels
    plt.xlabel("Semana epidemiógica 2021")
    plt.ylabel("Número de vaccinated")
    plt.grid(True, axis="y", color="grey", linewidth="1", linestyle="-")  # Configure grid
    plt.rcParams["axes.axisbelow"] = True

    return fig


def plot_epiweek(dataset):
    fig = plt.figure()
    dataset = df["epi_week"].iloc[44:]
    x = np.arange(len(df["epi_week"]))
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()

    ax.bar(x - width / 2, df["vaccinated_%"],
           width, label="vaccinated",
           color="blue", edgecolor="black")
    ax.bar(x + width / 2, df["deceased_%"],
           width, label="deceased",
           color="red", edgecolor="black")

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("% por semana epidemiológica")
    ax.set_xlabel("Semana epidemiológica")
    ax.set_title("Porcentaje (%) de deceased y vaccinated por semana epidemiológica")
    ax.set_xticks(x)
    ax.set_xticklabels(df["epi_week"])
    ax.legend()
    plt.tick_params(axis="x", labelsize=6)

    # Configure grid
    plt.grid(True, axis="y", color="grey", linewidth="1", linestyle="-")
    plt.rcParams["axes.axisbelow"] = True

    # 01/12/2020 en semana 49 empieza la segunda ola
    plt.axvline(x=39, color="black", linestyle="dotted", linewidth=1.5)

    ax.text(25, 6.35, r"Primera ola", fontsize=12)
    ax.text(45, 6.35, r"Segunda ola", fontsize=12)

    fig.tight_layout()

    return fig


f1 = plot_vaccinated()
f2 = plot_deceased()
f3 = plot_epiweek(df)

plt.show()
# %%
df = pd.read_csv("Data/TOTAL_deceasedXciudades.csv")

y_pos = np.arange(len(df["DEPARTAMENTO"]))

# Create bars
bh = plt.barh(y_pos, df["tasa_mortalidad"],
              color="silver", edgecolor="black")

# Create names on the x-axis
plt.xticks(np.arange(0, 1, 0.05))
plt.yticks(y_pos, df["DEPARTAMENTO"], fontsize=9)

# Labels
plt.title("deceased por COVID-19 por DEPARTAMENTOS del PERÚ", fontsize=12)
plt.xlabel("Tasa de mortalidad por 100 habitantes", fontsize=10)
plt.tick_params(axis="x", labelsize=9)

# 01/12/2020 en semana 49 empieza la segunda ola
plt.axvline(x=0.6123714780640244, color="black",
            linestyle="dashed", linewidth=1)

plt.text(0.62, 20, r"Tasa de mortalidad", fontsize=10)
plt.text(0.62, 19, r"general (0.61)", fontsize=10)

# Configure grid
plt.grid(True, axis="x", color="grey", linewidth="1", linestyle="-")
plt.rcParams["axes.axisbelow"] = True

bh[25].set_color("r")

# Show graphic
plt.show()
