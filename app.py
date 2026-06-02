import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.carga_datos import cargar_datos
from src.validacion_datos import validar_dataframe, validar_consistencia
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_app, graficar_uso_por_app

st.set_page_config(page_title="BehaviorTracker Dashboard", layout="wide")
st.title(" BehaviorTracker — Dashboard de Uso")


archivo = st.file_uploader("Subí tu archivo CSV de datos", type="csv")

if archivo is None:
    st.info(" Arrastrá o seleccioná el archivo CSV para comenzar.")
    st.stop()

columnas = ["id_participante", "fecha", "app", "cant_uso", "tiempo_uso"]
df = pd.read_csv(archivo, names=columnas)


try:
    validar_dataframe(df)
except ValueError as e:
    st.error(f" Error en los datos: {e}")
    st.stop()

st.success(" Archivo válido cargado correctamente.")

ids_disponibles = sorted(df["id_participante"].unique().tolist())
id_buscado = st.selectbox("Seleccioná un participante:", ids_disponibles)

try:
    validar_consistencia(df, id_buscado)
except ValueError as e:
    st.error(f" Error: {e}")
    st.stop()

df_participante = filtrar_por_participante(df, id_buscado)

st.subheader(f" Métricas del participante ID: {id_buscado}")

tiempo_total  = calcular_tiempo_total(df_participante)
promedio_uso  = calcular_promedio_uso(df_participante)
uso_apps      = calcular_uso_app(df_participante)

col1, col2, col3 = st.columns(3)
col1.metric("⏱ Tiempo total de uso", f"{tiempo_total:.2f} hs")
col2.metric(" Promedio de uso", f"{promedio_uso:.2f} hs")
col3.metric(" Apps registradas", len(uso_apps))

st.subheader(" Visualizaciones")

st.markdown("**Promedio de uso por app (dataset completo)**")
fig1, ax1 = plt.subplots()
resumen = df.groupby("app")["cant_uso"].mean()
resumen.plot(kind="bar", ax=ax1)
ax1.set_title("Promedio de uso por app")
ax1.set_xlabel("App")
ax1.set_ylabel("Cantidad promedio de uso")
ax1.grid(True, linestyle="--", alpha=0.5, axis="y")
plt.tight_layout()
st.pyplot(fig1)

st.markdown(f"**Evolución diaria del participante {id_buscado}**")
fig2, ax2 = plt.subplots()
datos_diarios = df_participante.groupby("fecha")["tiempo_uso"].sum().reset_index()
ax2.plot(datos_diarios["fecha"], datos_diarios["tiempo_uso"], marker="o")
ax2.set_title(f"Uso diario — Participante {id_buscado}")
ax2.set_xlabel("Fecha")
ax2.set_ylabel("Horas de uso")
ax2.grid(axis="y", alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig2)
