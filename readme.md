# Asignación de cursos a profesores

Este programa escrito en Python intenta asignar profesores a cursos y visceversa dadas las franjas horarias de los cursos y la disponibilidad de los profesores.

## Archivos de Entrada

Este programa toma como insumo 2 archivos de excel ubicados en el folder `input`:

- cursos.xlsx
- disponibilidad.xlsx

### chorario.xlsx

Este archivo de Excel contiene los cursos con los días y horas a las que se dicta cada curso.
Las columnas del archivo son las siguientes:

A. curso: codigo del curso

B. dia: L, M, I, J, V, S, D

C. hora inicial: (p.e. 700, 1630)

D. hora final: (p.e. 1000, 1800)

### disponibilidad.xlsx

Este archivo de Excel contiene las franjas horarias de disponibilidad de cada uno de los profesores.
Las columnas del archivo son las siguientes:

A. profesor: nombre del profesor

B. dia: L, M, I, J, V, S, D

C. hora inicial: (p.e. 700, 1630)

D. hora final: (p.e. 1000, 1800)

### Observaciones de los archivos de entrada

- La lista de columnas de cada archivo debe estar desde la A hasta la D según se indica en los puntos anteriores.
- La nomenclatura de los días debe ser igual en ambos archivos, tanto en los días de la semana como en las horas.
- Las horas de inicio y fin deben ser coincidentes en ambos archivos. Por ejemplo, si las franjas de los cursos son 700-800, 800-900, 900-1000, la disponibilidad del profesor debería ser 700-800 y 800-900, y no: 700-900.
- En el folder `input`se pueden encontrar 2 ejemplos de los archivos: `cursos_sample.xlsx` y `disponibilidad_sample.xlsx`.

## Archivos de Salida

Este programa genera 2 archivos de excel ubicados en el folder `output` y un archivo de `log`. El archivo de log tiene como nombre la estructura `YYYY-MM-DD-HH-MM-SS.log`.

- resultado_cursos.xlsx
- resultado_profesores.xlsx
- archivo de log
