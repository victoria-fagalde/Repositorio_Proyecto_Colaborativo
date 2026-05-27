import pandas as pd

def check_df(df):
    """
    Verifica que la entreada sea efectivamente un DataFrame.

    Parameters
    ----------
    df : DataFrame

    Raises
    ------
    TypeError
        En el caso de que la entrada no sea un DataFrame.
    ValueError
        En el caso de que el DataFrame este vacio.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "Se esperaba un DataFrame."
        )
    if df.empty:
        raise ValueError(
            "El DataFrame está vacío."
        )

def calcular_tiempo_total(df):
    """
    Suma el tiempo de telefono del ususario
    
    Parámetros
    ---------
    df: DataFrame
    registro de un participante
    
    Retorna
    ------
    float
    el tiempo total de uso del telefono
    
    """
    
    check_df(df)
    return df["tiempo_uso"].sum()
    

def calcular_promedio_uso(df):
    """
    Calcula el promedio de usos de un usuario particular
    
    Parametros
    -------
    df: DataFrame
    registro de un participante
    
    Retorna
    -------
    float
    promedio


    """
    check_df(df)
    return df["cant_uso"].mean()

def calcular_uso_app(df):

    """
    Registra la frecuencia de uso de las apps
    
    Parametros
    ----------
    dic: dict
    registro del participante
    
    
    Retorna
    -------
    dict
    frecuencias_apps
    lista vacia 
    """
    check_df(df)
    return (df["app"].value_counts().to_dict)

  

