# scheduler.py

import tweepy
from instabot import Bot
from linkedin_api import Linkedin
import facebook
import schedule
import time
import logging
from config import POSTS, TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET, \
    INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, LINKEDIN_ACCESS_TOKEN, FACEBOOK_PAGE_ID, FACEBOOK_ACCESS_TOKEN

# Configure logging
logging.basicConfig(filename='logs/social_media_scheduler.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def post_to_twitter(content):
    """Post content to Twitter."""
    auth = tweepy.OAuth1UserHandler(TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)
    try:
        api.update_status(content)
        logging.info(f"Posted to Twitter: {content}")
    except Exception as e:
        logging.error(f"Error posting to Twitter: {e}")

def post_to_instagram(image_path, caption):
    """Post image to Instagram."""
    bot = Bot()
    bot.login(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)
    try:
        bot.upload_photo(image_path, caption=caption)
        logging.info(f"Posted to Instagram: {image_path} with caption: {caption}")
    except Exception as e:
        logging.error(f"Error posting to Instagram: {e}")

def post_to_linkedin(content):
    """Post content to LinkedIn."""
    linkedin = Linkedin('', '', LINKEDIN_ACCESS_TOKEN, '')
    try:
        linkedin.post_share(comment=content)
        logging.info(f"Posted to LinkedIn: {content}")
    except Exception as e:
        logging.error(f"Error posting to LinkedIn: {e}")

def post_to_facebook(content):
    """Post content to Facebook."""
    graph = facebook.GraphAPI(access_token=FACEBOOK_ACCESS_TOKEN)
    try:
        graph.put_object(parent_object=FACEBOOK_PAGE_ID, connection_name='feed', message=content)
        logging.info(f"Posted to Facebook: {content}")
    except Exception as e:
        logging.error(f"Error posting to Facebook: {e}")

def schedule_posts():
    """Schedule posts based on predefined times."""
    for post in POSTS:
        platform = post['platform']
        content = post.get('content')
        time_to_post = post['time']
        
        if platform == 'twitter':
            schedule.every().day.at(time_to_post).do(post_to_twitter, content)
        elif platform == 'instagram':
            image_path = content
            caption = post.get('caption', '')
            schedule.every().day.at(time_to_post).do(post_to_instagram, image_path, caption)
        elif platform == 'linkedin':
            schedule.every().day.at(time_to_post).do(post_to_linkedin, content)
        elif platform == 'facebook':
            schedule.every().day.at(time_to_post).do(post_to_facebook, content)

def run_scheduler():
    """Main function to run the scheduler."""
    logging.info("Starting Social Media Scheduler...")
    schedule_posts()
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduler()