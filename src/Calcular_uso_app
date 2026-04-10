"""
DocString:
    Calcula la frecuencia de uso de las apps.
    
    Parametros:
--------------------
    dic: diccionario
    
    lista_app = list
    apps usadas por el usuario
    frecuencias_apps: dicc
    diccionario con frecuencias del uso de app
    
    Retorna:
--------------------
dicc

frecuencias_apps
"""

def calcular_uso_app(dic):
    
    lista_app = dic[1]
    frecuencias_apps = {}

    if lista_app == []:
        return []

    for app in lista_app:
        if app in frecuencias_apps:
            frecuencias_apps[app] += 1
        else:
            frecuencias_apps[app] = 1

    return frecuencias_apps

