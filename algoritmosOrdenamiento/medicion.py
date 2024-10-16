import time
from archivos import cargar_archivo
from algoritmos import burbuja, quicksort, stooge_sort, pigeonhole_sort, merge_sort, bitonic_sort

def medir_tiempo(algoritmo, nombre_archivo):
    arr = cargar_archivo(nombre_archivo)
    start_time = time.time()
    if algoritmo == "burbuja":
        burbuja(arr)
    elif algoritmo == "quicksort":
        arr = quicksort(arr)
    elif algoritmo == "stooge":
        stooge_sort(arr, 0, len(arr)-1)
    elif algoritmo == "pigeonhole":
        pigeonhole_sort(arr)
    elif algoritmo == "merge":
        merge_sort(arr)
    elif algoritmo == "bitonic":
        bitonic_sort(arr, 0, len(arr), 1)
    end_time = time.time()
    return end_time - start_time
