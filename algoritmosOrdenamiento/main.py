import tkinter as tk
from tkinter import messagebox
from archivos import crear_archivo
from medicion import medir_tiempo
from graficas import mostrar_grafica
import time  # Importar para medir el tiempo total

# Crear los archivos de números aleatorios (solo si no existen)
crear_archivo("Arreglo 10.000", 10000)
crear_archivo("Arreglo 100.000", 100000)
crear_archivo("Arreglo 1.000.000", 1000000)

# Función para seleccionar y ejecutar el algoritmo
def seleccionar_algoritmo(algoritmo):
    start_total_time = time.time()  # Tiempo de inicio

    tiempos = [
        medir_tiempo(algoritmo, "Arreglo 10.000"),
        medir_tiempo(algoritmo, "Arreglo 100.000"),
        medir_tiempo(algoritmo, "Arreglo 1.000.000")
    ]

    end_total_time = time.time()  # Tiempo de fin
    total_time = end_total_time - start_total_time

    # Mostrar gráfica
    mostrar_grafica(tiempos, algoritmo)

    # Mostrar en consola el tiempo total de ejecución
    print(f"El algoritmo {algoritmo} tardó {total_time:.4f} segundos en ejecutar los 3 archivos.")

# Interfaz gráfica mejorada
root = tk.Tk()
root.title("Selecciona un Algoritmo de Ordenamiento")

label = tk.Label(root, text="Selecciona un algoritmo de ordenamiento:", font=("Helvetica", 14))
label.pack(pady=10)

# Crear botones para cada algoritmo
boton_burbuja = tk.Button(root, text="Burbuja", width=20, command=lambda: seleccionar_algoritmo("burbuja"))
boton_burbuja.pack(pady=5)

boton_quicksort = tk.Button(root, text="Quicksort", width=20, command=lambda: seleccionar_algoritmo("quicksort"))
boton_quicksort.pack(pady=5)

boton_stooge = tk.Button(root, text="Stooge Sort", width=20, command=lambda: seleccionar_algoritmo("stooge"))
boton_stooge.pack(pady=5)

boton_pigeonhole = tk.Button(root, text="Pigeonhole Sort", width=20, command=lambda: seleccionar_algoritmo("pigeonhole"))
boton_pigeonhole.pack(pady=5)

boton_merge = tk.Button(root, text="Merge Sort", width=20, command=lambda: seleccionar_algoritmo("merge"))
boton_merge.pack(pady=5)

boton_bitonic = tk.Button(root, text="Bitonic Sort", width=20, command=lambda: seleccionar_algoritmo("bitonic"))
boton_bitonic.pack(pady=5)

root.mainloop()
