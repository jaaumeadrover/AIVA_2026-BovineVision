"""
Script: ocr.py
Author: Andrea Celeste Curcio, Jaume Adrover
Date: 4/4/2026

Description:
Módulo unificado para el motor OCR. Proporciona capacidades de procesamiento
tanto individual como por lotes (batch), optimizando la carga de modelos.

Dependencies:
- opencv-python (cv2)
- easyocr
- numpy
"""
import os

from utils.validator import validate_against_dataset, detect_duplicates

# Workaround for OpenMP duplicate initialization on Windows/Conda
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import csv
import glob
import time
import easyocr
from utils import proc

# Global variable to hold the reader instance (lazy loading)
_READER_INSTANCE = None

def get_reader(gpu=False, lang='es'):
    """
    Singleton para obtener la instancia de EasyOCR.
    Evita recargar los modelos en cada llamada.
    """
    global _READER_INSTANCE
    if _READER_INSTANCE is None:
        print("--- Inicializando EasyOCR Engine (Cargando modelos...) ---")
        _READER_INSTANCE = easyocr.Reader([lang], gpu=gpu)
    return _READER_INSTANCE

def run_single_ocr(image_path: str, output_txt: str = None, gpu: bool = False, lang: str = 'es', dataset=None):
    """Procesa una única imagen y extrae el identificador."""
    start_time = time.time()

    reader = get_reader(gpu=gpu, lang=lang)

    print(f"--- Procesando imagen: {os.path.basename(image_path)} ---")
    original, processed = proc.preprocess_etr_pipeline(image_path)

    if processed is None:
        return None

    text_list = reader.readtext(processed, detail=0, allowlist='0123456789')
    detected_text = text_list[-1] if len(text_list) > 0 else "NO_DETECTION"

    is_valid = None # Inicialización para consistencia (uso futuro / debug)
    # Validación (solo si hay un dataset)
    if dataset is not None:
        is_valid = validate_against_dataset(detected_text, dataset)

        if not is_valid:
            print(f"[WARNING] Código no válido: {detected_text}")

    elapsed = time.time() - start_time
    print(f"Resultado: {detected_text} ({elapsed:.2f}s)")

    if output_txt:
        with open(output_txt, 'w', encoding='utf-8') as f:
            f.write(detected_text)

    return detected_text

def run_batch_ocr(input_dir: str, output_csv: str, gpu: bool = False, lang: str = 'es', dataset=None):
    """Ejecuta el pipeline de OCR sobre un directorio completo."""
    reader = get_reader(gpu=gpu, lang=lang)

    extensions = ['*.TIF', '*.jpg', '*.jpeg', '*.png']
    image_files = []
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(input_dir, ext)))

    if not image_files:
        print(f"No se encontraron imágenes en {input_dir}")
        return

    print(f"--- Iniciando Batch ({len(image_files)} archivos) ---")
    results_data = []

    for image_path in image_files:
        filename = os.path.basename(image_path)
        start_time = time.time()

        _, processed = proc.preprocess_etr_pipeline(image_path)

        if processed is not None:
            text_list = reader.readtext(processed, detail=0, allowlist='0123456789')
            detected_text = text_list[-1] if len(text_list) > 0 else ""

            is_valid = None

            # Validación (solo si hay un dataset)
            if dataset is not None:
                is_valid = validate_against_dataset(detected_text, dataset)

                if not is_valid:
                    print(f"[WARNING] Código no válido: {detected_text}")

            elapsed = time.time() - start_time

            print(f"Procesado: {filename} -> {detected_text}")
            results_data.append({'filename': filename, 'result': detected_text,
                                 'valid': is_valid, 'time_seconds': round(elapsed, 3)})
        else:
            results_data.append({'filename': filename, 'result': 'ERROR_LOADING',
                                 'valid': None, 'time_seconds': 0})

    results = [r['result'] for r in results_data if r['result'] and r['result'] != 'ERROR_LOADING']
    duplicates = detect_duplicates(results)

    if duplicates:
        print(f"[WARNING] Duplicados detectados: {duplicates}")

    # Guardar CSV
    keys = ['filename', 'result', 'valid', 'time_seconds']
    output_dir = os.path.dirname(output_csv)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(results_data)

    print(f"\n--- Batch completado. Reporte: {output_csv} ---")
