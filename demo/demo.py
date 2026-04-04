"""
Script: demo.py
Author: Andrea Celeste Curcio, Jaume Adrover
Date: 4/4/2026

Description:
Demostración visual utilizando Matplotlib.
Muestra el preprocesado y la detección de OCR.
"""

import argparse
import cv2
import os
import matplotlib.pyplot as plt
from utils import proc
from src import ocr

def main():
    parser = argparse.ArgumentParser(description="Demo visual de OCR con Matplotlib")
    parser.add_argument('--img', type=str, default='../data/TestSamples/0001.TIF', help='Ruta de la imagen')
    args = parser.parse_args()

    print(f"--- Iniciando Demo Matplotlib ---")

    # 1. Obtener Lector e Imagen
    reader = ocr.get_reader(gpu=False)
    original, processed = proc.preprocess_etr_pipeline(args.img)

    if original is None:
        print("Error: No se pudo cargar la imagen.")
        return

    # 2. Inferencia OCR
    results = reader.readtext(processed, detail=1, allowlist='0123456789')

    # 3. Convertir BGR a RGB para Matplotlib
    display_img = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

    # 4. Configurar Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    # Lado Izquierdo: Imagen Procesada (Binary/Otsu)
    ax1.imshow(processed, cmap='gray')
    ax1.set_title("1. Preprocesado ETR-6 (Otsu)")
    ax1.axis('off')

    # Lado Derecho: Imagen Original con Bounding Boxes
    ax2.imshow(display_img)
    ax2.set_title(f"2. Detección Original: {os.path.basename(args.img)}")

    if results:
        for (bbox, text, prob) in results:
            # bbox: [[tl_x, tl_y], [tr_x, tr_y], [br_x, br_y], [bl_x, bl_y]]
            tl = bbox[0]
            br = bbox[2]

            # Crear rectángulo en Matplotlib
            rect = plt.Rectangle((tl[0], tl[1]), br[0]-tl[0], br[1]-tl[1],
                                 fill=False, edgecolor='lime', linewidth=2)
            ax2.add_patch(rect)
            ax2.text(tl[0], tl[1] - 10, f"{text} ({prob:.2f})",
                     bbox=dict(facecolor='lime', alpha=0.5), fontsize=10, color='white')

            print(f"Detectado: {text} ({prob:.4f})")

    ax2.axis('off')

    plt.tight_layout()
    print("\nCerrar la ventana del gráfico para finalizar el script.")
    plt.show()

if __name__ == "__main__":
    main()