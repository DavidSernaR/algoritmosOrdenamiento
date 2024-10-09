"""
Autores: Esteban Julián Ortega Tapie, Yeison Andrés Marín Martínez y David Serna Restrepo
Docente: Ing. Carlos Andrés Florez Villarraga
Facultad: Ingeniería
Programa: Ingeniería de Sistemas y Computación
Institución Educativa: Universidad del Quindío

Descripción:
Este programa implementa varios algoritmos de búsqueda (búsqueda lineal, búsqueda lineal limitada,
búsqueda binaria y búsqueda por saltos) y mide su tiempo de ejecución sobre arreglos de números 
aleatorios de 8 dígitos. Los datos se generan aleatoriamente y se almacenan en archivos de texto. 
El rendimiento de cada algoritmo se evalúa y se presenta en gráficos.

Funciones:
1. generar_archivo_texto(nombre_archivo, size): Genera un archivo de texto con números aleatorios de 8 dígitos.
2. cargar_arreglo_desde_archivo(nombre_archivo): Carga y retorna un arreglo de enteros desde un archivo de texto.
3. busqueda_lineal(arr, x): Realiza una búsqueda lineal en el arreglo arr para encontrar el valor x.
4. busqueda_lineal_limitada(arr, x, limite): Realiza una búsqueda lineal en el arreglo arr hasta un límite.
5. busqueda_binaria(arr, x): Realiza una búsqueda binaria en un arreglo ordenado arr para encontrar el valor x.
6. busqueda_por_saltos(arr, x): Realiza una búsqueda por saltos en el arreglo arr para encontrar el valor x.
7. medir_tiempo(algoritmo, arr, x): Mide y retorna el tiempo de ejecución de un algoritmo de búsqueda.
8. analizar(nombre_archivo, size): Ejecuta los algoritmos de búsqueda sobre el arreglo cargado desde el archivo y mide el tiempo de ejecución.

Requisitos:
- Python 3.11.0
- Biblioteca matplotlib para la visualización de resultados.

Uso:
El programa generará automáticamente archivos de texto con números aleatorios y luego ejecutará los algoritmos
de búsqueda, mostrando los resultados en la consola y graficando los tiempos de ejecución en subgráficas.
"""

import random
import time
import matplotlib.pyplot as plt
import math

# Función para generar un archivo de texto plano con números aleatorios de 8 dígitos
def generar_archivo_texto(nombre_archivo, size):
    with open(nombre_archivo, 'w') as archivo:
        for _ in range(size):
            archivo.write(str(random.randint(10000000, 99999999)) + '\n')

# Función para cargar los datos desde un archivo de texto plano
def cargar_arreglo_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return [int(linea.strip()) for linea in archivo.readlines()]

# Búsqueda Lineal
def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Búsqueda Lineal Limitada (solo hasta un número de elementos especificado)
def busqueda_lineal_limitada(arr, x, limite):
    for i in range(min(len(arr), limite)):
        if arr[i] == x:
            return i
    return -1

# Búsqueda Binaria (requiere que el arreglo esté ordenado)
def busqueda_binaria(arr, x):
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == x:
            return medio
        elif arr[medio] < x:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Búsqueda por Saltos (Jump Search)
def busqueda_por_saltos(arr, x):
    n = len(arr)
    paso = int(math.sqrt(n))
    prev = 0
    while arr[min(paso, n)-1] < x:
        prev = paso
        paso += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(paso, n)):
        if arr[i] == x:
            return i
    return -1

# Función para medir tiempo de ejecución de un algoritmo de búsqueda
def medir_tiempo(algoritmo, arr, x):
    inicio = time.time()
    algoritmo(arr, x)
    fin = time.time()
    return (fin - inicio) * 1000  # Tiempo en milisegundos

# Función para ejecutar los algoritmos y graficar los resultados
def analizar(nombre_archivo, size):
    resultados = {
        'Lineal': [],
        'Lineal Limitada': [],
        'Binaria': [],
        'Por Saltos': []
    }

    # Cargar el arreglo desde el archivo
    arreglo = sorted(cargar_arreglo_desde_archivo(nombre_archivo))  # Ordenamos para la búsqueda binaria
    elemento_a_buscar = arreglo[random.randint(0, len(arreglo) - 1)]  # Tomamos un elemento aleatorio del arreglo

    # Medir el tiempo de ejecución de cada algoritmo y registrar resultados
    resultados['Lineal'].append(medir_tiempo(busqueda_lineal, arreglo, elemento_a_buscar))
    resultados['Lineal Limitada'].append(medir_tiempo(lambda arr, x: busqueda_lineal_limitada(arr, x, 5000), 
                                                      arreglo, elemento_a_buscar))  # Limitado a 5000 elementos
    resultados['Binaria'].append(medir_tiempo(busqueda_binaria, arreglo, elemento_a_buscar))
    resultados['Por Saltos'].append(medir_tiempo(busqueda_por_saltos, arreglo, elemento_a_buscar))

    return resultados

# Tamaños de los arreglos y nombres de los archivos
size_arrays = [10000, 100000, 1000000]
nombres_archivos = ['datos_10000.txt', 'datos_100000.txt', 'datos_1000000.txt']

# Generar los archivos de texto con números aleatorios
for size, nombre_archivo in zip(size_arrays, nombres_archivos):
    generar_archivo_texto(nombre_archivo, size)

# Inicializar listas para los tiempos de ejecución de cada algoritmo
tiempos_totales = {
    'Lineal': [],
    'Lineal Limitada': [],
    'Binaria': [],
    'Por Saltos': []
}

# Ejecutar el análisis para cada archivo
for size, nombre_archivo in zip(size_arrays, nombres_archivos):
    resultados = analizar(nombre_archivo, size)
    
    # Acumular los resultados por algoritmo y mostrar en consola
    print(f"\nResultados para {size} elementos:")
    for algoritmo, tiempo in resultados.items():
        print(f"{algoritmo}: {tiempo[0]:.2f} ms")  # Solo tomamos el primer (y único) tiempo
        tiempos_totales[algoritmo].append(tiempo[0])  # Solo tomamos el primer (y único) tiempo

# Graficar los resultados en subgráficas
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Crear gráficas para cada tamaño de arreglo
for idx, size in enumerate(size_arrays):
    metodos = list(tiempos_totales.keys())
    tiempos = [tiempos_totales[metodo][idx] for metodo in metodos]
    
    axs[idx].bar(metodos, tiempos, color=['red', 'blue', 'green', 'purple'])
    axs[idx].set_title(f'Tiempos de Ejecución ({size} elementos)')
    axs[idx].set_xlabel('Algoritmo de Búsqueda')
    axs[idx].set_ylabel('Tiempo de Ejecución (ms)')
    axs[idx].grid(axis='y')

plt.tight_layout()
plt.show()