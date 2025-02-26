# scraper.py

import requests
from bs4 import BeautifulSoup
import logging
from config import DARK_WEB_URLS, MONITOR_KEYWORDS, TOR_PROXY

# Configure logging
logging.basicConfig(filename='logs/deep_web_scraper.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def setup_tor_session():
    """Set up a session using Tor for anonymous browsing."""
    session = requests.session()
    session.proxies = TOR_PROXY
    return session

def scrape_dark_web(session, url):
    """Scrape data from a dark web URL."""
    try:
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        posts = []
        for post in soup.find_all('div', class_='post'):
            content = post.text.lower()
            if any(keyword in content for keyword in MONITOR_KEYWORDS):
                posts.append(content)
        
        return posts
    except Exception as e:
        logging.error(f"Error scraping {url}: {e}")
        return []

def run_scraper():
    """Main function to run the scraper."""
    logging.info("Starting Dark Web Scraper...")
    session = setup_tor_session()
    all_posts = []
    
    for url in DARK_WEB_URLS:
        posts = scrape_dark_web(session, url)
        all_posts.extend(posts)
    
    df = pd.DataFrame(all_posts, columns=['content'])
    df.to_csv('logs/dark_web_data.csv', index=False)
    logging.info("Scraping completed. Data saved to dark_web_data.csv")

if __name__ == "__main__":
    run_scraper()