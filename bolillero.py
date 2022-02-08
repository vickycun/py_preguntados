#G03_CODIGO_MP2_Cunill_Quispe_Valverde

import random
from base_arte import BASE_ARTE
from base_ciencia import BASE_CIENCIA
from base_geografia import BASE_GEOGRAFIA
from base_historia import BASE_HISTORIA
from base_entretenimiento import BASE_ENTRETENIMIENTO
from base_deportes import BASE_DEPORTES

class Bolillero:
#clase en la que se realiza el molde del objeto Bolillero, que va a recibir las bases de datos con las preguntas, sus posibles respuestas y la respuesta correcta
#y por medio del uso de random va a sacar categoria, sacar preguntas y devolverlas a la clase Tablero, que será desde donde se manejará la interacion del juegador con el bolillero

    CATEGORIAS = ("Arte", "Ciencia", "Geografía", "Historia", "Entretenimiento", "Deportes", "Corona")  # tupla con las categorias
      

    def __init__(self):
        """Método especial constructor, con el que le damos un estado inicial a nuestro objeto de tipo Bolillero"""
        self.base_arte = BASE_ARTE  #guardamos el diccionario que está en la base importada
        self.base_ciencia = BASE_CIENCIA
        self.base_geografia = BASE_GEOGRAFIA
        self.base_historia = BASE_HISTORIA
        self.base_entretenimiento = BASE_ENTRETENIMIENTO
        self.base_deportes = BASE_DEPORTES
        self.preguntas_arte = self.base_arte.keys()  #guardamos lista de preguntas en un diccionario
        self.preguntas_ciencia = self.base_ciencia.keys()  #cuando pedimos una pregunta, le hacemos random a esta lista, vamos a buscarla a la base y nos traemos el diccionario completo (pregunta con opciones)por key
        self.preguntas_geografia = self.base_geografia.keys()
        self.preguntas_historia = self.base_historia.keys()
        self.preguntas_entretenimiento = self.base_entretenimiento.keys()
        self.preguntas_deportes = self.base_deportes.keys()
        self.pregunta = ""
        self.opciones = {}


    def sacar_categoria(self):
        """Método que nos permite buscando aleatoriamente una categoria en la Tupla CATEGORIAS """
        categoria = random.choice(self.CATEGORIAS)  
        return categoria  #devuelve un string con la categoria obtenida en random

    def sacar_pregunta(self, categoria):
        """Método que recibe la categoría (nunca puede ser corona), saca una pregunta aleatoria y devuelve la pregunta y un diccionario con las posibles respuestas"""
        if categoria == "Arte":
            self.pregunta = random.choice(list(self.preguntas_arte))  #nos devuelve string con la pregunta de la lista
            self.opciones = self.base_arte[self.pregunta]  #Traemos del diccionario las opciones (las opciones son valor de la pregunta, pero a su vez clave de la respuesta booleana)
        elif categoria == "Ciencia":
            self.pregunta = random.choice(list(self.preguntas_ciencia))
            self.opciones = self.base_ciencia[self.pregunta]
        elif categoria == "Geografía":
            self.pregunta = random.choice(list(self.preguntas_geografia))
            self.opciones = self.base_geografia[self.pregunta]
        elif categoria == "Historia":
            self.pregunta = random.choice(list(self.preguntas_historia))
            self.opciones = self.base_historia[self.pregunta]
        elif categoria == "Entretenimiento":
            self.pregunta = random.choice(list(self.preguntas_entretenimiento))
            self.opciones = self.base_entretenimiento[self.pregunta]
        elif categoria == "Deportes":
            self.pregunta = random.choice(list(self.preguntas_deportes))
            self.opciones = self.base_deportes[self.pregunta]
        return self.pregunta, self.opciones  #retorna el string pregunta y el diccionario con las opciones como claves y su valor booleano como values

