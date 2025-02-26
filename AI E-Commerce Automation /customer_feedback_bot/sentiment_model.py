# sentiment_model.py

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def preprocess_text(texts, tokenizer, max_length):
    """Preprocess text data for sentiment analysis."""
    sequences = tokenizer.texts_to_sequences(texts)
    padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')
    return padded_sequences

def analyze_sentiment(feedback):
    """Analyze sentiment of feedback using a trained model."""
    model = load_model('models/sentiment_model.h5')
    tokenizer = Tokenizer(num_words=10000)
    max_length = 100
    
    processed_feedback = preprocess_text(feedback, tokenizer, max_length)
    predictions = model.predict(processed_feedback)
    
    sentiment_scores = [1 if pred > 0.5 else 0 for pred in predictions]  # 1 = Positive, 0 = Negative
    return sentiment_scores