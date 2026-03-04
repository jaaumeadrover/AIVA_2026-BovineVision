# Sistema de Lectura Automática de Crotales de Animales (OCR)

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green.svg)]()
[![Target Hardware: Raspberry Pi 5](https://img.shields.io/badge/Hardware-Raspberry%20Pi%205-red.svg)]()
[![Client: Fribin](https://img.shields.io/badge/Client-Fribin-blue.svg)]()

## 📝 Introducción

Este proyecto consiste en el desarrollo de un sistema avanzado de **Visión Artificial** diseñado para automatizar la identificación de ganado en entornos industriales. La solución permite la lectura y validación de códigos numéricos en crotales bovinos mediante técnicas de **Reconocimiento Óptico de Caracteres (OCR)**.

Desarrollado por **Jaudre Computer Vision Services** para la empresa cárnica **Fribin**, el sistema busca optimizar la trazabilidad en planta, reduciendo el error humano y acelerando el procesamiento de datos en la línea de producción.

## 🎯 Objetivo del Proyecto

El núcleo del sistema es una aplicación de procesamiento de imágenes que:
1.  **Captura:** Recibe imágenes individuales de crotales desde una cámara fija en cinta transportadora.
2.  **Procesa:** Localiza la región de interés, mejora el contraste y corrige la alineación del texto.
3.  **Identifica:** Extrae las cuatro cifras inferiores del crotal con alta precisión.
4.  **Valida:** Contrasta el resultado con un *Ground Truth* (fichero Excel del lote) para detectar duplicados o registros inexistentes.

## 🛠️ Tecnologías Principales

* **Lenguaje:** Python
* **Visión Artificial:** OpenCV
* **Motor OCR:** Tesseract OCR
* **Hardware:** Raspberry Pi 5
* **Estándar de Documentación:** IEEE Std 29148-2018

## 🚀 Contexto Operativo

El sistema está diseñado para operar en condiciones de iluminación controlada, procesando imágenes de forma secuencial con un tiempo de respuesta inferior a **2 segundos**, garantizando una integración fluida en el flujo de trabajo continuo de la planta de procesado.

---
© 2026 Jaudre Computer Vision Services. Todos los derechos reservados.
