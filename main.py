#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.carga_datos import parsear_lineas, cargar_datos
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_app
from src.procesamiento_datos import filtrar_por_participante
from src.validacion_datos import validar_archivo, validar_consistencia

ruta = "datos/BehaviorTracker_mock_data_error01.csv"

try:
    validar_archivo(ruta)
except (FileNotFoundError, PermissionError, ValueError) as e:
    print("Error al cargar el archivo:", e)
    exit()

lista_datos_parseados = parsear_lineas(ruta)
datos = cargar_datos(lista_datos_parseados)

try:
    id_buscado = int(input("Ingrese el ID que busca: "))
except ValueError:
    print("El ID debe ser un número entero.")
    exit()

try:
    validar_consistencia(datos, id_buscado)
except ValueError as e:
    print("Error:", e)
    exit()
        
registro_filtrado = filtrar_por_participante(datos, id_buscado)


try:
    tiempo_total = calcular_tiempo_total(registro_filtrado)
    promedio_uso = calcular_promedio_uso(registro_filtrado)
    uso_apps     = calcular_uso_app(registro_filtrado)
    print(f"El usuario de ID: {id_buscado} tiene un tiempo total de uso del teléfono de: {tiempo_total} horas, \
          un uso promedio de: {promedio_uso} horas y el registro del uso de apps muestra: {uso_apps}")
          
except TypeError as e:
    print("Error de tipo:", e)
except ValueError as e:
    print("Error de valor:", e)

    
          
