# content_generator.py

import openai
import logging
from config import OPENAI_API_KEY, PLATFORMS, CONTENT_TYPES, HASHTAG_COUNT, VIDEO_SCRIPT_DURATION

openai.api_key = OPENAI_API_KEY

# Configure logging
logging.basicConfig(filename='output/content_generator.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_caption(topic):
    """Generate a caption for a social media post."""
    prompt = f"Write an engaging caption about {topic} for a social media post."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def generate_hashtags(topic):
    """Generate relevant hashtags for a social media post."""
    prompt = f"Generate {HASHTAG_COUNT} relevant hashtags for a post about {topic}."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip().split()

def generate_video_script(topic):
    """Generate a video script for TikTok or YouTube."""
    prompt = f"Write a {VIDEO_SCRIPT_DURATION}-second video script about {topic}. Include dialogue and scene descriptions."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text.strip()

def run_content_generator():
    """Main function to run the content generator."""
    logging.info("Starting Influencer Content Generator Bot...")
    
    topic = "travel tips"  # Replace with actual topic
    
    for platform in PLATFORMS:
        for content_type in CONTENT_TYPES:
            if content_type == 'caption':
                caption = generate_caption(topic)
                logging.info(f"Generated caption for {platform}: {caption}")
            elif content_type == 'hashtag':
                hashtags = generate_hashtags(topic)
                logging.info(f"Generated hashtags for {platform}: {hashtags}")
            elif content_type == 'video_script':
                script = generate_video_script(topic)
                logging.info(f"Generated video script for {platform}: {script}")

if __name__ == "__main__":
    run_content_generator()