
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
