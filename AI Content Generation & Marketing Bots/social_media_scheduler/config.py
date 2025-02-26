# config.py

# Twitter API Credentials
TWITTER_API_KEY = 'your_twitter_api_key'
TWITTER_API_SECRET = 'your_twitter_api_secret'
TWITTER_ACCESS_TOKEN = 'your_twitter_access_token'
TWITTER_ACCESS_SECRET = 'your_twitter_access_secret'

# Instagram API Credentials
INSTAGRAM_USERNAME = 'your_instagram_username'
INSTAGRAM_PASSWORD = 'your_instagram_password'

# LinkedIn API Credentials
LINKEDIN_CLIENT_ID = 'your_linkedin_client_id'
LINKEDIN_CLIENT_SECRET = 'your_linkedin_client_secret'
LINKEDIN_ACCESS_TOKEN = 'your_linkedin_access_token'

# Facebook API Credentials
FACEBOOK_PAGE_ID = 'your_facebook_page_id'
FACEBOOK_ACCESS_TOKEN = 'your_facebook_access_token'

# Scheduled Posts
POSTS = [
    {"platform": "twitter", "content": "Check out our latest blog post: https://example.com", "time": "2023-10-15 10:00:00"},
    {"platform": "instagram", "content": "images/post1.jpg", "caption": "Our latest product is here!", "time": "2023-10-15 12:00:00"},
    {"platform": "linkedin", "content": "Excited to share our new project!", "time": "2023-10-15 14:00:00"},
    {"platform": "facebook", "content": "Check out our latest video: https://youtube.com/example", "time": "2023-10-15 16:00:00"}
]