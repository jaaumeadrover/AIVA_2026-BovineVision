"""
Script: batch.py
Author: Andrea Celeste Curcio, Jaume Adrover
Date: 4/4/2026

Description:
Módulo de procesamiento por lotes para OCR. Expone una función ejecutable
para procesar directorios completos y generar reportes CSV.

Dependencies:
- opencv-python (cv2)
- easyocr
- numpy
"""
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import csv
import glob
import time
import easyocr
from utils import proc

def run_batch_ocr(input_dir: str, output_csv: str, gpu: bool = False, lang: str = 'es'):
    """
    Ejecuta el pipeline de OCR sobre todos los archivos de un directorio.

    Args:
        input_dir (str): Ruta al directorio con las imágenes.
        output_csv (str): Ruta del archivo CSV de salida.
        gpu (bool): Uso de aceleración por hardware.
        lang (str): Idioma para EasyOCR.
    """
    # Inicializar el lector con los parámetros recibidos
    reader = easyocr.Reader([lang], gpu=gpu)

    # Soportar múltiples extensiones comunes
    extensions = ['*.TIF', '*.jpg', '*.jpeg', '*.png']
    image_files = []
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(input_dir, ext)))

    if not image_files:
        print(f"No se encontraron imágenes en {input_dir}")
        return

    print(f"--- Iniciando Procesamiento Batch ETR ({len(image_files)} archivos) ---")

    results_data = []

    for image_path in image_files:
        filename = os.path.basename(image_path)
        start_time = time.time()

        # Llamada al módulo de preprocesado ETR-6
        original, processed = proc.preprocess_etr_pipeline(image_path)

        if processed is not None:
            # Ejecutar OCR con whitelist numérica
            text_list = reader.readtext(processed, detail=0, allowlist='0123456789')

            # Selección del último elemento (Heurística de posición inferior)
            detected_text = text_list[-1] if len(text_list) > 0 else ""

            elapsed = time.time() - start_time
            print(f"Procesado: {filename} -> {detected_text} ({elapsed:.2f}s)")

            results_data.append({
                'filename': filename,
                'result': detected_text,
                'time_seconds': round(elapsed, 3)
            })
        else:
            print(f"Error al cargar/procesar: {filename}")
            results_data.append({
                'filename': filename,
                'result': 'ERROR_LOADING',
                'time_seconds': 0
            })

    # Guardar resultados en CSV
    keys = ['filename', 'result', 'time_seconds']
    try:
        # Asegurar que el directorio de salida existe
        output_dir = os.path.dirname(output_csv)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(output_csv, 'w', newline='', encoding='utf-8') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(results_data)
        print(f"\n--- Proceso completado. Resultados guardados en: {output_csv} ---")
    except Exception as e:
        print(f"Error al guardar el CSV: {e}")

