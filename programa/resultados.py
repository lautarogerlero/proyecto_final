# Funcion para editar el archivo "ganadores"

import csv

def agregar_ganadores(ganador, puntaje):
    header = ["ganador", "puntaje total"]
    csvfile = open("ganadores.csv", "a", newline="")
    writer = csv.DictWriter(csvfile, fieldnames=header)
    nuevo_ganador = {"ganador": ganador, "puntaje total":puntaje}
    writer.writerow(nuevo_ganador)
    csvfile.close()

