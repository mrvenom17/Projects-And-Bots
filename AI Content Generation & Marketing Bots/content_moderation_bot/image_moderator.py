# image_moderator.py

import tensorflow as tf
import cv2
import numpy as np
import logging
from config import IMAGE_MODERATION_MODEL, LOG_FILE

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def preprocess_image(image_path):
    """Preprocess image for moderation."""
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def moderate_image(image_path):
    """Moderate image content using a trained model."""
    model = tf.keras.models.load_model(IMAGE_MODERATION_MODEL)
    img = preprocess_image(image_path)
    prediction = model.predict(img)
    
    if prediction[0][0] > 0.5:  # Assuming binary classification (explicit vs non-explicit)
        logging.warning(f"Image flagged for explicit content: {image_path}")
        return True
    return False

def run_image_moderation():
    """Main function to run image moderation."""
    logging.info("Starting Image Moderation Bot...")
    
    sample_images = [
        "images/sample1.jpg",
        "images/sample2.jpg",
        "images/sample3.jpg"
    ]
    
    for image in sample_images:
        if moderate_image(image):
            logging.warning(f"Image flagged for moderation: {image}")
        else:
            logging.info(f"Image passed moderation: {image}")

if __name__ == "__main__":
    run_image_moderation()