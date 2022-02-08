#G03_CODIGO_MP2_Cunill_Quispe_Valverde - Mini Proyecto 2 - Preguntados

from bolillero import Bolillero
from jugador import Jugador
from tablero import Tablero
from arte_ascii import PREGUNTADOS,FIN

def verificar_ganador(cant_personajes, jugador):
    """Verifica la cantidad de personajes que tiene acumulado el jugador que acaba de recibir, controla si cumple el requisito para ganar que es
    obtener 2 personajes y retorna si es ganador o no y el nombre del jugador sobre el que se está verificando"""
    if cant_personajes == 2:
        es_ganador = True
    else:
        es_ganador = False
    return es_ganador, jugador


def main():
    tablero = Tablero()
    boli = Bolillero()
    print(PREGUNTADOS)  #sabemos que no suma puntos pero queda lindo
    print("---Bienvenidos a Preguntados---\n")
    player1 = Jugador()
    player2 = Jugador()
    nadie_gano = True 
    while nadie_gano:
        cantidad_personajes = tablero.jugar(player1, boli)
        ganador, player = verificar_ganador(cantidad_personajes, player1)
        if ganador:
            gano = player1
            nadie_gano = False
        else:
            cantidad_personajes = tablero.jugar(player2, boli)
            ganador, player = verificar_ganador(cantidad_personajes, player2)
            if ganador:
                gano = player2
                nadie_gano = False    

    print(f"\n¡Felicitaciones {gano}!¡Has ganado el juego!")
    gano.mostrar_personaje_ganado()
    print("\n***Regresa pronto al preguntados***")
    print(FIN)
    return None

main()
