# Documento de Diseño — BehaviorTracker

## Descripción General

BehaviorTracker es un sistema de análisis del comportamiento digital en smartphones.
Procesa datos de uso de aplicaciones móviles por participante, aplica validaciones
sobre los datos y genera métricas y visualizaciones.

El sistema tiene dos interfaces de usuario:
- **`main.py`**: orquestador por consola (interacción por input de teclado).
- **`app.py`**: dashboard web interactivo construido con Streamlit.

---

## Estructura del Repositorio

```
/
├── datos/                  # Datasets CSV de prueba
├── diagramas/              # Diagramas de flujo del sistema
├── graficos/               # Imágenes exportadas por la analítica
├── src/                    # Módulos auxiliares
│   ├── carga_datos.py
│   ├── metricas.py
│   ├── procesamiento_datos.py
│   ├── validacion_datos.py
│   └── diseño.md           # Este archivo
├── app.py                  # Interfaz web Streamlit
├── main.py                 # Orquestador por consola
├── prompts_dashboard.txt   # Bitácora de prompts
└── README.md
```

---

## Formato del Dataset

El archivo CSV no tiene encabezado. Las columnas se asignan en el orden siguiente:

| Columna          | Tipo    | Descripción                                      |
|------------------|---------|--------------------------------------------------|
| `id_participante`| `int`   | Identificador único del participante             |
| `fecha`          | `str`   | Fecha del registro (formato YYYY-MM-DD)          |
| `app`            | `str`   | Nombre de la aplicación usada                    |
| `cant_uso`       | `int`   | Cantidad de veces que se abrió la app ese día    |
| `tiempo_uso`     | `float` | Tiempo de uso en horas                           |

**Apps válidas:** `instagram`, `tiktok`, `youtube`, `twitter`, `facebook`, `whatsapp`

---

## Módulos

### `src/carga_datos.py`

**Función:** `cargar_datos(fuente)`

Carga el CSV y devuelve un DataFrame con las columnas definidas.
Acepta tanto una ruta de archivo (`str`) como un objeto `UploadedFile` de Streamlit,
lo que permite reutilizar la misma función en ambas interfaces sin modificación.

---

### `src/validacion_datos.py`

**Función:** `validar_dataframe(df)`

Valida la integridad del DataFrame. Lanza `ValueError` si detecta:
- Valores nulos en cualquier columna
- IDs de participante negativos
- Valores negativos en `cant_uso` o `tiempo_uso`
- Apps que no pertenecen a la lista de apps válidas

**Función:** `validar_consistencia(df, id_buscado)`

Verifica que el DataFrame no esté vacío y que el `id_buscado` exista en los datos.
Lanza `ValueError` si alguna condición falla.

---

### `src/procesamiento_datos.py`

**Función:** `filtrar_por_participante(df, id_participante)`

Filtra el DataFrame devolviendo solo las filas del participante indicado.
Lanza `TypeError` si los argumentos no son del tipo correcto.

---

### `src/metricas.py`

**Función:** `calcular_tiempo_total(df)` → `float`
Suma el tiempo de uso total del participante.

**Función:** `calcular_promedio_uso(df)` → `float`
Calcula el promedio de horas de uso.

**Función:** `calcular_uso_app(df)` → `dict`
Devuelve un diccionario con la frecuencia de uso de cada app.

**Función:** `graficar_uso_por_app(df)` → `matplotlib.figure.Figure`
Genera un gráfico de barras con el promedio de uso por app sobre el dataset completo.
Retorna la figura para que pueda ser renderizada con `st.pyplot()` en Streamlit.

---

## Flujo de la Interfaz Web (`app.py`)

```
Usuario sube CSV
       │
       ▼
cargar_datos(archivo)
       │
       ▼
validar_dataframe(df) ──── error ──→ st.error() + st.stop()
       │
       ▼
st.selectbox → id_buscado
       │
       ▼
validar_consistencia(df, id_buscado) ── error ──→ st.error() + st.stop()
       │
       ▼
filtrar_por_participante(df, id_buscado)
       │
       ▼
calcular_tiempo_total / calcular_promedio_uso / calcular_uso_app
       │
       ▼
st.metric (KPIs) + st.pyplot (gráficos)
```

---

## Flujo del Orquestador por Consola (`main.py`)

```
cargar_datos(ruta)
       │
       ▼
validar_dataframe(df)
       │
       ▼
input() → id_buscado
       │
       ▼
validar_consistencia(df, id_buscado)
       │
       ▼
filtrar_por_participante → métricas → print()
```
