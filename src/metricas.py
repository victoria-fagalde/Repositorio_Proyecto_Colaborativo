#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def calcular_tiempo_total(dic):
    

    """
    Suma el tiempo de telefono del ususario
    
    Parámetros
    ---------
    dic: dict
    registro de un participante
    
    lista_tiempos: list
    intervalos de tiempo de uso del telefono
    
    tiempo_total: float
    acumulador de tiempos de uso
    
    Retorna
    ------
    float
    el tiempo total de uso del telefono
    
    """
    lista_tiempos = dic[3]
    if len(lista_tiempos) == 0:
        raise ValueError("La lista no puede estar vacia.")

    tiempo_total = 0
    for tiempo in lista_tiempos:
        tiempo_total += tiempo
    
    return tiempo_total


def calcular_promedio_uso(dic):
    """
    Calcula el promedio de usos de un usuario particular
    
    Parametros
    -------
    dic: dict
    registro de un participante
    
    lista_usos: list
    momentos de uso del telefono
    
    suma: float
    acumulador de veces de uso
    
    promedio:float
    promedio de usos del telefono
    
    Retorna
    -------
    float
    promedio


    """
    lista_usos = dic[2]
    
    if len(lista_usos) == 0:
        raise ValueError("La lista no puede estar vacia.")
    
    suma = 0
    for uso in lista_usos:
        suma += uso

    
        promedio = suma/ len(lista_usos)
    
    return promedio

def calcular_uso_app(dic):

    """
    Registra la frecuencia de uso de las apps
    
    Parametros
    ----------
    dic: dict
    registro del participante
    
    lista_app: list
    apps usadas por el usuario
    
    frecuencias_apps: dict
    diccionario con frecuencias del uso de apps
    
    Retorna
    -------
    dict
    frecuencias_apps
    lista vacia 
    """
    lista_apps = dic[1]
    
    if len(lista_apps) == 0:
        raise ValueError("La lista no puede estar vacia.")
    
    frecuencias_apps = {}
      
    for app in lista_apps:
        if app not in frecuencias_apps:
            frecuencias_apps[app] = 1
        else:
          frecuencias_apps[app] += 1
          
    return frecuencias_apps
  

