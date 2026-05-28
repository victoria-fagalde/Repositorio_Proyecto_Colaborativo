
from src.carga_datos import cargar_datos
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_app
from src.procesamiento_datos import filtrar_por_participante
from src.validacion_datos import validar_consistencia, validar_dataframe
from src.metricas import graficar_uso_por_app
from src.metricas import calcular_uso_promedio
ruta = "datos/BehaviorTracker_mock_data.csv"
df = cargar_datos(ruta)


graficar_uso_por_app(df)
try:
    validar_dataframe(df)
except (FileNotFoundError, PermissionError, ValueError) as e:
    print("Error al cargar el archivo:", e)
    exit()  

try:
    validar_dataframe(df)
except ValueError as e:
    print("Error en los datos", e)
    exit()

try:
    id_buscado = int(input("Ingrese el ID que busca: "))
except ValueError:
    print("El ID debe ser un número entero.")
    exit()

try:
    validar_consistencia(df, id_buscado)
except ValueError as e:
    print("Error:", e)
    exit()
        
df_participante = filtrar_por_participante(df, id_buscado)

try:
    tiempo_total = calcular_tiempo_total(df_participante)
    promedio_uso = calcular_promedio_uso(df_participante)
    uso_apps     = calcular_uso_app(df_participante)
    print(f"El usuario de ID: {id_buscado} tiene un tiempo total de uso del teléfono de: {tiempo_total} horas, \
          un uso promedio de: {promedio_uso} horas y el registro del uso de apps muestra: {uso_apps}")
          
except TypeError as e:
    print("Error de tipo:", e)
except ValueError as e:
    print("Error de valor:", e)



