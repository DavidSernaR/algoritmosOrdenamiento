import matplotlib.pyplot as plt
import numpy as np

def mostrar_grafica(tiempos, algoritmo):
    # Tamaños de los arreglos para el eje X
    archivos = ["10.000", "100.000", "1.000.000"]
    
    # Crear la gráfica de barras
    fig, ax = plt.subplots()
    y_pos = np.arange(len(archivos))
    
    # Dibujar las barras
    bars = ax.bar(y_pos, tiempos, align='center', alpha=0.7, color='b')
    
    # Añadir los nombres de los arreglos en el eje X
    ax.set_xticks(y_pos)
    ax.set_xticklabels(archivos)
    ax.set_ylabel('Tiempo (segundos)')
    ax.set_title(f'Tiempo de ejecución: {algoritmo}')
    
    # Añadir etiquetas de tiempo justo encima de cada barra
    for bar, tiempo in zip(bars, tiempos):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, height, f'{tiempo:.4f}s', ha='center', va='bottom', fontsize=10, color='black')

    # Mostrar la gráfica
    plt.show()
