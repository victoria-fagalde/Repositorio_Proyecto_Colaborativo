

def parsear_linea(linea):
    if linea.strip() == "":
        return []
    
    campos = linea.strip().split(",")
    
    id_partiicpante = int(campos[0])
    fecha = campos[1].strip()
    app = campos[2].strip()
    cant_uso = int(campos[3])
    tiempo_uso = float(campos[4])
    
lista_lineas = [id_participante, fecha, app, cant_uso, tiempo_uso]

return lista_lineas 

    
'''
 La funcion copia las lineas de un archivo y las pasa a una lista.
 Recorre las lineas para parsearlas.
 
 Parámetros:
-----------
lista_lineas: list
Lista de lineas copiadas por el archivo.
Linea_strip: str
Separa las lineas en posiciones respecto a cada elemento. 

Retorna:
--------
list
Una lista con los datos ya parseados.
'''

def cargar_datos(nombre_archivo: str) -> list:
    datos = []
    registro_participante = {}
    
    with open(nombre_archivo.csv,"r") as archivo:
     for linea in archivo:
         campos = parsear_linea(linea)
         
         if len(campos) == 0:
             continue
         
         id_participante = int(campos[0])
         fecha = campos[1]
         app = campos[2]
         cant_uso = int(campos[3])
         tiempo_uso = float(campos[4])
         
         registro_participante = None
         for registro in datos:
             if registro["id_participante"] == id_participante:
                 registro_participante = registro 
                 break 
             
         if registro_participante:
              registro_participante["fecha"].append(fecha)
              registro_participante["app"].append(app)
              registro_participante["cant_uso"].append(cant_uso)
              registro_participante["tiempo_uso"].append(tiempo_uso)
         else:
             registro_participante = { "id_participante": id_participante,
                               "fecha": [fecha],"app": [app],  
                               "cant_uso": [cant_uso],"tiempo_uso": [tiempo_uso]}
             datos.append(registro_participante)
        
        
return datos 
         
        
'''
Recorre una lista parseada para convertir los valores a sus tipos correspondientes 
Carga los datos de cada uno a un diccionario donde las claves son los id de los participantes y el resto, los valores.
Luego carga los diccionarios a una lista

Parámetros:
----------
Archivo: str

datos: list
Lista a cargar con los diccionarios.
registro_participante: dicc
Diccionario con los datos de cada usuario.
id_participante: int
Numero que reconoce al usuario y su informacion.
Fecha: str

app: str
registro de las apps usadas.
cant_uso: int
cantidad de veces que el usuario usa el telefono.
tiempo_uso: float
cantidad de tiempo que el usuario usa el telefono.

Retorna:
--------
list
lista de los diccionarios registrados.
'''
