import streamlit as st
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

st.title('Análisis de Datos para Empresa de Taxis en ciudad de NY')

st.markdown('***')
st.markdown('Una empresa de servicios de transporte de pasajeros, especializada en micros de media y larga distancia, busca expandir sus operaciones al sector de transporte de pasajeros con automóviles. Con el objetivo de avanzar hacia un futuro más sostenible y adaptarse a las tendencias del mercado, la empresa pretende evaluar la relación entre los medios de transporte particulares y la calidad del aire, así como la contaminación sonora. El análisis preliminar se centrará en el movimiento de taxis en la ciudad de Nueva York como referencia para la posible implementación de vehículos eléctricos en la flota.')

st.markdown('***')
st.markdown('# TRANSPORTER')
st.markdown('### Explicación del modelo y como funciona')


# Datos de ejemplo (reemplázalos con tus propios datos)
df_reseñas = pd.read_csv("reviews.csv")

# Preprocesamiento de texto y vectorización
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df_reseñas['review_english'])
y = df_reseñas['category']

# División de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Entrenamiento del modelo de árbol de decisión
tree_classifier = DecisionTreeClassifier(random_state=42)
tree_classifier.fit(X_train, y_train)

# Definir la aplicación Streamlit


def main():
    st.title("Clasificación de Reseñas")

    # Textbox para que el usuario ingrese una reseña
    reseña = st.text_area("Ingresa una reseña en inglés:")

    # Preprocesamiento de la reseña ingresada por el usuario
    reseña_vectorizada = vectorizer.transform([reseña])

    # Realizar la predicción
    if st.button("Predecir"):
        categoria_predicha = tree_classifier.predict(reseña_vectorizada)
        st.write("La categoría predicha para esta reseña es:",
                 categoria_predicha[0])


if __name__ == "__main__":
    main()
