# Sistema de Lectura Automática de Crotales de Animales (OCR)

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-green.svg)]()
[![Target Hardware: Raspberry Pi 5](https://img.shields.io/badge/Hardware-Raspberry%20Pi%205-red.svg)]()
[![Client: Fribin](https://img.shields.io/badge/Client-Fribin-blue.svg)]()

## Introducción

Este proyecto consiste en el desarrollo de un sistema avanzado de **Visión Artificial** diseñado para automatizar la identificación de ganado en entornos industriales. La solución permite la lectura y validación de códigos numéricos en crotales bovinos mediante técnicas de **Reconocimiento Óptico de Caracteres (OCR)**.

Desarrollado por **Jaudre Computer Vision Services** para la empresa cárnica **Fribin**, el sistema busca optimizar la trazabilidad en planta, reduciendo el error humano y acelerando el procesamiento de datos en la línea de producción.

## Objetivo del Proyecto

El núcleo del sistema es una aplicación de procesamiento de imágenes que:
1.  **Captura:** Recibe imágenes individuales de crotales desde una cámara fija en cinta transportadora.
2.  **Procesa:** Localiza la región de interés, mejora el contraste y corrige la alineación del texto.
3.  **Identifica:** Extrae las cuatro cifras inferiores del crotal con alta precisión.
4.  **Valida:** Contrasta el resultado con un *Ground Truth* (fichero Excel del lote) para detectar duplicados o registros inexistentes.

## Arquitectura del Sistema

El sistema sigue un pipeline secuencial de visión artificial para la lectura de crotales.

![Pipeline](docs/pipeline_mockup.svg)

El flujo de procesamiento es:

Dataset → Carga de imagen → Preprocesado → Detección del crotal → OCR → Resultado

## Tecnologías Principales

* **Lenguaje:** Python
* **Visión Artificial:** OpenCV
* **Motor OCR:** Tesseract OCR
* **Hardware:** Raspberry Pi 5
* **Estándar de Documentación:** IEEE Std 29148-2018

## Estructura del Proyecto
```
.
├── src/        # Código fuente del sistema
├── tests/      # Tests unitarios
├── data/       # Imágenes de prueba de crotales
├── docs/       # Diagramas y documentación técnica
└── README.md
```

## Instalación

Clonar el repositorio:

`git clone https://github.com/usuario/proyecto.git`

Instalar dependencias:

`pip install -r requirements.txt`

## Ejecución

`python src/pipeline/pipeline.py`


## Metodología de Desarrollo (GitFlow)

Para garantizar la estabilidad del sistema en producción (Raspberry Pi 5) y mantener un historial de cambios limpio, seguimos un flujo de trabajo basado en **Feature Branches**:

1.  **Creación de Tarea:** Cada nueva funcionalidad o corrección debe tener una *Issue* asignada con el prefijo `ETR-X`.
2.  **Ramificación:** No se trabaja directamente sobre `main` ni `dev`. Se crea una rama específica:
    * `git checkout -b feature/ETR-X-descripcion-corta`
3.  **Desarrollo e Integración:**
    * Se realizan los commits en la rama local.
    * Una vez finalizado, se sube la rama al repositorio: `git push origin feature/ETR-X-descripcion-corta`.
4.  **Pull Request (PR):**
    * Se abre un PR hacia la rama **`dev`** para integración y pruebas.
    * Tras validar el funcionamiento en el entorno de desarrollo, se realiza el merge.
5.  **Despliegue a Producción:** Solo el código verificado en `dev` se mergeará mediante PR a la rama **`main`** para su despliegue final en planta.

> ### Regla de Oro
> **Todo Pull Request debe referenciar la Issue correspondiente** (ej. `Closes #12`) para mantener la trazabilidad de los requisitos, tareas de desarrollo y cambios en el código.


## Contexto Operativo

El sistema está diseñado para operar en condiciones de iluminación controlada, procesando imágenes de forma secuencial con un tiempo de respuesta inferior a **2 segundos**, garantizando una integración fluida en el flujo de trabajo continuo de la planta de procesado.

---
© 2026 Jaudre Computer Vision Services. Todos los derechos reservados.
