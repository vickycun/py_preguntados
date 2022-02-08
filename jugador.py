#G03_CODIGO_MP2_Cunill_Quispe_Valverde

class Jugador:
#clase en la que se realiza el molde del objeto jugador, que puede completar una corona (obteniendo 3 puntos), elegir personajes y acumularlos
    
    personajes = [("Tina", "Arte"), ("Albert", "Ciencia"), ("Tito", "Geografía"), ("Héctor", "Historia"), ("Pop", "Entretenimiento"), ("Bonzo", "Deportes")]  # lista con tuplas que tienen nombre de los personajes y las categorias


    def __init__(self):
        """Método especial constructor, con el que le damos un estado inicial a nuestro objeto de tipo Jugador """
        self.nombre = input("Nombre: ").title()  #Al instanciar en el main los objetos del tipo de esta clase, les pedimos que ingresen sus nombres y los guardamos en esta variable
        self.puntos = 0  #inicializamos en 0 los puntos que van a ir acumulandose para completar la barra corona
        self.corona = False  #Incializamos en False la corona, ya que al iniciar el juego, el jugador no va a tener puntos en la corona
        self.personajes_ganados = [] #lista con personajes ganados
        

    def __str__(self):
        """Método especial str que nos va a permitir realizar un print del nombre del objeto de tipo Jugador instanciado en otras clases, sin necesidad de usar la notación del punto"""
        return f"'{self.nombre}'"

    def sumar_puntos(self):
        """Método que a medida que el jugador acierta las respuestas, va sumando un punto a la barra corona y muestra cuantos puntos de los 3 necesarios para completar corona, se tienen hasta el momento"""
        self.puntos += 1
        print(f"Barra corona: {self.puntos} de 3")
        return self.puntos
    
    def reiniciar_puntaje(self):
        """Método que en este juego se invoca desde la clase tablero, a través de su método si_tiene_corona, que es sólo para el caso en que al tirar el bolillero, salió por random corona como categoria, por lo que reincia el puntaje a 0 """
        self.puntos = 0
        return self.puntos

    def verificar_corona(self, puntaje):
        """Método que verifica que si los puntos son iguales a 3, si es así, los reinicia a 0 y da a elegir un personaje"""
        self.puntos = puntaje
        if self.puntos == 3:
            self.corona = True
            self.puntos = 0  #si se completa la barra de corona, reiniciamos los puntos a 0
        else:
            self.corona = False
        return self.corona

    def elegir_personaje(self):
        """Método que muestra la lista con tuplas de los personajes y categorias, solicita que se elija el personaje que se desea obtener
        y retorna el personaje y la categoria"""
        print("\n***Personajes disponibles***")
        i = 1
        for personaje, categoria in self.personajes:
            print(f"{i}. {categoria}: {personaje}")
            i += 1
        num = int(input("Ingrese el número de personaje que desea ganar: "))
        personaje, categoria = self.personajes[num-1]  #desempaquetamos la tupla que está en el indice que se le pasa a la lista
        print(f"\nHas elegido {personaje}")
        return personaje, categoria

    def guardar_personaje_ganado(self, personaje, categoria):
        """Método se utiliza en el caso de que el jugador haya acertado la pregunta, entocnes guarda en la lista de los personajes_ganados, el personaje que ganó"""
        self.personajes_ganados.append(personaje)
        valor = (personaje, categoria)
        self.personajes.remove(valor)
        return self.personajes_ganados
    
    def mostrar_puntos_personajes(self):
        """Método que muestra los puntos y personajes guardados por el jugador que está vigente al momento de iniciar turno """
        print(f"Puntos: {self.puntos}")
        if len(self.personajes_ganados) == 0:
            print("Personajes obtenidos: Ninguno")
        elif len(self.personajes_ganados) == 1:
            print(f"Personajes obtenidos: {self.personajes_ganados[0]}")
        else:
            ("Personajes obtenidos: {self.personajes_ganados[0]}, {self.personajes_ganados[1]} ")
        return None
        
    def mostrar_personaje_ganado(self):
        """Método que sirve para mostrar los personajes guardados en la lista personajes_ganados, que tiene el jugador"""
        print("Personajes ganados:")
        for personaje in self.personajes_ganados:
            print(f" - {personaje}")
        return None

