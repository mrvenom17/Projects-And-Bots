# model_training.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import talib
import logging

# Configure logging
logging.basicConfig(filename='logs/model_training.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_historical_data():
    """Load historical Forex data."""
    # Replace this with actual data loading logic (e.g., from MT4 or CSV)
    data = pd.read_csv('data/historical_forex_data.csv')
    return data

def calculate_indicators(data):
    """Calculate technical indicators."""
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
    data['MACD'], _, _ = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    data['SMA_50'] = talib.SMA(data['Close'], timeperiod=50)
    data['SMA_200'] = talib.SMA(data['Close'], timeperiod=200)
    return data.dropna()

def train_model(data):
    """Train a predictive model."""
    features = ['RSI', 'MACD', 'SMA_50', 'SMA_200']
    target = 'Signal'  # 1 for Buy, 0 for Sell
    
    X = data[features]
    y = data[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    accuracy = model.score(X_test, y_test)
    logging.info(f"Model trained with accuracy: {accuracy}")
    return model

if __name__ == "__main__":
    data = load_historical_data()
    data = calculate_indicators(data)
    model = train_model(data)