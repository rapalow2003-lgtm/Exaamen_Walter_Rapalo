import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

st.set_page_config(
    page_title="Clasificador de Objetos",
    page_icon="📷",
    layout="centered"
)

st.title("📷 Clasificador de Objetos en Imágenes")
st.write("Examen Walter Edurado Rapalo Smith")
st.write("---")

@st.cache_resource
def load_trained_model():
    return tf.keras.models.load_model('cifar10_model.keras')

with st.spinner("Cargando modelo de IA..."):
    model = load_trained_model()

class_names = ['Avión', 'Auto', 'Pájaro', 'Gato', 'Ciervo', 
               'Perro', 'Rana', 'Caballo', 'Barco', 'Camión']

st.markdown("### 1. Selecciona cómo ingresar la imagen")
option = st.radio("Método:", ("Subir una imagen", "Tomar foto con la cámara"))

image = None

if option == "Subir una imagen":
    uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
else:
    camera_file = st.camera_input("Toma una foto")
    if camera_file is not None:
        image = Image.open(camera_file)

if image is not None:
    st.image(image, caption="Imagen ingresada", use_column_width=True)
    
    if st.button("🚀 Analizar Imagen"):
        with st.spinner("Procesando imagen con la Red Neuronal..."):
            img_resized = image.convert('RGB').resize((32, 32))
            img_array = np.array(img_resized) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            
            predictions = model.predict(img_array)
            predicted_class = class_names[np.argmax(predictions)]
            confidence = np.max(predictions)
            
            st.success("¡Análisis completado!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Predicción", value=predicted_class)
            with col2:
                st.metric(label="Confianza", value=f"{confidence * 100:.2f}%")
