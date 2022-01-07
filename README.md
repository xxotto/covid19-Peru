# COVID-19 en Perú
El objetivo del repositorio es integrar información, generar tablas resumen y visualizar datos referentes a COVID-19 de todo el Perú. Así facilitar el uso de los mismos para reportes y boletines de salud, investigaciones epidemiológicas, y apoyar en el proceso de toma de desiciones por parte de instituciones gubernamentales encargadas del área de salud.

**Fecha de última actualización: 5 de enero del 2022.**

*Nota: Repositorio aún en desarrollo. En caso no sea posible visualizar las libretas de Jupyter Notebook, utilizar la siguiente dirección [https://nbviewer.org](https://nbviewer.org).*

# Data Products (Data)
Data products, datos finales o tablas resumen obtenidos se encuentran en el directorio [Data](https://github.com/xxotto/covid19-peru/tree/main/Data). Todos los archivos se encuentran en formato de valores separados por comas (CSV).
   
   - [Data Product 1](/Data/DP1_vacunados_y_fallecidos_x_semanaEpi.csv): Dataset con el número de fallecidos y vacunados (dosis aplicadas) por COVID-19 por semana epidemiológica y departamento.

   - [Data Product 2](/Data/DP2_TOTAL_vacunados_y_fallecidos_x_departamento.csv): TOTAL de personas fallecidas y vacunadas contra COVID-19 por departamento.

Imágenes de resultados se encuentran en el directorio [Images](https://github.com/xxotto/covid19-peru/tree/main/Images).

# Fuentes de datos (RawData)
En el directorio de [RawData](/RawData/) se encuentran todas las bases de datos que fueron usados para generar tablas resumen y gráficas. Las fuentes de datos se encuentran "crudas", tal y como se obtuvieron a través de la [Plataforma Nacional de Datos Abiertos](https://www.datosabiertos.gob.pe/) del Gobierno del Perú. 

1. [Fallecidos por COVID-19](https://www.datosabiertos.gob.pe/dataset/fallecidos-por-covid-19-ministerio-de-salud-minsa)
2. [Vacunación contra la COVID-19](https://www.datosabiertos.gob.pe/dataset/vacunacion)
   
3. [Casos positivos por COVID-19](https://www.datosabiertos.gob.pe/dataset/casos-positivos-por-covid-19-ministerio-de-salud-minsa)
   
4. [Centros de vacunación](https://www.datosabiertos.gob.pe/dataset/centros-de-vacunacion)
   
5. [Códigos equivalentes de UBIGEO del Perú](https://www.datosabiertos.gob.pe/dataset/codigos-equivalentes-de-ubigeo-del-peru)

Toda la información usada en este repositorio fue obtenida mediante fuentes oficiales como el [Instituto Nacional de Estadística e Informática (INEI)](https://www.inei.gob.pe/) o el [Ministerio de Salud del Perú (MINSA)](https://www.gob.pe/minsa).

# ¿Cómo funciona?

Proximamente...

# Fuentes de información usadas

- [«Documento Técnico: Plan Nacional Actualizado de Vacunación contra la COVID-19»](https://cdn.www.gob.pe/uploads/document/file/1805113/Plan%20Nacional%20Actualizado%20contra%20la%20COVID-19.pdf). Fuente: MINSA.

- [«PERÚ: Estimaciones y Proyecciones de Población por Departamento, Provincia y Distrito, 2018 - 2020»](https://www.inei.gob.pe/media/MenuRecursivo/publicaciones_digitales/Est/Lib1715/Libro.pdf). Página 39 estimaciones de población total proyectada para 2020 por departamento. Fuente: INEI.

# Contacto
   
Todos los scripts, gráficos, procesos de limpieza y manejo de bases de datos epidemiológicos fueron realizados por Otto Proaño ([@xxotto](https://github.com/xxotto)) durante el transcurso de pasantías de investigación dentro del [Laboratorio de Investigación en Enfermedades Emergentes - EmergeLab](https://investigacion.cayetano.edu.pe/catalogo/saludintegral/emerge), de la Universidad Peruana Cayetano Heredia (UPCH) bajo la supervisión de David W. Chaupis-Meza. Cualquier duda, comentario o sugerencia será bienvenida. 

Correo de contacto: otto.proano@hotmail.com

# Agradecimientos

Proyecto inspirado en el repositorio [Datos-COVID19](https://github.com/MinCiencia/Datos-COVID19) de MinCiencia.
