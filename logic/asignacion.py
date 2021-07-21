from datetime import datetime
from pathlib import Path


def asignar(cursos, profes):
    '''
    Asigna los profesores a los cursos y visceversa
    '''
    # Verifica que el directorio de salida exista, de lo contrario lo crea
    Path("output").mkdir(parents=True, exist_ok=True)

    # Genera el archivo de log
    nombre_archivo = f'output/{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log'

    # Crea el archivo de log
    archivo = open(nombre_archivo, 'w')

    # Recorre los cursos
    for curso in cursos:
        # Recorre los profesores
        for profe in profes:

            # Obtiene la cantidad de cursos asignados al profesor
            cursos_profesor = [
                c for c in cursos if 'profesor' in c and c['profesor'] == profe['profesor']]

            # Verifica que las topes máximos de asignación
            # no sean superados por la cantidad de cursos asignados
            if profe["tipo"] == 'TC' and len(cursos_profesor) == 6 or profe["tipo"] == 'MT' and len(cursos_profesor) == 5:
                break

            # Recorre las franjas del curso
            matches = 0
            encontradas = []
            for franja in curso["franjas"]:
                # Busca la siguiente franja del curso en las disponibilidades del profesor
                encontrada = next((d for d in profe["disponibilidad"] if d["disponible"] and d["dia"] == franja["dia"]
                                  and d["hi"] == franja["hi"] and franja["hf"] == franja["hf"] and franja["asignada"] == False), None)

                # Si encuentra la franja, incrementa el conteo y agrega la disponibilidad del profesor
                if encontrada:
                    matches = matches + 1
                    encontradas.append(encontrada)

            # Verifica si todas las franjas de curso coincidieron
            if matches == len(curso["franjas"]):
                # Asigna el profesor al curso
                curso['profesor'] = profe["profesor"]

                # Asigna el profesor a las franjas del curso
                for franja in curso["franjas"]:
                    franja["asignada"] = True
                    franja["profesor"] = profe["profesor"]

                # Asigna el curso a las disponibilidades del profesor
                for e in encontradas:
                    e["disponible"] = False
                    e["curso"] = curso["curso"]

                # Escribe en el log
                archivo.write(
                    f'curso={curso["curso"]}, profesor={profe["profesor"]}\n')

                # Dado que se encontró un profesor para el curso,
                # no se necesita seguir buscando en la lista de profesores.
                # Este break rompe el ciclo de profesores
                break

    # Cierra el archivo de log
    archivo.close()
