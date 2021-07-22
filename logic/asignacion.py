from .globales import obtener_numero_dia


def asignar(lista_cursos, lista_profes):
    '''
    Asigna los cursos a los profesores
    '''
    # Recorre los cursos
    for curso in lista_cursos:

        # Recorre los profesores
        for profe in lista_profes:

            # Obtiene el tipo de profesor
            tipo_profesor = profe['tipo']

            # Verifica que el profesor no sobrepase
            # la cantidad de cursos asignados dado su tipo
            if (
                (tipo_profesor == 'MT' and len(profe["cursos"]) == 5) or
                (tipo_profesor == 'TC' and len(profe["cursos"]) == 6)
            ):
                # Continua con el siguiente profesor
                continue

            # Recorre las franjas del curso
            disponibilidades_validas = []
            for franja in curso['franjas']:

                # Obtiene el numero del dia de la franja
                numero_dia = obtener_numero_dia(franja['dia'])

                # Intenta obtener la disponibilidad que hace match con la HI de la franja
                disp_inicial = next(
                    (disp for disp in profe['horario'][numero_dia] if franja['hi'] >= disp['hi']
                        and franja['hi'] < disp['hf']
                        and disp['disponible']
                        and not disp['asignado']), None)

                # Intenta obtener la disponibilidad que hace match con la HF de la franja
                disp_final = next(
                    (disp for disp in profe['horario'][numero_dia] if franja['hf'] >= disp['hi']
                        and franja['hf'] < disp['hf']
                        and disp['disponible']
                        and not disp['asignado']), None)

                # Verifica si se encontró una disponibilidad inicial y final
                if disp_inicial and disp_final:
                    # Busca la posicion inicial y final
                    posicion_inicial = profe['horario'][numero_dia].index(
                        disp_inicial)
                    posicion_final = profe['horario'][numero_dia].index(
                        disp_final)

                    # Obtiene todas las disponibilidades entre
                    # la disponibilidad inicial y la final
                    disp_franja = profe['horario'][numero_dia][posicion_inicial:posicion_final+1]

                    # Verifica que todas las disponibilidades obtenidas estén disponibles
                    todas = all(d['disponible'] and not d['asignado']
                                for d in disp_franja)
                    if todas:
                        # Agrega las disponibilidades de la franja
                        disponibilidades_validas.append(disp_franja)
                    else:
                        # Si no todas las disponibilidades son válidas no continua buscando
                        break

                    # print(
                    #     f"C={curso['curso']}, F={franja['hi']}-{franja['hf']}, P={profe['profesor']}, dia={numero_dia}, inicial={posicion_inicial}->{disp_inicial['hi']}-{disp_inicial['hf']}, final={posicion_final}->{disp_final['hi']}-{disp_final['hf']} - LIBRE={todas}")

            # Verifica si todas las disponibilidades del profesor
            # están disponibles para todas las franjas de curso
            if len(curso['franjas']) == len(disponibilidades_validas):
                # Recorre las disponibilidades para marcarlas como asignadas
                for grupo in disponibilidades_validas:
                    for disponibilidad in grupo:
                        disponibilidad['asignado'] = True
                        disponibilidad['curso'] = curso['curso']
                # Recorre las franjas del curso para marcarlas como asignadas
                for franja in curso['franjas']:
                    franja['asignada'] = True
                    franja['profesor'] = profe['profesor']

                # Asigna el profesor al curso
                curso['asignado'] = True
                curso['profesor'] = profe['profesor']

                # Agrega el curso al profesor
                profe['cursos'].append(curso['curso'])

                # print(
                #     f"El profesor {profe['profesor']} fue asignado al curso {curso['curso']}")

                # No busca más profesores
                break
