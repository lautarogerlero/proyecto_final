# Juego de preguntas y respuestas
# Autor: Lautaro Gerlero
# Version: 1.0

import csv
import random
import operator
from abrir_archivos import open_geografia, open_deportes, open_interes_general, open_todas
from preguntas import juego
from resultados import agregar_ganadores


if __name__ == "__main__":
    # Bienvenida e instrucciones
    print("Bienvenidos al juego de preguntas y respuestas!!")
    print("El juego puede tener un máximo de 4 jugadores y 10 rondas. Los jugadores pueden elegir ")
    print("responder solamente preguntas de geografia, de deportes o de interes general. También")
    print("tienen la opción de elegir todas las categorias y que en cada ronda se les hagan tres")
    print("preguntas a cada jugador, una de cada categoría.")
    print("Una vez completado el juego pueden cerrarlo o volver a empezar.")
    print("Ahora sí están listos para empezar. Mucha suerte!!")

    preguntas_geografia = open_geografia()
    preguntas_deportes = open_deportes()
    preguntas_interes_general = open_interes_general()
    preguntas_todas = open_todas()

    while True:
        # Mezclar las preguntas para que no se repita el orden
        random.shuffle(preguntas_geografia)
        random.shuffle(preguntas_deportes)
        random.shuffle(preguntas_interes_general)
        random.shuffle(preguntas_todas)

        # Usuario ingresa numero de jugadores, de rondas y la categoría
        cantidad_jugadores = int(input("Ingrese cuantos jugadores participarán (máximo 4):\n"))
        cantidad_rondas = int(input("Ingrese cuantas rondas van a jugar (máximo 10):\n"))
        categoria = str(input("Que categoria eligen? (interes general, geografia, deportes o todas):\n")).lower()
        categorias_posibles = ["geografia", "deportes", "interes general", "todas"]

        if 0 < cantidad_jugadores <= 4 and 0 < cantidad_rondas <= 10:
            if categoria in categorias_posibles:
            
                if categoria == "geografia":
                    # Llama a la función, hace las preguntas y muestra los puntajes finales
                    puntajes = juego(cantidad_rondas, cantidad_jugadores, preguntas_geografia, categoria)

                elif categoria == "deportes":
                    # Llama a la función, hace las preguntas y muestra los puntajes finales
                    puntajes = juego(cantidad_rondas, cantidad_jugadores, preguntas_deportes, categoria)
                
                elif categoria == "interes general":
                    # Llama a la función, hace las preguntas y muestra los puntajes finales
                    puntajes = juego(cantidad_rondas, cantidad_jugadores, preguntas_interes_general, categoria)

                else:
                    # Llama a la función, hace las preguntas y muestra los puntajes finales
                    puntajes = juego(cantidad_rondas, cantidad_jugadores, preguntas_todas, categoria)
            
                # Ordenar el diccionario segun los puntajes
                puntajes_ordenados = sorted(puntajes.items(), key=operator.itemgetter(1), reverse=True)
                print(f"La tabla de posiciones final es {puntajes_ordenados}")  

                # Guardar al ganador y su puntaje como un diccionario aparte
                ganador = dict([puntajes_ordenados[0]])

                # Obtener el nombre del ganador
                nombre_ganador = list(ganador.keys())
                print(f"El ganador es {nombre_ganador}")

                # Obtener el puntaje del ganador
                puntaje_ganador = list(ganador.values())

                # Llamar a la función que agrega al ganador y su puntaje al registro final
                nuevo_ganador = agregar_ganadores(nombre_ganador, puntaje_ganador)
                print("El registro de ganadores se puede ver en el archivo 'ganadores'.")

                # Desea iniciar un nuevo juego o terminar?
                seguir = str(input("Si desea finalizar escriba 'FIN', sino se reiniciará el juego:\n")).upper()
                if seguir == "FIN":
                    break

            else:
                print("Por favor ingrese una categoria válida")
        

        else:
            print("Por favor ingrese una cantidad valida de jugadores y de rondas")



    

