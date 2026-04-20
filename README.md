# Repositorio_Proyecto_Colaborativo

Los participantes de este proyecto colaborativo son: Delfina Pauiggari, Guadalupe Margiotta, Ramiro Gago y Victoria Fagalde.

EL propósito de este proyecto es diseñar un programa que procese y analice datos de un archivo con el objetivo de encontrarpatrones de comportamiento digital de diferentes usuarios.

Errores y validaciones:
1. Un primer error que identificamos fue la posibilidad de que las listas estén vacías. Para evitar ese error, implementamos un "raise ValueError" dentro de las funciones que lo requerían.

2. Un segundo error que identificamos fue la posibilidad de la división por cero al momento de calcular un promedio. Implementamos un "ZeroDivisionError" como para aclarar que eso es un error. Sin embargo, este error es poco probable que ocurra, ya que el valor por el que se está dividiendo es el largo de una lista, que como mencinamos antes, ya establecimos el código para que no pueda ser cero.

Objetos:
En esta seccion planteariamos como quedaria el sistema si fuera orientada a objetos.

1. Class RegistroUso:
Atributos:
los datos que guarda(fecha:str, app:str, cantidad_uso:int, tiempo_uso:float)
Metodos:
resumen(): muestra los datos del registro por pantalla 

2. Class Participante: (agrupa todos sus registros de uso)
Atributos:
los datos que guarda: id_participante, registros (lista de objetos que estan asociados con la clase de RegistroUso)
Metodos:
agregar_registro(): suma un nuevo registro a su lista
calcular_tiempo_total(): devuleve la suma de todo el tiempo de uso de los registrados
calcular_promedio_uso(): devuelve el promedio diario
calcular_uso_por_app(): devuelve un diccionario con el tiempo de uso por aplicación

3. ClassCargarDatos:
Atributos: archivo.csv(ubicacion del archivo)
Metodos:
parsear_linea(linea): convierte una línea del archivo en un objeto RegistroUso
cargar_datos(): lee el archivo completo y devuelve una lista de objetos Participante





