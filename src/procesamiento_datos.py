import pandas as pd

def filtrar_por_participante(df, id_participante):
    """
    Filtra el DataFrame por id.
    Devuelve un DataFrame con las filas del participante solicitado
    
    Parametros
    --------
    df: DataFrame
    
    id_participante: int
    numero que identifica al usuario, clave del diccionario
    
    Retorna
    -------
    dict: el diccionario del paticipante encontrado
    None: si no se encuentra el participante
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Se esperaba un DataFrame.")
        
    if not isinstance(id_participante, int):
        raise TypeError("El valor ingresado es incorrecto. Debe ser un número entero")
    
    return df[df["id_participante"]== id_participante]   
