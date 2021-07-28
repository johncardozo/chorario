from terminaltables import AsciiTable


def mostrar_reporte(lista_cursos, lista_profes):

    # print('\nCURSOS')
    # Datos de los profesores
    cursos_data = [
        ['Curso', 'Profesor']
    ]

    # Agrega los datos de los cursos
    cursos_asignados = 0
    for curso in lista_cursos:
        fila = []
        fila.append(curso["curso"])
        # Verifica si el curso fue asignado
        if curso['asignado'] and 'profesor' in curso:
            cursos_asignados = cursos_asignados + 1
            fila.append(curso["profesor"])
        else:
            fila.append("Sin asignar")
        # Agrega la fila a los datos
        cursos_data.append(fila)

    # Genera la tabla de cursos
    table_cursos = AsciiTable(cursos_data)
    # Muestra la tabla
    # print(table_cursos.table)

    print('\nPROFESORES')
    # Datos de los profesores
    profesores_data = [
        ['Profesor', 'Tipo', 'Asignación', 'Cursos']
    ]
    # Agrega los datos de los profesores
    for profe in lista_profes:
        fila = []
        fila.append(profe["profesor"])
        fila.append(profe["tipo"])
        fila.append(len(profe["cursos"]))
        fila.append(','.join(map(str, profe["cursos"])))
        profesores_data.append(fila)

    # Genera la tabla de profesores
    table_profesores = AsciiTable(profesores_data)
    # Muestra la tabla
    print(table_profesores.table)

    # Obtiene la cantidad de cursos sin asignar
    cursos_sin_asignar = len(lista_cursos)-cursos_asignados

    # Datos finales
    final_data = [
        ['Dato', 'Resultado'],
        ['Cantidad total de NRC', f'{len(lista_cursos)}'],
        ['NRC asignados',
            f'{cursos_asignados} ({(cursos_asignados*100)/len(lista_cursos)}%)'],
        ['NRC sin asignar',
            f'{cursos_sin_asignar} ({(cursos_sin_asignar*100)/len(lista_cursos)}%)'],
    ]
    # Genera la tabla final
    table_final = AsciiTable(final_data)
    # Muestra la tabla final
    print(table_final.table)
