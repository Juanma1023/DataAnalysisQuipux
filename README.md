# Data Analysis Quipux

Este repositorio contiene un proyecto de análisis de datos y modelado predictivo relacionado con la polucion. El objetivo principal es procesar datos de contaminación atmosférica y entrenar un modelo que pueda predecir los niveles de PM2.5 en función de diversas características.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **Data/**: Contiene los archivos de datos originales utilizados para el análisis.
- **DataClean/**: Incluye el módulo `dataClean.py` con la clase `Data` para la carga y limpieza de los datos.
- **Model/**: Contiene el módulo `model.py` con la clase `Pollution` para el entrenamiento y evaluación del modelo predictivo.
- **main.py**: Script principal que realiza la carga, limpieza, entrenamiento y evaluación del modelo.
- **test.py**: Script para pruebas adicionales o validación del modelo.

## Requisitos

Para ejecutar este proyecto, es necesario tener instalado:

- Python 3.6 o superior
- Las dependencias se encuentran listadas en `requirements.txt`

Puedes instalar las dependencias utilizando:

```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar el flujo completo del proyecto, simplemente ejecuta:

```bash
python main.py
```
## Test Modelo

Para ejecutar la prueba del modelo, simplemente ejecuta:

```bash
python test.py


