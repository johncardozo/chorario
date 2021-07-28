import math

franjas = [
    {'hi': 700, 'hf': 715},
    {'hi': 715, 'hf': 730},
    {'hi': 730, 'hf': 745},
    {'hi': 745, 'hf': 800},
    {'hi': 800, 'hf': 815},
    {'hi': 815, 'hf': 830},
    {'hi': 830, 'hf': 845},
    {'hi': 845, 'hf': 900},
    {'hi': 900, 'hf': 915},
    {'hi': 915, 'hf': 930},
    {'hi': 930, 'hf': 945},
    {'hi': 945, 'hf': 1000},
    {'hi': 1000, 'hf': 1015},
    {'hi': 1015, 'hf': 1030},
    {'hi': 1030, 'hf': 1045},
    {'hi': 1045, 'hf': 1100},
    {'hi': 1100, 'hf': 1115},
    {'hi': 1115, 'hf': 1130},
    {'hi': 1130, 'hf': 1145},
    {'hi': 1145, 'hf': 1200},
    {'hi': 1200, 'hf': 1215},
    {'hi': 1215, 'hf': 1230},
    {'hi': 1230, 'hf': 1245},
    {'hi': 1245, 'hf': 1300},
    {'hi': 1300, 'hf': 1315},
    {'hi': 1315, 'hf': 1330},
    {'hi': 1330, 'hf': 1345},
    {'hi': 1345, 'hf': 1400},
    {'hi': 1400, 'hf': 1415},
    {'hi': 1415, 'hf': 1430},
    {'hi': 1430, 'hf': 1445},
    {'hi': 1445, 'hf': 1500},
    {'hi': 1500, 'hf': 1515},
    {'hi': 1515, 'hf': 1530},
    {'hi': 1530, 'hf': 1545},
    {'hi': 1545, 'hf': 1600},
    {'hi': 1600, 'hf': 1615},
    {'hi': 1615, 'hf': 1630},
    {'hi': 1630, 'hf': 1645},
    {'hi': 1645, 'hf': 1700},
    {'hi': 1700, 'hf': 1715},
    {'hi': 1715, 'hf': 1730},
    {'hi': 1730, 'hf': 1745},
    {'hi': 1745, 'hf': 1800},
    {'hi': 1800, 'hf': 1815},
    {'hi': 1815, 'hf': 1830},
    {'hi': 1830, 'hf': 1845},
    {'hi': 1845, 'hf': 1900},
    {'hi': 1900, 'hf': 1915},
    {'hi': 1915, 'hf': 1930},
    {'hi': 1930, 'hf': 1945},
    {'hi': 1945, 'hf': 2000},
    {'hi': 2000, 'hf': 2015},
    {'hi': 2015, 'hf': 2030},
    {'hi': 2030, 'hf': 2045},
    {'hi': 2045, 'hf': 2100},
    {'hi': 2100, 'hf': 2115},
    {'hi': 2115, 'hf': 2130},
    {'hi': 2130, 'hf': 2145},
    {'hi': 2145, 'hf': 2200},
]

dias = ['M', 'T', 'W', 'R', 'F', 'S']

colores = [
    '00FFFF00', '00FF00FF', '0000FFFF', '00000000', '00FFFFFF',  # 5-9
    '00FF0000', '0000FF00', '000000FF', '00FFFF00', '00FF00FF',  # 10-14
    '0000FFFF', '00800000', '00008000', '00000080', '00808000',  # 15-19
    '00800080', '00008080', '00C0C0C0', '00808080', '009999FF',  # 20-24
    '00993366', '00FFFFCC', '00CCFFFF', '00660066', '00FF8080',  # 25-29
    '000066CC', '00CCCCFF', '00000080', '00FF00FF', '00FFFF00',  # 30-34
    '0000FFFF', '00800080', '00800000', '00008080', '000000FF',  # 35-39
    '0000CCFF', '00CCFFFF', '00CCFFCC', '00FFFF99', '0099CCFF',  # 40-44
    '00FF99CC', '00CC99FF', '00FFCC99', '003366FF', '0033CCCC',  # 45-49
    '0099CC00', '00FFCC00', '00FF9900', '00FF6600', '00666699',  # 50-54
    '00969696', '00003366', '00339966', '00003300', '00333300',  # 55-59
    '00993300', '00993366', '00333399', '00333333',  # 60-63
]


def obtener_horario_inicial():
    horario = []
    # Recorre los días
    for dia in dias:
        horario_dia = []
        # Recorre las franjas
        for franja in franjas:
            nueva_franja = {
                'dia': dia,
                'hi': franja['hi'],
                'hf': franja['hf'],
                'disponible': False,
                'asignado': False,
                # 'profe': '',
                'curso': ''
            }
            # Agrega la franja al dia
            horario_dia.append(nueva_franja)
        # Agrega el horario del dia al horario
        horario.append(horario_dia)

    # Retorna el horario
    return horario


def obtener_numero_franja(hora_inicial):
    for indice, franja in enumerate(franjas):
        if franja['hi'] == hora_inicial:
            return indice


def obtener_numero_dia(dia):
    return dias.index(dia)


def generar_franjas_descuadradas(franja):
    # Inicializa los limites a generar
    inicio = int(franja['hi'])
    fin = int(franja['hf']) + 1

    # Inicializa la lista de franjas
    franjas = []

    # Genera las franjas de 15 minutos
    actual = inicio
    hora_inicio = actual
    while actual < fin:
        # Calcula la nueva franja
        if actual % 100 == 45:
            actual = actual + 55
        else:
            actual = actual + 15

        # Agrega la franja
        franjas.append({
            'hi': hora_inicio,
            'hf': actual
        })
        # Actualiza la hora inicial
        hora_inicio = actual

    return franjas


def color_es_oscuro(color):
    # Transforma HEX a RGB
    rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

    # Obtiene los valores R, G, B
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    # Calcula el HSP basado en el R, G y B
    hsp = math.sqrt(0.241 * (r * r) +
                    0.691 * (g * g) +
                    0.068 * (b * b))

    # Si el HSP está por debajo de 127.5, el color es oscuro
    return hsp <= 127.5
