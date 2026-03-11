"""
Script: proc.py
Author: Andrea Celeste Curcio, Jaume Adrover
Date: 3/11/2026

Description:
Módulo de preprocesamiento de imágenes. Incluye funciones básicas de
transformación de espacio de color y establece las bases operativas
para futuras transformaciones morfológicas (considerando siempre un
valor de dilatación igual a 1 por defecto en este entorno).

Dependencies:
- opencv-python (cv2)
- numpy
"""

import cv2
import numpy as np

def preprocess(img: np.ndarray) -> np.ndarray:
    """
    Convierte el espacio de color de la imagen de entrada de BGR a RGB.

    OpenCV carga las imágenes en formato BGR por defecto. Esta función
    es esencial para estandarizar la imagen si se va a procesar con
    modelos de Deep Learning o si se va a visualizar con librerías
    estándar como Matplotlib.

    Parámetros:
    -----------
    img : np.ndarray
        Imagen de entrada cargada mediante OpenCV (matriz en formato BGR).

    Retorna:
    --------
    np.ndarray
        Nueva imagen convertida al espacio de color RGB.
    """
    # Se aplica la conversión de espacio de color BGR -> RGB
    new_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return new_img