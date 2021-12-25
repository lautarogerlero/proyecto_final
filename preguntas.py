    # Funcion para hacer las preguntas y sumar los puntajes.
    # Ingresa los nombres de los jugadores y los guarda en un diccionario para
    # ir sumando los puntos obtenidos por cada uno.
    # A cada jugador le hace la pregunta que corresponde y suma +1 en la linea de las 
    # preguntas para pasar a la siguiente.
    # Esto se repite la cantidad de rondas que dure el juego.


def juego(cantidad_rondas, cantidad_jugadores, preguntas, categoria):

    jugadores = {}
    linea = 0

    for jugador in range(cantidad_jugadores):
        nombre = str(input(f"Ingrese el nombre del jugador {jugador+1}:\n")).capitalize()
        jugadores[nombre] = 0

    for rondas in range(cantidad_rondas):
        print(f"Ronda numero {rondas+1}")
        for jugador in jugadores:
            pregunta = preguntas[linea]["pregunta"]
            opcion_1 = preguntas[linea]["respuesta_1"]
            opcion_2 = preguntas[linea]["respuesta_2"]
            opcion_3 = preguntas[linea]["respuesta_3"]
            opcion_4 = preguntas[linea]["respuesta_4"]
            respuesta_correcta = int(preguntas[linea]["respuesta_correcta"])

            print(f"Turno de {jugador}")
            print(f"La pregunta sobre {categoria} es: {pregunta}")
            print("Opción 1:", opcion_1)
            print("Opción 2:", opcion_2)
            print("Opción 3:", opcion_3)
            print("Opción 4:", opcion_4)
            eleccion = int(input("Elija el numero de la opción correcta:\n"))
            if eleccion == respuesta_correcta:
                print("Respuesta correcta! Sumas un punto :)")
                jugadores[jugador] += 1
            else:
                print("Incorrecto. La respueta correcta es la numero {}".format(respuesta_correcta))
            
            linea += 1
    
    return jugadores