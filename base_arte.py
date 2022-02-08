#G03_CODIGO_MP2_Cunill_Quispe_Valverde
"""Detalle para identificar como está armado el diccionario:
    - Nombre del diccionario corresponde a la categoría de preguntas
    - Las claves, son las preguntas. Los valores, son otro diccionario 
    - Este otro diccionario interno, contiene las 4 opciones de respuesta (claves) y 4 valores booleanos (valores)"""


BASE_ARTE = {
    "¿Cómo se llaman las pinturas prehistóricas encontradas en cavernas?":
       {"Pinturas rupestres": True,
        "Jeroglíficos": False,
        "Pinturas vanguardistas": False,
        "Grafiti": False },
    "¿Qué músico ganó el Premio Nobel de Literatura en 2016?":
        {"Andrea Bocelli": False,
         "Carlos Gardel": False,
         "Bob Dylan": True,
         "Mick Jagger": False },
    "¿En qué país nació el escritor Stephen King?":
        {"Estados Unidos": True,
        "Reino Unido": False,
        "Canadá": False,
        "Suiza": False},
    "¿Cuál de estos es un instrumento de percusión?":
        {"La guitarra": False,
	"La batería": True,
	"El violín": False,
	"El arpa": False},
    "¿Cuál de las siguientes obras NO fue escrita por J.R.Tolkien?":
	{"El señor de los anillos": False,
	"Las crónicas de Narnia": True,
	"El hobbit": False,
	"El Silmarillion": False}
    }
