# COVID-19 en Perú
El objetivo del repositorio es integrar información, generar tablas resumen y visualizar datos referentes a COVID-19 de todo el Perú. Así facilitar el uso de los mismos para reportes y boletines de salud, investigaciones epidemiológicas, y apoyar en el proceso de toma de desiciones por parte de instituciones gubernamentales encargadas del área de salud.

***IMPORTANTE:** Repositorio aún en desarrollo. Datos actualizados cada fin de semana.

## Tabla de Contenidos

  - [1. Data Products (Data)](#1-data-products-data)
  - [2. Fuentes de datos (RawData)](#2-fuentes-de-datos-rawdata)
  - [3. ¿Cómo funciona?](#3-cómo-funciona)
  - [4. Fuentes de información](#4-fuentes-de-información)
  - [5. Contacto](#5-contacto)
  - [6. Agradecimientos](#6-agradecimientos)


## 1. Data Products ([Data](https://github.com/xxotto/covid19-peru/tree/main/Data))
Data products, datos finales o tablas resumen obtenidos se encuentran en el directorio Data. Todos los archivos se encuentran en formato de valores separados por comas (CSV).
   
   - [Data Product 1](Data/DP1_covid19-peru_x_semanaEpi.csv): Dataset de casos positivos, fallecidos y personas completamente vacunadas contra COVID-19 respecto a grupos etáreos y departamentos por año y semana epidemiológica.

   - [Data Product 2](Data/DP2_covid19-peru_resumen_x_departamentos.csv):  Dataset de casos positivos, fallecidos y totalmente vacunados por cada departamento del Perú. De la misma manera se agrega el número de habitantes de cada departamento, para calcular la tasa de mortalidad por 100 000 habitantes y el porcentaje de vacunación respectivo.

Gráficas de análisis de resultados disponibles en [Images](https://github.com/xxotto/covid19-peru/tree/main/Images).

**Ejemplo # 1:** Total de muertes por COVID-19 en Perú desde que comenzó la campaña de vacunación (SE6 del 2021) vs porcentaje de la población completamente vacunada.

![Esta es una imagen de ejemplo](https://raw.githubusercontent.com/xxotto/covid19-peru/main/Images/covid19-peru_fallecidos_vs_vacunados_x_semanaEpi.png)

## 2. Fuentes de datos ([RawData](https://github.com/xxotto/covid19-peru/tree/main/RawData))
En el directorio de  se encuentran todas las bases de datos que fueron usados para generar tablas resumen y gráficas. Las fuentes de datos se encuentran "crudas", tal y como se obtuvieron a través de la [Plataforma Nacional de Datos Abiertos](https://www.datosabiertos.gob.pe/) del Gobierno del Perú. 

1. [Fallecidos por COVID-19](https://www.datosabiertos.gob.pe/dataset/fallecidos-por-covid-19-ministerio-de-salud-minsa)
2. [Vacunación contra la COVID-19](https://www.datosabiertos.gob.pe/dataset/vacunacion)
3. [Casos positivos por COVID-19](https://www.datosabiertos.gob.pe/dataset/casos-positivos-por-covid-19-ministerio-de-salud-minsa)
4. [Centros de vacunación](https://www.datosabiertos.gob.pe/dataset/centros-de-vacunacion)
5. [Códigos equivalentes de UBIGEO del Perú](https://www.datosabiertos.gob.pe/dataset/codigos-equivalentes-de-ubigeo-del-peru)

Toda la información usada en este repositorio fue obtenida mediante fuentes oficiales como el Instituto Nacional de Estadística e Informática (INEI) o el Ministerio de Salud del Perú (MINSA).

## 3. ¿Cómo funciona?

Proximamente...

## 4. Fuentes de información

- [«Documento Técnico: Plan Nacional Actualizado de Vacunación contra la COVID-19»](https://cdn.www.gob.pe/uploads/document/file/1805113/Plan%20Nacional%20Actualizado%20contra%20la%20COVID-19.pdf). Fuente: MINSA.

- [«PERÚ: Estimaciones y Proyecciones de Población por Departamento, Provincia y Distrito, 2018 - 2020»](https://www.inei.gob.pe/media/MenuRecursivo/publicaciones_digitales/Est/Lib1715/Libro.pdf). Página 39 estimaciones de población total proyectada para 2020 por departamento. Fuente: INEI.

## 5. Contacto
   
Todos los scripts, gráficos, procesos de limpieza y manejo de bases de datos epidemiológicos fueron realizados por Otto Proaño ([@xxotto](https://github.com/xxotto)) durante el transcurso de pasantías de investigación dentro del [Laboratorio de Investigación en Enfermedades Emergentes - EmergeLab](https://investigacion.cayetano.edu.pe/catalogo/saludintegral/emerge), de la Universidad Peruana Cayetano Heredia (UPCH) bajo la supervisión de David W. Chaupis-Meza. Cualquier duda, comentario o sugerencia será bienvenida. 

Correo de contacto: otto.proano@hotmail.com

## 6. Agradecimientos

Proyecto inspirado en el repositorio [Datos-COVID19](https://github.com/MinCiencia/Datos-COVID19) de MinCiencia.
