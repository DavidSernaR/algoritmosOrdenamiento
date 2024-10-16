# Algoritmos de Ordenamiento y Medición de Rendimiento

Este proyecto implementa varios algoritmos de ordenamiento y mide su rendimiento en grandes conjuntos de datos de números generados aleatoriamente. Además, ofrece una interfaz gráfica (GUI) para seleccionar los algoritmos y visualizar los tiempos de ejecución. El código también incluye un módulo separado para algoritmos de búsqueda, con medición de tiempo y representación gráfica de los resultados.

## Tabla de Contenidos
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Características](#características)
- [Requisitos](#requisitos)
- [Uso](#uso)
- [Algoritmos de Ordenamiento](#algoritmos-de-ordenamiento)
- [Algoritmos de Búsqueda](#algoritmos-de-búsqueda)
- [Visualización del Rendimiento](#visualización-del-rendimiento)

## Estructura del Proyecto

- **main.py**: Archivo principal de la aplicación, que incluye la GUI para seleccionar un algoritmo de ordenamiento y visualizar el rendimiento.
- **algoritmos.py**: Contiene la implementación de varios algoritmos de ordenamiento.
- **archivos.py**: Gestiona la creación y carga de archivos con números generados aleatoriamente.
- **medicion.py**: Mide el tiempo de ejecución de los algoritmos de ordenamiento seleccionados.
- **graficas.py**: Genera representaciones gráficas de los tiempos de ejecución de los algoritmos.
- **algoritmosBusqueda.py**: Implementa varios algoritmos de búsqueda, mide su rendimiento y muestra los resultados de forma gráfica (incluido por separado).

## Características

- **GUI para Ordenamiento**: Los usuarios pueden seleccionar algoritmos de ordenamiento desde una interfaz gráfica construida con `tkinter`, y la aplicación medirá el tiempo necesario para ordenar arreglos de distintos tamaños.
- **Gestión de Archivos**: El programa crea automáticamente archivos con arreglos de números aleatorios de 8 dígitos, que se utilizan para los algoritmos de ordenamiento.
- **Medición de Rendimiento**: Mide el tiempo de ejecución de los algoritmos de ordenamiento y búsqueda, mostrando los resultados en gráficos.
- **Algoritmos de Búsqueda**: Implementa algoritmos comunes de búsqueda como búsqueda lineal, binaria y por saltos, con medición del tiempo de ejecución.

## Requisitos

- Python 3.11+
- Bibliotecas necesarias:
  - `matplotlib` para la generación de gráficos
  - `numpy` para operaciones numéricas
  - `tkinter` para la interfaz gráfica

Instalar dependencias con pip:

```bash
pip install matplotlib numpy
```

## Uso

**1. Ejecutar la GUI de Ordenamiento:**

   - Ejecuta el archivo `main.py` para iniciar la GUI.
   - Selecciona un algoritmo de ordenamiento, y el programa ordenará tres conjuntos de datos de 10.000, 100.000 y 1.000.000 números aleatorios.
   - Se mostrará un gráfico con el tiempo de ejecución y se imprimirá el tiempo total en la consola.

**2. Algoritmos de Búsqueda:**

  - El archivo `algoritmosBusqueda.py` contiene los algoritmos de búsqueda.
  - Genera arreglos aleatorios, busca un elemento objetivo utilizando diferentes algoritmos y muestra los tiempos en la consola, además de una representación gráfica.

## Algoritmos de Ordenamiento

Los siguientes algoritmos de ordenamiento están implementados en `algoritmos.py`:

  - **Ordenamiento Burbuja (`burbuja`):** Algoritmo de ordenamiento simple con complejidad O(n^2).
  - **Quicksort (`quicksort`):** Algoritmo eficiente de ordenamiento con complejidad O(n log n).
  - **Stooge Sort (`stooge_sort`):** Algoritmo menos común con complejidad O(n^2.7).
  - **Pigeonhole Sort (`pigeonhole_sort`):** Algoritmo adecuado para rangos específicos de valores de entrada.
  - **Merge Sort (`merge_sort`):** Algoritmo eficiente y estable con complejidad O(n log n).
  - **Bitonic Sort (`bitonic_sort`):** Algoritmo paralelo de ordenamiento.

## Algoritmos de Búsqueda

Los algoritmos de búsqueda implementados en `algoritmosBusqueda.py` incluyen:

- **Búsqueda Lineal:** Busca elemento por elemento.
- **Búsqueda Lineal Limitada:** Búsqueda lineal limitada a un número específico de elementos.
- **Búsqueda Binaria:** Búsqueda en un arreglo ordenado utilizando un enfoque de divide y vencerás.
- **Búsqueda por Saltos:** Busca utilizando pasos fijos, seguidos de una búsqueda lineal en el bloque.

## Visualización del Rendimiento

El programa genera representaciones gráficas del tiempo que toma cada algoritmo para procesar arreglos de distintos tamaños. Los gráficos muestran el tiempo de ejecución en segundos para facilitar la comparación entre algoritmos.

Los tiempos de ordenamiento se muestran para conjuntos de datos de:

- 10.000 elementos
- 100.000 elementos
- 1.000.000 elementos

Los tiempos de búsqueda se visualizan en milisegundos.
