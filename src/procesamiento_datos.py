def filtrar_por_participante(datos, id_participante):
    """
    Selecciona los datos correspondientes a un susario/participante 
    Busca dentro de la lista el diccionario cuya id_participante coincida
    
    Parametros
    --------
    datos: list
    lista de diccionarios a filtrar
    
    id_participante: int
    numero que identifica al usuario, clave del diccionario
    
    Retorna
    -------
    dict: el diccionario del paticipante encontrado
    None: si no se encuentra el participante
    """
    if not isinstance(datos, dict):
        raise TypeError("El valor ingresado no es un diccionario.")
        
    if not isinstance(id_participante, int):
        raise TypeError("El valor ingresado es incorrecto. Debe ser un número entero")
    
    return datos.get(int(id_participante))   
