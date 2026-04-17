#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.carga_datos import parsear_lineas, cargar_datos
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_app
from src.procesamiento_datos import filtrar_por_participante

ruta = "datos/BehaviorTracker_mock_data.csv"

lista_datos_parseados = parsear_lineas(ruta)
datos = cargar_datos(lista_datos_parseados)

id = input("Ingrese el ID que busca: ")

registro_filtrado = filtrar_por_participante(datos, id)

for registro in datos:
   if registro == registro_filtrado:
      tiempo_total = calcular_tiempo_total(registro)
      promedio_uso = calcular_promedio_uso(registro)
      uso_apps = calcular_uso_app(registro)

print(f"El usuario de ID: {id} tiene un tiempo total de uso del teléfono de: {tiempo_total} horas, \
      un uso promedio de: {promedio_uso} horas y el registro del uso de apps muestra: {uso_apps}")

      
