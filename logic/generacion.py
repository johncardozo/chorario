from openpyxl import Workbook
from openpyxl.styles import PatternFill
from pathlib import Path
import collections


def generar_excel_cursos(cursos):
    '''
    Genera el archivo de Excel con la asignación de profesores a cursos
    '''
    # Verifica que el directorio de salida exista, de lo contrario lo crea
    Path("output").mkdir(parents=True, exist_ok=True)

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
    # Verifica que el directorio de salida exista, de lo contrario lo crea
    Path("output").mkdir(parents=True, exist_ok=True)

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


def generar_excel_horarios(profes):
    '''
    Genera los horarios de los profesores
    '''
    # Verifica que el directorio de salida exista, de lo contrario lo crea
    Path("output").mkdir(parents=True, exist_ok=True)

    # Crea el libro de Excel
    wb = Workbook()

    # Establece el background de las celdas
    asignado_fill = PatternFill(start_color='0099CCFF',
                                end_color='0099CCFF',
                                fill_type='solid')
    no_asignado_fill = PatternFill(start_color='00FF99CC',
                                   end_color='00FF99CC',
                                   fill_type='solid')
    encabezado_fill = PatternFill(start_color='00C0C0C0',
                                  end_color='00C0C0C0',
                                  fill_type='solid')

    for profe in profes:
        # Crea una nueva hoja
        ws = wb.create_sheet(str(profe["profesor"]).lstrip().rstrip())

        # Escribe el encabezado del horario
        ws.cell(row=1, column=1, value="HI").fill = encabezado_fill
        ws.cell(row=1, column=2, value="HF").fill = encabezado_fill
        ws.cell(row=1, column=3, value="LUNES").fill = encabezado_fill
        ws.cell(row=1, column=4, value="MARTES").fill = encabezado_fill
        ws.cell(row=1, column=5, value="MIERCOLES").fill = encabezado_fill
        ws.cell(row=1, column=6, value="JUEVES").fill = encabezado_fill
        ws.cell(row=1, column=7, value="VIERNES").fill = encabezado_fill
        ws.cell(row=1, column=8, value="SABADO").fill = encabezado_fill

        # Genera los encabezados de las listas
        encabezados_hora = set()
        for disponibilidad in profe["disponibilidad"]:
            encabezados_hora.add(disponibilidad["hi"])

        # Obtiene y ordena los encabezados de las horas
        lista = list(encabezados_hora)
        lista.sort()

        # Recorre la disponibilidad del profesor
        for disponibilidad in profe["disponibilidad"]:
            # Obtiene la fila donde se escribe la HI y HF
            pos = lista.index(int(disponibilidad["hi"])) + 2

            # Escribe las horas de inicio y fin
            ws.cell(row=pos, column=1, value=disponibilidad["hi"])
            ws.cell(row=pos, column=2, value=disponibilidad["hf"])

            # Calcula la columna
            columna = 0
            if disponibilidad["dia"] == 'M':
                columna = 3
            if disponibilidad["dia"] == 'T':
                columna = 4
            if disponibilidad["dia"] == 'W':
                columna = 5
            if disponibilidad["dia"] == 'R':
                columna = 6
            if disponibilidad["dia"] == 'F':
                columna = 7
            if disponibilidad["dia"] == 'S':
                columna = 8

            # Verifica si se asignó un curso a la disponibilidad del profesor
            if "curso" in disponibilidad:
                # Asigna el background asignado
                ws.cell(row=pos, column=columna).fill = asignado_fill
                # Escribe el curso en la celda
                ws.cell(row=pos, column=columna,
                        value=disponibilidad["curso"])
            else:
                # Asigna el background no asignado
                ws.cell(row=pos, column=columna).fill = no_asignado_fill

    # Elimina la hoja original
    wb.remove(wb['Sheet'])

    # Guarda el Excel en disco
    wb.template = False
    wb.save('output/resultado_horarios.xlsx')


def generar_excel(cursos, profes):
    '''
    Genera la asignación resultante en archivos de Excel
    '''
    generar_excel_cursos(cursos)
    generar_excel_profes(profes)
    generar_excel_horarios(profes)
