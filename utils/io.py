"""
Script: io.py
Author: Andrea Celeste Curcio, Jaume Adrover
Date: 3/11/2026

Description:
Módulo de entrada/salida (I/O). Gestiona todas las operaciones de
lectura y escritura de archivos necesarias para el proyecto,
asegurando una carga de datos robusta.

Dependencies:
- opencv-python (cv2)
- numpy
"""

import cv2
import numpy as np
from typing import Optional

def load_image(filename: str) -> Optional[np.ndarray]:
    """
    Carga una imagen desde el disco en memoria.

    Utiliza OpenCV para leer el archivo desde la ruta especificada.
    Es importante notar que OpenCV carga las imágenes en formato BGR
    y que, si el archivo no existe o está corrupto, no lanzará un error,
    sino que devolverá un objeto vacío (None).

    Parámetros:
    -----------
    file : str
        Ruta (absoluta o relativa) del archivo de imagen que se desea cargar.

    Retorna:
    --------
    Optional[np.ndarray]
        Matriz numpy que representa la imagen cargada (en BGR).
        Devuelve None si la imagen no pudo ser leída.
    """

    # Carga la imagen utilizando OpenCV
    img = cv2.imread(filename)

    return img