def filtrar_por_participante(datos: list, id_participante: int) -> dict:
"""
Selecciona los datos correspondientes a un susario/participante 
Busca dentro de la lista el diccionario cuya id_participante coincida

Parametros:
datos: list
lista de diccionarios a filtrar

id_participante: int
numero que identifica al usuario, clave del diccionario

Retorna:
dict: el diccionario del paticipante encontrado
None: si no se encuentra el participante
"""
    
  for diccionario in datos:
    if id "id_participante" in diccionario: 
      if diccionario["id_participante"]==id_participante: 
        return diccionario
  return None
