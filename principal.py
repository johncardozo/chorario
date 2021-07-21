import time
from openpyxl import load_workbook
from logic import(
    cursos,
    disponibilidad,
    asignacion,
    generacion,
    reporte)


def main():

    # Registra el tiempo de inicio
    hora_inicio = time.time()

    print('Iniciando proceso...')

    # Carga los cursos del excel
    lista_cursos = cursos.cargar_cursos()

    # Carga los profesores del excel
    lista_profes = disponibilidad.cargar_disponibilidad()

    # Asigna los profesores a los cursos y visceversa
    asignacion.asignar(lista_cursos, lista_profes)

    # Genera el Excel resultado de la asignación
    generacion.generar_excel(lista_cursos, lista_profes)

    # Muestra el reporte de ejecución
    reporte.mostrar_reporte(lista_cursos, lista_profes)

    # Muestra el tiempo de ejecución
    print('\nProceso finalizado!')
    print("Tiempo de ejecución: %s segundos" % (time.time() - hora_inicio))


if __name__ == "__main__":
    # Se ejecuta sólo si se ejecuta como un script
    main()
