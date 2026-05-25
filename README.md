# Movie Review Sentiment Analysis using RNN

This project performs Sentiment Analysis on movie reviews using:

- Integer Encoding
- Word Embedding
- Simple RNN (Recurrent Neural Network)
- TensorFlow/Keras
- Streamlit

The model predicts whether a movie review is:

- Positive 
- Negative 

---

# Deep Learning Concepts Used

- NLP (Natural Language Processing)
- Integer Encoding
- Sequence Padding
- Word Embedding
- SimpleRNN
- Binary Classification

---

# Tech Stack

- Python
- TensorFlow
- Keras
- NumPy
- Streamlit

---

# Dataset Used

IMDB Movie Review Dataset from Keras.

- 25,000 Training Reviews
- 25,000 Testing Reviews

---

# Model Architecture

```python
Embedding Layer
↓
SimpleRNN Layer
↓
Dense Output Layer
```

---

# Project Structure

```text
SentimentAnalysis_RNN_DeepLearning/
│
├── app.py
├── main.py
├── sentiment_rnn_model.h5
├── README.md
├── .gitignore
└── Notebook/
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Movie_Review_SentimentAnalysis_RNN_DeepLearning.git
```

Move into project directory:

```bash
cd Movie_Review_SentimentAnalysis_RNN_DeepLearning
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run Streamlit App

```bash
streamlit run app.py
```

---

# Model Training

The model was trained using:

- Embedding Dimension = 32
- Max Sequence Length = 100
- Optimizer = Adam
- Loss Function = Binary Crossentropy
- Epochs = 5

---

# Sample Predictions

| Review | Prediction |
|--------|------------|
| "This movie was amazing" | Positive  |
| "Worst movie ever" | Negative  |

---


# Author

Vedant Uplap
