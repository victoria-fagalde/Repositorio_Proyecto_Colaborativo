def parsear_lineas(archivo):
    '''
     La funcion copia las lineas de un archivo y las pasa a una lista.
     Recorre las lineas para parsearlas.
     
     Parámetros:
    -----------
    archivo: archivo con valores a procesar 

    Retorna:
    --------
    list
    Una lista con los datos ya parseados.
    '''
    archivo_abierto = open(archivo,"r")
    lista_lineas = archivo_abierto.readlines()
    archivo_abierto.close()

    nueva_lista = []
    
    if len(lista_lineas) == 0:
        raise ValueError("La lista no puede estar vacía.")

    for linea in lista_lineas[1:]:
        linea_strip = linea.strip("\n")
        linea_split = linea_strip.split(",")
        nueva_lista.append(linea_split)
        
        
    if len(linea_split) != 5:
        raise IndexError("Error")
    
    return nueva_lista 

def cargar_datos(nueva_lista):
    '''
    Recorre una lista parseada para convertir los valores a sus tipos correspondientes 
    Carga los datos de cada uno a un diccionario donde las claves son los id de los participantes y el resto, los valores.
    Luego carga los diccionarios a una lista

    Parámetros:
    ----------
    nueva_lista: lista
    lista con los valores de un archivo ya parseados.

    Retorna:
    --------
    list
    lista de los diccionarios registrados.
    '''

    registro_participante = {}

    for linea in nueva_lista: 
        id_participante = int(linea[0])
        fecha = linea[1]
        app = linea[2]
        cant_uso = int(linea[3])
        tiempo_uso = float(linea[4])

        if id_participante not in registro_participante: 
            registro_participante[id_participante] = {"fechas":[],"apps":[],"usos":[],"tiempos":[]}

            
        registro_participante[id_participante]["fechas"].append(fecha)
        registro_participante[id_participante]["apps"].append(app)
        registro_participante[id_participante]["usos"].append(cant_uso)
        registro_participante[id_participante]["tiempos"].append(tiempo_uso) 
        
    return registro_participante
        


