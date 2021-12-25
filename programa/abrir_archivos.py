import csv

def open_geografia():
    # Abrir archivo con preguntas sobre geografía y guardarlo
    with open("geografia.csv") as csvfile:
        preguntas_geografia = list(csv.DictReader(csvfile))
    return preguntas_geografia


def open_deportes():
    # Abrir archivo con preguntas sobre deportes y guardarlo
    with open("deportes.csv") as csvfile:
        preguntas_deportes = list(csv.DictReader(csvfile))
    return preguntas_deportes


def open_interes_general():
    # Abrir archivo con preguntas sobre interes general y guardarlo
    with open("interes_general.csv") as csvfile:
        preguntas_interes_general = list(csv.DictReader(csvfile))
    return preguntas_interes_general

def open_todas():
    # Abrir archivo con preguntas sobre todas las categorias y guardarlo
    with open("todas.csv") as csvfile:
        preguntas_todas = list(csv.DictReader(csvfile))
    return preguntas_todas