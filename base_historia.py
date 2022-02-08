#G03_CODIGO_MP2_Cunill_Quispe_Valverde
"""Detalle para identificar como está armado el diccionario:
    - Nombre del diccionario corresponde a la categoría de preguntas
    - Las claves, son las preguntas. Los valores, son otro diccionario 
    - Este otro diccionario interno, contiene las 4 opciones de respuesta (claves) y 4 valores booleanos (valores)"""


BASE_HISTORIA = {
    "¿En qué territorio actual se encontraba la antigua Sumeria?": {
	"Irak": True,
	"Canadá": False,
	"Francia": False,
	"India": False },
    "¿De qué imperio fue líder Carlomagno?": {
	"Sacro Imperio Romano Germánico": True,
	"Imperio otomano": False,
	"Imperio astrohúngaro": False,
	"Imperio bizantino": False },
    "¿Cuál de los siguientes materiales fue importante durante la Revolución Industrial?": {
	"Carbón": True,
	"Agua": False,
	"Vapor": False,
	"Aceite": False },
    "¿Quién fue el último gobernante del Imperio incaico?": {
	"Huáscar": False,
	"Atahualpa": True,
	"Rumiñahui": False,
	"Huayna Cápac": False },
    "¿Qué siglo es conocido como el “Siglo de las luces”?": {
	"Siglo XVIII": True,
	"Siglo XX": False,
	"Siglo XIX": False,
	"Siglo XV": False }
    }


