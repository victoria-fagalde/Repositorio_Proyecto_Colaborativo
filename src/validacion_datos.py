import os

apps_validas = ["instagram", "tiktok", "youtube", "twitter", "facebook", "whatsapp"]

def validar_archivo(ruta):
    """
    Valida que el archivo exista, pueda abrirse y no esté vacío.
    
    Parámetros:
    -----------
    ruta: str
        Ruta al archivo a validar.
    
    Retorna:
    --------
    None
    
    Lanza:
    ------
    FileNotFoundError: si el archivo no existe.
    PermissionError: si el archivo no puede abrirse.
    ValueError: si el archivo está vacío.
    """
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"El archivo '{ruta}' no existe. Verifique la ruta.")
    
    try:
        with open(ruta, "r") as f:
            contenido = f.read()
    except PermissionError:
        raise PermissionError(f"No se tiene permiso para abrir el archivo '{ruta}'.")
    
    if len(contenido.strip()) == 0:
        raise ValueError(f"El archivo '{ruta}' está vacío.")

def validar_fila(linea, numero_fila):
    '''
    Se asegura que la fila no esté vacía y que tenga exactamente 5 columnas.

    Parameters
    ----------
    linea : TYPE
        DESCRIPTION.
    numero_fila : TYPE
        DESCRIPTION.

    Returns
    -------
    None
    '''
    if len(linea) == 0:
        raise ValueError(f"Fila {numero_fila}: la fila esta vacia")
    if len(linea) !=5:
        raise ValueError(f"Fila {numero_fila}: se esperan 5 coulmnas, se encontraron {len(linea)}.")
    for campo in linea:
        if campo.strip() == "":
            raise ValueError(f"Fila {numero_fila}: hay un campo vacio")
  

def validar_tipos(linea, numero_fila):
    '''
    Se asegura que cada campo pueda ser convertido a su tipo correspondiente. 
    Que el id_buscado sea un numero entero, que el tiempo no sea negativo y que los campos no sean strs vacios.

    Parameters
    ----------
    linea : TYPE
        DESCRIPTION.
    numero_fila : TYPE
        DESCRIPTION.

    Returns
    -------
    None
    '''
    try:
       id_participante = int(linea[0])
    except ValueError:
        raise ValueError(f"Fila {numero_fila}: el id '{linea[0]}' no es un numero entero")
    if id_participante <0:
        raise ValueError(f"Fila {numero_fila}: el id debe ser un enteronpositivo")
    
    try:
        int(linea[3])
    except ValueError:
        raise ValueError(f"Fila {numero_fila}: la cantidad de uso '{linea[3]}' no es un número entero.")
    
    try:
        float(linea[4])
    except ValueError:
        raise ValueError(f"Fila {numero_fila}: el tiempo '{linea[4]}' no es un número válido.")
    
    
def validar_rango(linea, numero_fila):
    '''
    Comprueba que los valores numéricos estén dentro de límites válidos y que las marcas de tiempo estén en orden ascendente.
    
    Parameters
    ----------
    linea : TYPE
        DESCRIPTION.
    numero_fila : TYPE
        DESCRIPTION.

    Returns
    -------
    None
    '''
    
    tiempo = float(linea[4])
    if tiempo < 0:
        raise ValueError(f"Fila {numero_fila}: el tiempo no puede ser negativo.")
    
    cant_uso = int(linea[3])
    if cant_uso < 0:
        raise ValueError(f"Fila {numero_fila}: la cantidad de uso no puede ser negativa.")

    if linea[2].strip() not in apps_validas:
        raise ValueError(f"Fila {numero_fila}: la app '{linea[2]}' no es una categoría válida.")


def validar_consistencia(datos, id_participante):
    '''
    Se asegura que datos no este vacio, que el participante exista, y que las listas tienen las suficientes entradas para calcular las metricas.

    Parameters
    ----------
    datos : TYPE
        DESCRIPTION.
    id_participante : TYPE
        DESCRIPTION.

    Returns
    -------
    None
    '''
    if len(datos) == 0:
        raise ValueError("La base de datos está vacía.")
    
    registro = datos.get(int(id_participante))
    if registro is None:
        raise ValueError(f"No se encontró ningún participante con id {id_participante}.")
    
    if len(registro["tiempos"]) == 0:
        raise ValueError(f"El participante {id_participante} no tiene datos suficientes.")
