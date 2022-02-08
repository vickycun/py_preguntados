#G03_CODIGO_MP2_Cunill_Quispe_Valverde
"""Detalle para identificar como está armado el diccionario:
    - Nombre del diccionario corresponde a la categoría de preguntas
    - Las claves, son las preguntas. Los valores, son otro diccionario 
    - Este otro diccionario interno, contiene las 4 opciones de respuesta (claves) y 4 valores booleanos (valores)"""

BASE_ENTRETENIMIENTO = {
    "¿Cuál de estos NO es un personaje de la serie “Vikingos”?":
        {"Ragnar": False,
	"Jon Snow": True,
	"Rollo": False,
	"Bjorn": False},
    "¿Cuál era el verdadero nombre del humorista Tato Bores?":
	{"Horacio Borenstein": False,	
	"Ronald McBores": False,
	"Mauricio Borensztein": True,
	"Juan Carlos Borensztein": False},
    "¿Cómo se llama la esposa de Goku en la saga “Dragon Ball”?":
	{"Mary": False,
	"Milk": True,
	"Lemu": False,
	"Bulma": False},
    "¿A qué oficio se dedica Peter Parker?":
	{"Dibujo": False,
	"Piano": False,
	"Fotografía": True,
	"Carpintería": False},
    "¿De qué color es el pelo del payaso Krusty?":
	{"Violeta": False,
	"Turquesa": True,
	"Rojo": False,
	"Amarillo": False}
    }
