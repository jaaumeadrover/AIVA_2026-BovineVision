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
import os
import cv2
import numpy as np
from typing import Optional


def load_image(filename: str) -> Optional[np.ndarray]:
    """
    Carga una imagen desde el disco en memoria con validaciones.

    Parámetros:
    -----------
    filename : str
        Ruta del archivo de imagen.

    Retorna:
    --------
    Optional[np.ndarray]
        Matriz numpy (BGR) o None si falla.
    """
    # 1. Check if the file actually exists on disk
    if not os.path.exists(filename):
        print(f"Error: El archivo no existe en la ruta: {filename}")
        return None

    try:
        # 2. Attempt to read the image
        img = cv2.imread(filename)

        # Check if OpenCV successfully decoded the image
        if img is None:
            print(f"Error: No se pudo decodificar la imagen en {filename}. El archivo podría estar corrupto.")
            return None

        return img

    except Exception as e:
        # Catch unexpected errors (e.g., permission issues, system errors)
        print(f"Ocurrió un error inesperado al cargar la imagen: {e}")
        return None