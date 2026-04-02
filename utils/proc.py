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
from typing import Optional


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


def preprocess_image_array(img: np.ndarray) -> Optional[np.ndarray]:
    """
    Procesa una matriz de imagen (NumPy array) para mejorar la legibilidad de OCR.

    Pasos:
    1. Validación de entrada.
    2. Escala de grises.
    3. Mejora de contraste (CLAHE).
    4. Reducción de ruido.
    5. Binarización (Otsu).

    Parámetros:
    -----------
    img : np.ndarray
        Imagen original cargada (preferiblemente en formato BGR).

    Retorna:
    --------
    Optional[np.ndarray]
        Imagen binaria procesada, o None si la entrada no es válida.
    """

    # 1. Validación de la entrada
    if img is None or not isinstance(img, np.ndarray):
        print("Error: La entrada no es una matriz de imagen válida.")
        return None

    try:
        # 2. Convertir a escala de grises
        # Verificamos si ya es gris (2 dimensiones) o color (3 dimensiones)
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # 3. Mejorar contraste (CLAHE)
        # Ideal para compensar sombras en los crotales
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        contrast_enhanced = clahe.apply(gray)

        # 4. Filtrado para reducir ruido
        # El desenfoque ayuda a suavizar imperfecciones antes de binarizar
        blurred = cv2.GaussianBlur(contrast_enhanced, (5, 5), 0)

        # 5. Binarización (Umbral de Otsu)
        # Esto convierte la imagen a blanco y negro puro (0 y 255)
        _, binary = cv2.threshold(
            blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        return binary

    except Exception as e:
        print(f"Error durante el preprocesado: {e}")
        return None