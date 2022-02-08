#G03_CODIGO_MP2_Cunill_Quispe_Valverde
"""Detalle para identificar como está armado el diccionario:
    - Nombre del diccionario corresponde a la categoría de preguntas
    - Las claves, son las preguntas. Los valores, son otro diccionario 
    - Este otro diccionario interno, contiene las 4 opciones de respuesta (claves) y 4 valores booleanos (valores)"""


BASE_CIENCIA = {
    "¿Qué otro nombre tiene el dedo gordo del pie?": {
	"Primer metacarpiano": False,
	"Chubby": False,
	"Hallux": True,
	"Quinto metatarsiano": False},
    "¿Qué tipo de mamífero es el conejo?": {
	"Primate": False,
	"Lagomorfo": True,
	"Marsupial": False,
	"Equino": False},
    "¿En qué año Albert Einstein publicó la teoría de la relatividad general?": {
	"1950": False,
	"1903": False,
	"1910": False,
	"1915": True},
    "¿Cuánto dura un día en Venus?": {
	"243 días": True,
	"9,9 horas": False,
	"7 días": False,
	"365 días": False} ,
    "¿Cuáles son las células del páncreas encargadas de segregar insulina?":{
	"Células de Langerhans": False,
	"Células gama": False,
	"Células alfa": False,
	"Células beta": True}
    }
