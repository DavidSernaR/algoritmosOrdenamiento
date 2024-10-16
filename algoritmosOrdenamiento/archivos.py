import os
import random

directorio = "Archivos"

# Verifica si existe la carpeta "Archivos", si no, la crea
if not os.path.exists(directorio):
    os.makedirs(directorio)

def crear_archivo(nombre_archivo, cantidad_numeros):
    ruta = os.path.join(directorio, nombre_archivo + ".txt")
    
    if not os.path.exists(ruta):
        with open(ruta, "w") as archivo:
            numeros = [str(random.randint(10000000, 99999999)) for _ in range(cantidad_numeros)]
            archivo.write("\n".join(numeros))
        print(f"Archivo {nombre_archivo} creado con {cantidad_numeros} números.")
    else:
        print(f"El archivo {nombre_archivo} ya existe.")

def cargar_archivo(nombre_archivo):
    ruta = os.path.join(directorio, nombre_archivo + ".txt")
    with open(ruta, "r") as archivo:
        return list(map(int, archivo.readlines()))
