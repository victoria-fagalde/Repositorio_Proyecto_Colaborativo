import pandas as pd

apps_validas = ["instagram", "tiktok", "youtube", "twitter", "facebook", "whatsapp"]

def validar_dataframe(df):
    """
    Valida que el el DataFrame exista, pueda abrirse y no esté vacío.
    
    Parameters:
    -----------
    ruta: str
        Ruta al archivo a validar.
    
    Returns:
    --------
    None
    
    Raises:
    ------
    ValueError: si el DataFrame tiene filas inválidas.
    """
    errores = []

    if df.isnull().values.any():
        errores.append("Hay valores vacíos en el dataset.")

    if (df["id_participante"] < 0).any():
        errores.append("Hay IDs negativos.")

    if (df["cant_uso"] < 0).any():
        errores.append("Hay valores negativos en cant_uso.")

    if (df["tiempo_uso"] < 0).any():
        errores.append("Hay valores negativos en tiempo_uso.")

    if not df["app"].isin(apps_validas).all():
        errores.append("Hay apps que no son válidas.")

    if errores:
        raise ValueError(
            "Errores en el dataset:\n" + "\n".join(errores)
        )

def validar_consistencia(df, id_buscado):
    '''
    Se asegura que datos no este vacio, que el participante exista, y que las listas tienen las suficientes entradas para calcular las metricas.

    Parameters
    ----------
    datos : dict
        Diccionario con los datos de un id.
    id_participante : int
        Numero que representa a cada participante.

    Returns
    -------
    None
    
    Raises
    -----
    ValueError: si el diccionario o las listas estan vacias o si no se encuentra el participante.
    
    '''
    if df.empty:
        raise ValueError("El DataFrame esta vacio")
    if id_buscado not in (df["id_participante"].values):
        raise ValueError(f"No existe el participante {id_buscado}")
