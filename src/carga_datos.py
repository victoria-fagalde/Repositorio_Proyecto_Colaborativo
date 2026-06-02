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

def cargar_datos(fuente):
    '''
    Lee un CSV y devuelve un DataFrame.
    Acepta tanto una ruta de archivo (str) como un objeto de archivo
    de Streamlit (UploadedFile), lo que permite usar la misma función
    tanto desde main.py como desde app.py.

    Parámetros:
    ----------
    fuente : str o UploadedFile
        Ruta al archivo CSV (para uso por consola) o el objeto devuelto
        por st.file_uploader() (para uso en Streamlit).

    Retorna:
    --------
    pd.DataFrame
        DataFrame con las columnas: id_participante, fecha, app,
        cant_uso, tiempo_uso.

    Raises:
    -------
    FileNotFoundError
        Si se pasa una ruta (str) y el archivo no existe.
    ValueError
        Si el archivo está vacío o no tiene el formato esperado.
    '''
    df = pd.read_csv(fuente, names=columnas)
    return df
