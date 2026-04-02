import cv2
import easyocr
import numpy as np
import time
import os
import glob
import csv
from typing import Optional, Tuple

def preprocess_image(image_path: str) -> Tuple[Optional[np.ndarray], Optional[np.ndarray]]:
    """
    Aplica el pre-procesamiento siguiendo la metodología ETR.
    """
    if not os.path.exists(image_path):
        return None, None

    img = cv2.imread(image_path)
    if img is None:
        return None, None

    # 1. Conversión a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. Umbralizado de Otsu
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 3. REGLA DE ORO: Dilatación con kernel de 1x1 (Basado en requerimiento previo)
    kernel = np.ones((1, 1), np.uint8)
    processed_img = cv2.dilate(thresh, kernel, iterations=1)

    return img, processed_img

def run_batch_ocr():
    # Inicializar el lector
    reader = easyocr.Reader(['es'], gpu=False)
    
    # Configuración de rutas
    input_dir = '../data/TestSamples'
    output_csv = 'ocr_results_21.csv'
    
    # Soportar múltiples extensiones comunes
    extensions = ['*.TIF', '*.jpg', '*.jpeg', '*.png']
    image_files = []
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(input_dir, ext)))

    if not image_files:
        print(f"No se encontraron imágenes en {input_dir}")
        return

    print(f"--- Iniciando Procesamiento Batch ETR-3 ({len(image_files)} archivos) ---")
    
    results_data = []

    for image_path in image_files:
        filename = os.path.basename(image_path)
        start_time = time.time()

        original, processed = preprocess_image(image_path)

        if processed is not None:
            # Ejecutar OCR. Usamos 'processed' para aprovechar el umbralizado
            # allowlist asegura que solo busque números de crotal
            text_list = reader.readtext(processed, detail=0, allowlist='0123456789')

            if len(text_list)>0:
                detected_text = text_list[-1]
            else:
                detected_text=""
            elapsed = time.time() - start_time
            print(f"Procesado: {filename} -> {detected_text} ({elapsed:.2f}s)")
            
            results_data.append({
                'filename': filename,
                'result': detected_text,
                'time_seconds': round(elapsed, 3)
            })
        else:
            print(f"Error al cargar: {filename}")
            results_data.append({
                'filename': filename,
                'result': 'ERROR_LOADING',
                'time_seconds': 0
            })

    # Guardar resultados en CSV
    keys = ['filename', 'result', 'time_seconds']
    try:
        with open(output_csv, 'w', newline='', encoding='utf-8') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(results_data)
        print(f"\n--- Proceso completado. Resultados guardados en: {output_csv} ---")
    except Exception as e:
        print(f"Error al guardar el CSV: {e}")

if __name__ == "__main__":
    run_batch_ocr()