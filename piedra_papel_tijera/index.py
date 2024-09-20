import time
import random

PuntajeCompu = 0
Mipuntaje = 0

def mostrar_puntaje():
    print(f"\nPuntaje actual -> Bot1: {Mipuntaje} | Computadora: {PuntajeCompu}\n")
    time.sleep(1)

def jugar():
    global PuntajeCompu, Mipuntaje

    while PuntajeCompu < 3 and Mipuntaje < 3:
        misopciones = random.randint(1, 3)
        computadora = random.randint(1, 3)
        
        opciones = {1: "piedra", 2: "papel", 3: "tijera"}
        
        print(f"Bot1 eligió {opciones[misopciones]}")
        print(f"Computadora eligió {opciones[computadora]}")
        
        # Evaluamos el resultado
        if misopciones == computadora:
            print("Hay un empate 😲")
        elif (misopciones == 1 and computadora == 2):
            print("Bot1 ha perdido 👿 y Bot2 ha ganado 🥳")
            PuntajeCompu += 1
        elif (misopciones == 1 and computadora == 3): 
            print("Bot1 ha ganado 🥳 y Bot2 ha perdido 🥴")
            Mipuntaje += 1
        elif (misopciones == 2 and computadora == 1):
            print("Bot1 ha ganado 😁 y Bot2 ha perdido 🥴")
            Mipuntaje += 1
        elif (misopciones == 2 and computadora == 3): 
            print("Bot1 ha perdido 🤕 y Bot2 ha ganado 🥳")
            PuntajeCompu += 1
        elif (misopciones == 3 and computadora == 1):
            print("Bot1 ha perdido 🥴 y Bot2 ha ganado 🥳")
            PuntajeCompu += 1
        elif (misopciones == 3 and computadora == 2): 
            print("Bot1 ha ganado 🤩 y Bot2 ha perdido 🥴")
            Mipuntaje += 1
        
        mostrar_puntaje()
        
    
    if PuntajeCompu == 3:
        print("La Computadora ha ganado el juego 🏆")
    else:
        print("¡Bot1 ha ganado el juego! 🎉")

    print(f"\nPuntaje final - Bot1: {Mipuntaje} | Computadora: {PuntajeCompu}")
    print("Gracias por jugar!")


jugar()

