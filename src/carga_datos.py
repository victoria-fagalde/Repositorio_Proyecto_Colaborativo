#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def parsear_lineas(archivo):
    archivo_abierto = open(archivo.csv,"r")
    lista_lineas = archivo_abierto.readlines()
    archivo_abierto.close()

    if len(lista_lineas) == 0:
        return []

    for linea in lista_lineas[1:]:
        linea_strip = linea.strip("\n")
        linea_split = linea_strip.split(",")

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

def cargar_datos(lista_lineas):
    datos = []
    registro_participante = {}

    for linea in lista_lineas: 
         id_participante = int(linea[0])
         fecha = linea[1]
         app = linea[2]
         cant_uso = int(linea[3])
         tiempo_uso = float(linea[4])

    if id_participante not in registro_participante:
        registro_participante[id_participante] = [ [], [], [], [] ]
    else:
        registro_participante[id_participante][0].append(fecha)
        registro_participante[id_participante][1].append(app)
        registro_participante[id_participante][2].append(cant_uso)
        registro_participante[id_participante][3].append(tiempo_uso)

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


