# text_moderator.py

import openai
import logging
from config import OPENAI_API_KEY, TEXT_MODERATION_THRESHOLD, LOG_FILE

openai.api_key = OPENAI_API_KEY

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def moderate_text(text):
    """Moderate text content using OpenAI GPT-4."""
    response = openai.Moderation.create(input=text)
    
    flagged = False
    categories = response['results'][0]['categories']
    scores = response['results'][0]['category_scores']
    
    for category, score in scores.items():
        if score > TEXT_MODERATION_THRESHOLD:
            flagged = True
            logging.warning(f"Flagged content: {text} | Category: {category} | Score: {score}")
    
    return flagged

def run_text_moderation():
    """Main function to run text moderation."""
    logging.info("Starting Text Moderation Bot...")
    
    sample_texts = [
        "This is a great post!",
        "I hate you and everyone like you.",
        "Buy cheap meds here!"
    ]
    
    for text in sample_texts:
        if moderate_text(text):
            logging.warning(f"Text flagged for moderation: {text}")
        else:
            logging.info(f"Text passed moderation: {text}")

if __name__ == "__main__":
    run_text_moderation()