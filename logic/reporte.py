def mostrar_reporte(lista_cursos, lista_profes):
    print('\nREPORTE:')

    print('\nCURSOS')
    print('-' * 40)

    # Imprime la lista de cursos con su profesor
    cursos_asignados = 0
    for curso in lista_cursos:
        # Verifica si el curso tiene un profesor asignado
        if 'profesor' in curso:
            cursos_asignados = cursos_asignados + 1
            print(f'Curso: {curso["curso"]} - Profesor: {curso["profesor"]}')
        else:
            print(f'Curso: {curso["curso"]} - SIN ASIGNAR')

    # Imprime los totales de cursos
    print(f'\nCantidad total de cursos: {len(lista_cursos)}')
    cursos_sin_asignar = len(lista_cursos)-cursos_asignados
    print(
        f'Cursos asignados: {cursos_asignados} ({(cursos_asignados*100)/len(lista_cursos)}%)')
    print(
        f'Cursos sin asignar: {cursos_sin_asignar} ({(cursos_sin_asignar*100)/len(lista_cursos)}%)')

    print('-' * 40)
    print('\nPROFESORES')
    lista_profes_revisar = []
    for profe in lista_profes:
        # Obtiene los cursos donde el profesor está asignado
        cursos_profe = [
            c for c in lista_cursos if 'profesor' in c and c['profesor'] == profe['profesor']]
        print(
            f'Profesor: {profe["profesor"]} - Tipo: {profe["tipo"]} - Cursos: {len(cursos_profe)}', end="")

        # Imprime los cursos del profesor
        print("[", end="")
        for index, c in enumerate(cursos_profe):
            print(f'{c["curso"]}', end="")
            # Verifica si se imprime la coma entre los cursos
            if index != len(cursos_profe)-1:
                print(',', end="")
        print("]")
