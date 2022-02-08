#G03_CODIGO_MP2_Cunill_Quispe_Valverde
"""Detalle para identificar como está armado el diccionario:
    - Nombre del diccionario corresponde a la categoría de preguntas
    - Las claves, son las preguntas. Los valores, son otro diccionario 
    - Este otro diccionario interno, contiene las 4 opciones de respuesta (claves) y 4 valores booleanos (valores)"""

BASE_DEPORTES = {
    "¿Cuántos expulsados hubo en el Mundial de México 1970?": {
	"14": False,
	"Ninguno":True,
	"2": False,
	"8": False },
    "¿Cómo se le llama a tocar la pelota con el talón en fútbol?": {
	"Taco": True,
	"Taloneada": False,
	"Pase de Aquiles": False,
	"Pase a espaldas": False },
    "¿Cuál es el apodo más famoso del ex nadador Michael Phelps?": {
	"El rayo de Baltimore": False,
	"El tiburón de Baltimore": True,
	"El coyote de Baltimore": False,
	"El pez de Baltimore": False },
    "¿Cuántos jugadores en cancha, incluyendo al arquero, tiene un equipo de handball?": {
	"6": False,
	"8": False,
	"7": True,
	"11": False },
    "¿Quién ganó cuatro mundiales consecutivos de Fórmula 1?": { 
	"Sebastián Vettel": True,
	"Fernando Alonso": False,
	"Lewis Hamilton": False,
	"Kimi Raikkonen": False }
    }
