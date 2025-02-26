# config.py

OPENAI_API_KEY = 'your_openai_api_key'

# Moderation Parameters
TEXT_MODERATION_THRESHOLD = 0.8  # Confidence threshold for flagging inappropriate text
IMAGE_MODERATION_MODEL = 'models/explicit_content_model.h5'  # Path to trained image moderation model
LOG_FILE = 'logs/content_moderation.log'