from openpyxl import load_workbook
from logic import cursos, disponibilidad, asignacion, generacion

def main():
    print('Iniciando proceso...')
    
    # Carga los cursos del excel
    lista_cursos = cursos.cargar_cursos()
    
    # Carga los profesores del excel
    lista_profes = disponibilidad.cargar_disponibilidad()

    # Asigna los profesores a los cursos y visceversa
    asignacion.asignar(lista_cursos, lista_profes)

    # Genera el Excel resultado de la asignación
    generacion.generar_excel(lista_cursos, lista_profes)
    
    print('Proceso finalizado!')

if __name__ == "__main__":
    # Se ejecuta sólo si se ejecuta como un script
    main()
