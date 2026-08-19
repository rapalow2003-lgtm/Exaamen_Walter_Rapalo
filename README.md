
## Información del Estudiante
* **Estudiante:** Walter Eduardo Rápalo Smith
* **Asignatura:** Computación en la Nube
* **Docente:** Ing. Asalia Zavala
* **Institución:** Universidad Tecnológica de Honduras (UTH)

## Enlaces del Proyecto
**Aplicación Desplegada:** [https://exaamenwalterrapalo-7vqm4batcjpfhg7khur4ep.streamlit.app/]
**Repositorio de Código:** [Poner aquí la URL de este repositorio en GitHub]

## Objetivos
1. Entrenar un modelo de clasificación de imágenes en **Google Colab** utilizando TensorFlow y Keras.
2. Utilizar el dataset **CIFAR-10** (10 clases distintas de objetos cotidianos y transporte).
3. Exportar e integrar el modelo entrenado (`cifar10_model.keras`) en una interfaz interactiva desarrollada con **Streamlit**.
4. Desplegar la solución en la nube mediante **Streamlit Cloud**.

## Tecnologías y Librerías
* **Lenguaje:** Python 3.11
* **Entrenamiento de IA:** TensorFlow / Keras, NumPy, Google Colab
* **Interfaz de Usuario:** Streamlit, Pillow (PIL)
* **Despliegue y Control de Versiones:** GitHub, Streamlit Cloud

## Dataset: CIFAR-10
El modelo fue entrenado con el conjunto de datos **CIFAR-10**, el cual contiene 60,000 imágenes a color de 32x32 píxeles distribuidas equitativamente en 10 clases:

| Categoría | Nombre en la App |
| :--- | :--- |
| **Airplane** | Avión ✈️ |
| **Automobile** | Auto 🚗 |
| **Bird** | Pájaro 🐦 |
| **Cat** | Gato 🐱 |
| **Deer** | Ciervo 🦌 |
| **Dog** | Perro 🐶 |
| **Frog** | Rana 🐸 |
| **Horse** | Caballo 🐴 |
| **Ship** | Barco 🚢 |
| **Truck** | Camión 🚚 |

## ¿Cómo Usar la Aplicación?
1. **Seleccionar método de entrada:**
   * **Subir una imagen:** Permite cargar archivos `.png`, `.jpg` o `.jpeg` desde el ordenador o teléfono móvil.
   * **Tomar foto con la cámara:** Captura una fotografía en vivo utilizando la cámara web.
2. **Procesar la imagen:** Haz clic en el botón **🚀 Analizar Imagen**.
3. **Ver Resultados:** La aplicación redimensiona la imagen al formato $32 \times 32$, realiza la inferencia con el modelo cargado y muestra la **Categoría Identificada** junto con el **Porcentaje de Confianza (%)**.
