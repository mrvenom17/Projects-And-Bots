# config.py

# Feedback Sources
FEEDBACK_SOURCES = [
    "data/reviews.csv",  # Path to reviews file
    "data/surveys.csv"   # Path to surveys file
]

# Sentiment Analysis Parameters
SENTIMENT_THRESHOLD = 0.5  # Threshold for positive/negative sentiment
TOPIC_COUNT = 5  # Number of topics to extract

# Logging
LOG_FILE = 'logs/feedback_analyzer.log'