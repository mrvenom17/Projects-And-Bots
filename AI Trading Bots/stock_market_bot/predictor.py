# predictor.py

import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from config import MODEL_PATH

def preprocess_data(data):
    """Preprocess stock data for prediction."""
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1, 1))
    
    x = []
    y = []
    for i in range(60, len(scaled_data)):
        x.append(scaled_data[i-60:i, 0])
        y.append(scaled_data[i, 0])
    
    x, y = np.array(x), np.array(y)
    x = np.reshape(x, (x.shape[0], x.shape[1], 1))
    return x, y, scaler

def predict_price_movement(stock_symbol):
    """Predict stock price movement using a trained model."""
    data = pd.read_csv(f"data/{stock_symbol}_historical.csv")
    x, _, scaler = preprocess_data(data)
    
    model = load_model(MODEL_PATH)
    predictions = model.predict(x)
    predictions = scaler.inverse_transform(predictions)
    
    return predictions[-1][0]  # Return the latest prediction

def run_predictor():
    """Main function to run the predictor."""
    for stock in STOCKS_TO_MONITOR:
        prediction = predict_price_movement(stock)
        print(f"Predicted price for {stock}: {prediction}")

if __name__ == "__main__":
    run_predictor()