# Asignación de cursos a profesores

Este programa escrito en Python intenta asignar profesores a cursos y viceversa dadas las franjas horarias de los cursos y la disponibilidad de los profesores.

## Archivos de Entrada

Este programa toma como insumo 2 archivos de excel ubicados en el folder `input`:

- cursos.xlsx
- disponibilidad.xlsx

### chorario.xlsx

Este archivo de Excel contiene los cursos con los días y horas a las que se dicta cada curso.
Las columnas del archivo son las siguientes:

A. curso: codigo del curso

B. dia: M, T, W, R, F, S

C. hora inicial: (p.e. 700, 1630)

D. hora final: (p.e. 1000, 1800)

### disponibilidad.xlsx

Este archivo de Excel contiene las franjas horarias de disponibilidad de cada uno de los profesores.
Las columnas del archivo son las siguientes:

A. profesor: nombre del profesor

B. dia: M, T, W, R, F, S

C. hora inicial: (p.e. 700, 1630)

D. hora final: (p.e. 1000, 1800)

E. Tipo de profesor (MT=Medio tiempo, TC=Tiempo completo)

La disponibilidad del profesor se debe expresar en franjas de 15 minutos. Por ejemplo, si el profesor tiene disponibilidad de 7:00am a 8:30am, el archivo debe tener las siguientes franjas:

- 700 - 715
- 715 - 730
- 730 - 745
- 745 - 800
- 815 - 830

### Observaciones de los archivos de entrada

- La lista de columnas de cada archivo debe estar desde la A hasta la D según se indica en los puntos anteriores.
- La nomenclatura de los días debe ser igual en ambos archivos.
- En el folder `input`se pueden encontrar 2 ejemplos de los archivos: `cursos_sample.xlsx` y `disponibilidad_sample.xlsx`.

## Archivos de Salida

Este programa genera 5 archivos de excel ubicados en el folder `output`:

- resultado_cursos.xlsx

  Lista de cursos con su respectivo profesor asignado. Si no se pudo asignar un profesor, la columna parecerá en blanco.

- resultado_profesores.xlsx

  Lista de profesores con sus cursos asginados. Si hay alguna franja de disponibilidad que no ha sido asignada, esta aparecerá en blanco.

- consolidado_profesores.xlsx

  Lista de profesores con el tipo de profesor, la cantidad de cursos asignados y la lista de los cursos que fueron asignados.

- resultado_horarios.xlsx

  Muestra el horario de los profesores de forma gráfica. El archivo tiene una hoja por cada uno de los profesores. En cada horario se muestran los cursos asignados y la disponibilidad que no pudo ser cubierta.

- horario_cursos_sin_asignar.xlsx

  Muestra en un solo horario todas las franjas de todos los cursos que no pudieron ser asignados. El nombre de la única hoja del archivo muestra la cantidad de cursos sin asignar.
