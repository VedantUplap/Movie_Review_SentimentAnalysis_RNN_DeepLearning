import streamlit as st
import tensorflow as tf

from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load trained model
model = tf.keras.models.load_model('sentiment_rnn_model.h5')

# Load word index
word_index = imdb.get_word_index()

# Encoding function
def encode_review(text):

    words = text.lower().split()

    encoded = []

    for word in words:

        index = word_index.get(word)

        if index is not None and index < 10000:
            encoded.append(index + 3)

    padded = pad_sequences([encoded], maxlen=100, padding='post')

    return padded

# Streamlit UI
st.title("Movie Review Sentiment Analysis")

review = st.text_area("Enter Movie Review")

if st.button("Predict Sentiment"):

    processed_review = encode_review(review)

    prediction = model.predict(processed_review)

    if prediction[0][0] > 0.5:
        st.success("Positive Review ")

    else:
        st.error("Negative Review ")