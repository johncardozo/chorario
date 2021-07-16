from openpyxl import Workbook

def generar_excel_cursos(cursos):
    '''
    Genera el archivo de Excel con la asignación de profesores a cursos
    '''
    
    # Crea el libro de Excel
    wb = Workbook()
    # Obtiene la hoja activa
    ws = wb.active
    # Modifica el titulo de la hoja
    ws.title = "asignacion"
    
    # Escribe el encabezado de la tabla
    ws.cell(row=1, column=1, value="curso")
    ws.cell(row=1, column=2, value="dia")
    ws.cell(row=1, column=3, value="hi")
    ws.cell(row=1, column=4, value="hf")
    ws.cell(row=1, column=5, value="profesor")

    fila = 2
    # Recorre los cursos
    for curso in cursos:
        # Recorre las franjas del curso
        for franja in curso["franjas"]:
            # Escribe la franja en el archivo
            ws.cell(row=fila, column=1, value=curso["curso"])
            ws.cell(row=fila, column=2, value=franja["dia"])
            ws.cell(row=fila, column=3, value=franja["hi"])
            ws.cell(row=fila, column=4, value=franja["hf"])
            # Verifica si se asignó un profesor a la franja
            if "profesor" in franja:
                ws.cell(row=fila, column=5, value=franja["profesor"])
            # Incrementa la fila del archivo
            fila = fila + 1

    # Guarda el Excel en disco
    wb.template = False
    wb.save('output/resultado_cursos.xlsx')


def generar_excel_profes(profes):
    '''
    Genera la asignación de cursos a la disponibilidad de los profesores
    '''
    # Crea el libro de Excel
    wb = Workbook()
    # Obtiene la hoja activa
    ws = wb.active
    # Modifica el titulo de la hoja
    ws.title = "asignacion"
    
    # Escribe el encabezado de la tabla
    ws.cell(row=1, column=1, value="profesor")
    ws.cell(row=1, column=2, value="dia")
    ws.cell(row=1, column=3, value="hi")
    ws.cell(row=1, column=4, value="hf")
    ws.cell(row=1, column=5, value="curso")

    fila = 2    
    for profe in profes:
        for disponibilidad in profe["disponibilidad"]:
            # Escribe la disponibilidad en el archivo
            ws.cell(row=fila, column=1, value=profe["profesor"])
            ws.cell(row=fila, column=2, value=disponibilidad["dia"])
            ws.cell(row=fila, column=3, value=disponibilidad["hi"])
            ws.cell(row=fila, column=4, value=disponibilidad["hf"])
            # Verifica si se asignó un curso a la disponibilidad del profesor
            if "curso" in disponibilidad:
                ws.cell(row=fila, column=5, value=disponibilidad["curso"])
            # Incrementa la fila del archivo
            fila = fila + 1

    # Guarda el Excel en disco
    wb.template = False
    wb.save('output/resultado_profesores.xlsx')



def generar_excel(cursos, profes):
    '''
    Genera la asignación resultante en archivos de Excel
    '''
    generar_excel_cursos(cursos)
    generar_excel_profes(profes)