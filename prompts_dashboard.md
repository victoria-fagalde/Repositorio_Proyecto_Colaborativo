
Para hacer esta entrega utilizamos la IA Claude. El primer prompt que insertamos, guiados por la estructura ROCA, fue el siguiente:

ROL: Sos un experto en diseño de interfaces web con Streamlit y Python.

OBJETIVO: Quiero que construyas el archivo app.py de mi proyecto de análisis de comportamiento de usuarios en smartphones.

CONTEXTO: (Como contexto además insertamos el README) El propósito de este proyecto es diseñar un programa que procese y analice datos de un archivo con el objetivo de encontrar patrones de comportamiento digital de diferentes usuarios.

ACCION: Sugerí los pasos y estructura para crear un app.py con Streamlit que:
1. Use st.file_uploader para cargar el CSV
2. Llame a validar_dataframe() y muestre errores con st.error()
3. Muestre KPIs con st.metric (tiempo total, promedio, apps más usadas)
4. Muestre los gráficos con st.pyplot()

