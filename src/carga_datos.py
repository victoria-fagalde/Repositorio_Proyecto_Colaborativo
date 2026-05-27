import pandas as pd

columnas = [
    "id_participante",
    "fecha",
    "app",
    "cant_uso",
    "tiempo_uso"]

tipo_dato = {
    "id_participante": int,
    "app": str,
    "cant_uso": int,
    "tiempo_uso": float}

def cargar_datos(ruta):
    '''
    Lee el CSV y devuelve un DataFrame.

    Parámetros:
    ----------
    ruta: archivo
    
    Retorna:
    --------
    
    '''
    df = pd.read_csv(ruta, names = columnas)
        
    return df
        


