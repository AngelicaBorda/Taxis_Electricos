import streamlit as st
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from imblearn.over_sampling import SMOTE
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

st.markdown("""
    <style>
        .centered_title {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='centered_title'>TRANSPORTER</h1>",
            unsafe_allow_html=True)
st.markdown('Transporter es nuestro sistema de IA, encargado de clasificar las reseñas de usuarios de taxis. Es capaz de clasificar el tipo de opinión vertida por los usuarios y además realiza un análisis de sentimiento.')

st.markdown('***')
st.markdown('## ¿Cómo funciona Transporter?')
st.markdown('''El sistema de IA se alimenta de reseñas, las cuales procesa y clasifica con el algoritmo Decision Tree Classifier, devolviendo la categoría en la cual se ajusta la reseña:
- Recomendación Generales
- Recomendación por el buen servicio del conductor 
- Recomendación por el buen estado del vehículo 
- Quejas por el mal servicio del conductor 
Luego con la herramienta Sentiment Intensity Analyzer realiza una análisis de sentimiento, el cual puede ser: positivo, negativo o neutro.
''')


sia = SentimentIntensityAnalyzer()


def etiquetar_sentimiento(texto):
    if pd.notnull(texto):
        score = sia.polarity_scores(texto)['compound']

        if score >= 0.05:
            return 'Positivo'  # Sentimiento positivo
        elif -0.05 < score < 0.05:
            return 'Neutro'  # Sentimiento neutro
        else:
            return 'Negativo'  # Sentimiento negativo
    else:
        return 'Neutro'  # Cuando es nulo, se asume un sentimiento neutro


# Datos de ejemplo (reemplázalos con tus propios datos)
df_reseñas = pd.read_csv("Streamlit/reviews.csv")

# Preprocesamiento de texto y vectorización
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df_reseñas['review_english'])
y = df_reseñas['category']

# Aplicación de SMOTE para balancear la base de datos
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# División de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.2, random_state=42)

# Entrenamiento del modelo de árbol de decisión
tree_classifier = DecisionTreeClassifier(random_state=42)
tree_classifier.fit(X_train, y_train)

# Definir la aplicación Streamlit


def main():
    st.markdown("### Clasificación de Reseñas")

    # Textbox para que el usuario ingrese una reseña
    reseña = st.text_area("Ingresa una reseña en inglés:")

    # Preprocesamiento de la reseña ingresada por el usuario
    reseña_vectorizada = vectorizer.transform([reseña])

    # Realizar la predicción
    if st.button("Predecir"):
        categoria_predicha = tree_classifier.predict(reseña_vectorizada)
        sentimiento = etiquetar_sentimiento(reseña)

        st.write("La reseña ingresada por el usuario es:", reseña)
        st.write("La categoría predicha para esta reseña es:",
                 categoria_predicha[0])
        st.write("El sentimiento de esta reseña es:", sentimiento)


if __name__ == "__main__":
    main()
