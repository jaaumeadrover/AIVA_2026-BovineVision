"""
Script: score.py
Author: Andrea Celeste Curcio, Jaume Adrover
Date: 4/2/2026

Description:
Módulo de evaluación de precisión para el sistema OCR ETR-6.
Compara las predicciones generadas contra el Ground Truth,
calcula la tasa de acierto (accuracy) y genera un reporte
detallado de las detecciones fallidas para análisis de errores.

Usage:
python score.py

Dependencies:
- pandas
- numpy
"""

import pandas as pd

def main():
    # Main logic
    gt = pd.read_csv('../data/GroundTruth.csv')
    pred = pd.read_csv('ocr_results.csv')

    result = pd.concat([gt, pred], axis=1)
    result['Real'] = result['Real'].astype(str).str.strip()
    result['result'] = result['result'].astype(str).str.strip()

    print(result['result'])
    result['is_correct'] = result.apply(
        lambda row: str(row['Real']) in str(row['result'])
        if pd.notna(row['result']) and str(row['result']).lower() != 'nan'
        else False,
        axis=1
    )

    # 4. Calculate Metrics
    total = len(result)
    correct = result['is_correct'].sum()
    accuracy = (correct / total) * 100

    incorrect_preds = result[result['is_correct'] == False]

    if not incorrect_preds.empty:
        print("\n--- Incorrect Predictions (Failures) ---")
        # Showing filename, ground truth, and what the OCR actually saw
        print(incorrect_preds[['filename', 'Real', 'result']])
        print(f"\nTotal Failures: {len(incorrect_preds)}")
    else:
        print("\nPerfect Score! No incorrect predictions found.")

    print("-" * 30)
    print(f"Total Images: {total}")
    print(f"Correct:      {correct}")
    print(f"Accuracy:     {accuracy:.2f}%")
    print("-" * 30)


if __name__ == "__main__":
    main()
