from openpyxl import load_workbook
profes = []

def cargar_disponibilidad():
    '''
    Carga la disponibilidad de los profesores en el Excel. 
    return Lista de profesores de tipo diccionario.
    '''
    # Abre el libro
    wb = load_workbook(filename = 'input/disponibilidad.xlsx')
    # Obtiene la página activa
    ws = wb.active

    # Inicializacion de variables
    fila = 2
    # Recorre la disponibilidad de los profesores
    while ws.cell(row=fila, column=1).value is not None:
        # Crea la disponibiliad horaria del profesor
        disponibilidad = {
            "profesor": ws.cell(row=fila, column=1).value,
            "dia" : ws.cell(row=fila, column=2).value,
            "hi" : ws.cell(row=fila, column=3).value,
            "hf" : ws.cell(row=fila, column=4).value
        }
        # Se ubica en la siguiente fila
        fila = fila + 1
        # Agrega la disponibilidad
        agregar_disponibilidad(disponibilidad)
    
    return profes


def agregar_disponibilidad(disponibilidad):
    '''
    Agrega la disponibilidad
    '''
    # Intenta encontrar el profesor
    profe_encontrado = next((p for p in profes if p["profesor"] == disponibilidad["profesor"]), None)

    # Crea la nueva disponibilidad
    nueva_disp = {
        "dia": disponibilidad["dia"],
        "hi": disponibilidad["hi"],
        "hf": disponibilidad["hf"],
        "disponible": True
    }

    # Verifica si existe el profesor
    if profe_encontrado is None:
        # Crea el nuevo curso
        nuevo_profe = {
            "profesor": disponibilidad["profesor"],
            "disponibilidad": [ nueva_disp ]
        }
        # Agrega el curso al chorario
        profes.append(nuevo_profe)
    else:
        # Agrega la disponibilidad al curso encontrado en el chorario
        profe_encontrado["disponibilidad"].append(nueva_disp)

    