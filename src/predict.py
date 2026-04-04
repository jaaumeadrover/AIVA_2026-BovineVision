"""
Script: predict.py
Author: Andrea Celeste Curcio, Jaume Adrover
Date: 4/4/2026

Description:
Pipeline principal para la inferencia de OCR en crotales.
Permite procesar una imagen individual o un directorio completo,
aplicando preprocesamiento ETR-6 y generando reportes de salida.

Usage:
python predict.py --img data/0299.TIF --out result.txt
python predict.py --dir data/TestSamples --eval results_batch.csv

Dependencies:
- argparse
- cv2
- easyocr
- numpy
"""

import argparse
import ocr
import os

def main():
    parser = argparse.ArgumentParser(
        description="ETR OCR Prediction Pipeline",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter # Muestra valores por defecto en --help
    )

    # Grupo de Entrada (Mutuamente excluyentes si quieres forzar uno u otro)
    input_group = parser.add_argument_group('Input Options')
    input_group.add_argument('--img', type=str, help='Ruta a una sola imagen para procesar')
    input_group.add_argument('--dir', type=str, default='../data/TestSamples', help='Directorio de imágenes para procesamiento por lotes')

    # Grupo de Salida
    output_group = parser.add_argument_group('Output Options')
    output_group.add_argument('--out', type=str, default='output.txt', help='Archivo TXT para guardar el resultado de una sola imagen')
    output_group.add_argument('--eval', type=str, default='ocr_results.csv', help='Ruta del CSV para los resultados del modo batch')

    args = parser.parse_args()

    # Lógica de ejecución basada en los argumentos
    print(f"--- Iniciando predict.py ---")

    if args.img:
        if not os.path.exists(args.img):
            print(f"Error: No se encuentra la imagen {args.img}")
            return
        print(f"Modo: Imagen individual -> {args.img}")

        # Single
        ocr.run_single_ocr(args.img, args.out)

    elif args.dir:
        if not os.path.isdir(args.dir):
            print(f"Error: El directorio {args.dir} no existe")
            return
        print(f"Modo: Batch processing en -> {args.dir}")
        print(f"Resultados se guardarán en: {args.eval}")

        # Batch logic
        ocr.run_batch_ocr(input_dir=args.dir, output_csv=args.eval)

if __name__ == "__main__":
    main()