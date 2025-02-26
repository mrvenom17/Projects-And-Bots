# feedback_analyzer.py

import pandas as pd
from sentiment_model import analyze_sentiment
from topic_model import extract_topics
import logging
from config import FEEDBACK_SOURCES, SENTIMENT_THRESHOLD, TOPIC_COUNT, LOG_FILE

# Configure logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_feedback_data():
    """Load feedback data from multiple sources."""
    feedback_data = []
    
    for source in FEEDBACK_SOURCES:
        data = pd.read_csv(source)
        feedback_data.append(data['feedback'].tolist())
    
    return [item for sublist in feedback_data for item in sublist]  # Flatten list

def analyze_feedback(feedback):
    """Analyze feedback using sentiment analysis and topic modeling."""
    sentiment_scores = analyze_sentiment(feedback)
    topics = extract_topics(feedback, TOPIC_COUNT)
    
    return sentiment_scores, topics

def run_feedback_analyzer():
    """Main function to run the feedback analyzer."""
    logging.info("Starting Customer Feedback Analyzer Bot...")
    
    feedback = load_feedback_data()
    sentiment_scores, topics = analyze_feedback(feedback)
    
    # Log results
    logging.info(f"Sentiment Scores: {sentiment_scores}")
    logging.info(f"Extracted Topics: {topics}")

if __name__ == "__main__":
    run_feedback_analyzer()