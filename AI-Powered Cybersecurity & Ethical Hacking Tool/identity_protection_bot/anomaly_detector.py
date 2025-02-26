# anomaly_detector.py

import numpy as np
from tensorflow.keras.models import load_model
from config import ANOMALY_THRESHOLD

def preprocess_user_data(data):
    """Preprocess user data for anomaly detection."""
    # Replace this with actual preprocessing logic
    return np.array(data)

def detect_anomalies(features):
    """Detect anomalies using a trained ML model."""
    model = load_model('models/anomaly_detection_model.h5')
    prediction = model.predict(np.array([features]))
    return prediction > ANOMALY_THRESHOLD

def run_anomaly_detection():
    """Main function to run the anomaly detector."""
    user_data = [0.1, 0.2, 0.3]  # Replace with actual user behavior data
    features = preprocess_user_data(user_data)
    
    if detect_anomalies(features):
        logging.warning("Anomalous behavior detected.")
    else:
        logging.info("No anomalies detected.")

if __name__ == "__main__":
    run_anomaly_detection()