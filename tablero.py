#G03_CODIGO_MP2_Cunill_Quispe_Valverde

from arte_ascii import TIRANDO_BOLILLERO  #Sabemos que no suma puntos, pero le da un toque

class Tablero:
#clase que hace jugar al jugador. En esta clase no vamos a definir el constructor (o sea no vamos a darle un estado inicial, si no que vamos a dejar el que viene predeterminado implicitamente)
#ya que en este caso no necesitamos definir atributos propios de la clase, si no utilizar sus métodos, para poner a interactuar al jugador con el bolillero
    
    def jugar(self, player, boli):
        """Método que pone a interactuar al jugador y al bolillero, valiendose de otros métodos
        saca una pregunta, solicita las opciones, la respuesta y que se valide. Se sigue sacando
        preguntas hasta que pierde"""
        perdio = False
        cantidad_personajes_ganados = 0
        print(f"\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n*Es el turno de {player}*")
        player.mostrar_puntos_personajes()  #cada vez que inicia el turno del jugador, mostramos un detalle de sus puntos y personajes acumulados
        print(f"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        while not perdio and cantidad_personajes_ganados < 2:
            print(TIRANDO_BOLILLERO)
            categoria_sacada = boli.sacar_categoria()  #Pedimos a bolillero que saque la categoría. La pedimos aparte, porque también puede caer en corona y ahí el sistema de preguntar es distinto, ya que tiene que pedir personaje referido a una categoria sobre la que se le hará la pregunta
            if categoria_sacada != "Corona":  #vamos por el caso en que categoria no sea corona, o sea, que sean las otras 6
                perdio = self.ciclo_pregunta(categoria_sacada, boli)  #Invocamos al método que tiene todo el ciclo de realización de preguntas (sacar pregunta, pedir respuesta, verificar respuesta), y nos devuelve si acertó o no en un booleano
                if not perdio: 
                    puntos = player.sumar_puntos()  #como acertó, sumamos un punto llamando al método sumar_puntos de la clase Jugador
                    corona = player.verificar_corona(puntos)  #Verificamos si se completó la barra de corona llamando al método verificar_puntos
                    if corona:
                        print("Obtuviste 'Corona'")
                        perdio, cantidad_personajes_ganados = self.si_tiene_corona(player, boli)  #si obtuvo corona porque se llenó la barra, invocamos al método si tiene corona, donde pedimos personaje, iniciamos el ciclo de preguntas y nos devuelve si acertó (booleano condicion para salir del while)y la cantidad de personajes ganados (0, 1 o 2 y otra condicion para salir del while)
            else:  #en el caso que la categoria fuera corona, vamos por acá
                print("Categoría especial 'Corona'")
                perdio, cantidad_personajes_ganados = self.si_tiene_corona(player, boli)  #idem explicado más arriba               
        return cantidad_personajes_ganados  #devuelve al main la cantidad de personajes ganados, para verificar si se terminó la partida o no (jugador que gana 2 personajes, gana el juego)

    def si_tiene_corona(self, player, boli):
        """Método que en caso de obtener corona, por random de bolillero o por acumulación de puntos, pide que se elija personaje, e invoca
        al método ciclo_pregunta para iniciar proceso de sacar pregunta, mostrarla, pedir respusta y validar respuesta. Si acierta, invoca al método
        para guardar el personaje ganado y devuelve, la cantidad de personajes ganados hasta el momento (ya sea 0, 1 o 2)"""
        personaje, categoria_sacada = player.elegir_personaje()  #Pedimos al jugador que elija un personaje y recibimos el personaje y su categoria
        player.reiniciar_puntaje()  #Reinica los puntos a 0, para poder comenzar a llenar la barra corona nuevamente
        perdio = self.ciclo_pregunta(categoria_sacada, boli)  #Invocamos al método para sacar pregunta, mostrarla, pedir respuesta y validarla. Si acertó devuelve True, si perdió False
        cantidad_personajes = len(player.personajes_ganados)  #Nos trae la cantidad de personajes, que el jugador tiene ganados (puede ser 0, 1 o 2)
        if not perdio:
            print(f"\n*|*|*Has ganado el personaje: {personaje}*|*|*")
            premio = player.guardar_personaje_ganado(personaje, categoria_sacada)  #Guardamos en el jugador, el personaje que ganó al responder correctamente y que había elegido anteriormente
            cantidad_personajes = len(premio)  #volvemos a pedir la cantidad de personajes que el jugador tiene ganados (0, 1 o 2)
        return perdio, cantidad_personajes  #retorna valor booleano indicando si acertó o no y la cantida dde personajes ganados

    def ciclo_pregunta(self, categoria, boli):
        """Método que saca una pregunta, solicita a otros métodos que muestren la categoría  
        la pregunta con las opciones y que soliciten y validen la respuesta, devolviendo si perdió o ganó"""
        la_pregunta_es, opciones = boli.sacar_pregunta(categoria)  #le pedimos a boli que saque una pregunta, string que guardamos en la variable la_pregunta_es y que nos devuelva el diccionario de opciones con las posibles respuestas como clave y valor booleano como valor
        respuesta = self.mostrar_pregunta(categoria, la_pregunta_es, opciones)  #invocamos al método mostrar pregunta, al que le pasamos la categoria, la pregunta y el diccionario de opciones y nos devuelve la respuesta ingresada por el jugador
        perdio = self.verificar_respuesta(respuesta, opciones)  #verificamos que la respuesta ingresada por el jugador sea True o False y guardamos este valor en la variable perdio (variable que condiciona seguir en el while del método jugar)
        return perdio  #devolvemos al método jugar o al método si_tiene_corona (desde donde se lo haya invocado) el valor booleano que determinará si el jugador acertó o no

    def mostrar_pregunta(self, categoria, la_pregunta_es, opciones):
        """Método quee exhibe la pregunta con las 4 opciones, solicita que se elija una opcion del 1 al 4 y devuelve el texto de la respuesta."""
        print(f"\nCategoría '{categoria}'\n{la_pregunta_es}")
        aux = {}  #creamos un diccionario auxiliar,cuyas clavers serán los números del 1 al 4 y sus valores las opciones
        i = 1
        for items in opciones.keys():  #recorremos el diccionario de opciones
            aux[i] = aux.get(i, items)  #vamos guardando en un diccionario auxiliar, la clave númerica y el valor que son las posibles opciones de respuesta
            print(f"  {i}. {items}")  #imprimimos el número de respuesta y la posible respuesta a elegir
            i += 1
        numero_respuesta = int(input("\nIngrese el número de la respuesta correcta: "))  #pedimos al jugador que ingrese el número de la posible respuesta que elige como correcta 
        respuesta_usuario = aux[numero_respuesta]  #pasamos el número que era clave del diccionario auxiliar, para recuperar el texto de la opción que será la etiqueta (clave) del diccionario de opciones
        return respuesta_usuario  #devolvemos el texto de la respuesta, que será la clave a buscar en el diccionario de opciones

    def verificar_respuesta(self, respuesta_usuario, opciones):
        """Método que recibe la respuesta del usuario y el diccionario de opciones, verifica si la respuesta es True o False.
        Si la respusta era verdadera asigna 1 punto y lo manda a jugador, asigna a la variable "perdio" el valor False. Si la
        respueta era incorrecta, muestra mensaje afín y retorna que perdió con valor verdadero   """
        if opciones[respuesta_usuario]:
            print("\nRespuesta correcta!")
            perdio = False
        else:
            print("\nRespuesta incorrecta! Perdiste tu turno")
            perdio = True
        return perdio

