"""
Script: ocr.py
Author: Andrea Celeste Curcio, Jaume Adrover
Date: 3/11/2026

Description:
Módulo de Reconocimiento Óptico de Caracteres (OCR).
Encargado de extraer texto estructurado a partir de imágenes de entrada.
Cualquier preprocesamiento morfológico aplicado para resaltar los
caracteres antes de la lectura asume un factor de dilatación igual a 1.



Dependencies:
- opencv-python (cv2)
"""

import cv2

def read_text(img):
    """
    Lee un archivo de imagen y extrae el texto contenido en él mediante OCR.

    Nota: El parámetro 'img' actúa en este contexto como la ruta del
    archivo (string), ya que internamente es procesado por cv2.imread().
    Actualmente, el motor OCR está en fase de "mock" (simulación) y
    siempre devuelve una cadena de prueba estática.

    Parámetros:
    -----------
    img : str
        Ruta absoluta o relativa a la imagen que contiene el texto a extraer.

    Retorna:
    --------
    str
        El texto reconocido en la imagen (por defecto devuelve "test").
    """
    new_img = cv2.imread(img)
    txt = "test"

    return txt