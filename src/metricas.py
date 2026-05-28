import pandas as pd
import matplotlib.pyplot as plt

def check_df(df):
    """
    Verifica que la entreada sea efectivamente un DataFrame.

    Parameters
    ----------
    df : DataFrame

    Raises
    ------
    TypeError
        En el caso de que la entrada no sea un DataFrame.
    ValueError
        En el caso de que el DataFrame este vacio.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "Se esperaba un DataFrame."
        )
    if df.empty:
        raise ValueError(
            "El DataFrame está vacío."
        )

def calcular_tiempo_total(df):
    """
    Suma el tiempo de telefono del ususario
    
    Parámetros
    ---------
    df: DataFrame
    registro de un participante
    
    Retorna
    ------
    float
    el tiempo total de uso del telefono
    
    """
    
    check_df(df)
    return df["tiempo_uso"].sum()
    

def calcular_promedio_uso(df):
    """
    Calcula el promedio de usos de un usuario particular
    
    Parametros
    -------
    df: DataFrame
    registro de un participante
    
    Retorna
    -------
    float
    promedio
    """

usuario_elegido = 1

columnas = ["Usuario_ID", "Fecha", "Aplicacion", "Accesos", "Minutos"]
df_completo = pd.read_csv("BehaviorTracker_mock_data.(1)csv", names=columnas)

# Filtramos los datos de ese usuario y sumamos sus minutos por día
df_usuario = df_completo[df_completo["Usuario_ID"] == usuario_elegido]
datos_grafico = df_usuario.groupby("Fecha")["Minutos"].sum().reset_index()

# Hacemos el gráfico de líneas básico
plt.plot(datos_grafico["Fecha"], datos_grafico["Minutos"], marker="o")
plt.show()



def calcular_uso_app(df):

    """
    Registra la frecuencia de uso de las apps
    
    Parametros
    ----------
    dic: dict
    registro del participante
    
    
    Retorna
    -------
    dict
    frecuencias_apps
    lista vacia 
    """
    check_df(df)
    return (df["app"].value_counts().to_dict)


def graficar_uso_por_app(df):
    """
    La funcion genera un gráfico de barras con el promedio de uso por app.
    
    Parameters
    ----------
    df (DataFrame)
    datos del sistema

    Returns
    -------
    None
    """

    resumen = df.groupby("app")["cant_uso"].mean()

    resumen.plot(kind="bar")

    plt.title("Promedio de uso por app")
    plt.xlabel("App")
    plt.ylabel("Cantidad promedio de uso")
    plt.grid(True, linestyle='--', alpha=0.5, axis='y')
    plt.show()
  

