#G03_CODIGO_MP2_Cunill_Quispe_Valverde
"""Detalle para identificar como está armado el diccionario:
    - Nombre del diccionario corresponde a la categoría de preguntas
    - Las claves, son las preguntas. Los valores, son otro diccionario 
    - Este otro diccionario interno, contiene las 4 opciones de respuesta (claves) y 4 valores booleanos (valores)"""

BASE_GEOGRAFIA = {
    "¿En qué continente se encuentran las Islas Feroe?": {
	"Asia": False,
	"Oceanía": False,
	"Europa": True,
	"América": False},
    "¿Cuál es el desierto más seco del mundo?": {
	"Sahara": False,
	"Sonora": False,
	"Atacama": True,
	"Egipcio": False},
    "¿Cómo se llaman las personas nacidas en el Principado de Mónaco?": {
	"Monaquenses": False,
	"Monarcas": False,
	"Monegascos": True,
	"Monaquesinos": False},
    "¿Qué país tiene el mismo huso horario en todo su territorio?": {
	"España": False,
	"Australia": False,
	"China": True,
	"Rusia": False},
    "¿En qué país se comenzó a tomar café por primera vez?": {
	"Marruecos": False,
	"Arabia": False,
	"Etiopía": True,
	"Colombia": False}
    }

