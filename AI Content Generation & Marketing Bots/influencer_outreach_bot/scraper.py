# scraper.py

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from config import PLATFORMS, SEARCH_KEYWORDS, MIN_FOLLOWERS

# Configure logging
import logging
logging.basicConfig(filename='output/influencer_scraper.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver():
    """Set up Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def scrape_instagram(driver, keyword):
    """Scrape influencer data from Instagram."""
    url = f"https://www.instagram.com/explore/tags/{keyword}/"
    driver.get(url)
    time.sleep(3)  # Avoid rate-limiting
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    influencers = []
    for item in soup.find_all('div', class_='v1Nh3'):
        username = item.find('a')['href'].split('/')[1]
        followers = int(item.find('span', class_='g47SY').text.replace(',', ''))
        
        if followers >= MIN_FOLLOWERS:
            influencers.append({
                'platform': 'Instagram',
                'username': username,
                'followers': followers
            })
    return influencers

def scrape_twitter(driver, keyword):
    """Scrape influencer data from Twitter."""
    url = f"https://twitter.com/search?q={keyword}&src=typed_query"
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    influencers = []
    for item in soup.find_all('div', class_='css-1dbjc4n'):
        username = item.find('span', class_='css-901oao').text
        followers = int(item.find('span', class_='css-901oao').text.split(' ')[0].replace(',', ''))
        
        if followers >= MIN_FOLLOWERS:
            influencers.append({
                'platform': 'Twitter',
                'username': username,
                'followers': followers
            })
    return influencers

def run_scraper():
    """Main function to run the scraper."""
    logging.info("Starting Influencer Scraper...")
    driver = setup_driver()
    all_influencers = []
    
    for platform in PLATFORMS:
        for keyword in SEARCH_KEYWORDS:
            if platform == 'instagram':
                all_influencers.extend(scrape_instagram(driver, keyword))
            elif platform == 'twitter':
                all_influencers.extend(scrape_twitter(driver, keyword))
    
    driver.quit()
    df = pd.DataFrame(all_influencers)
    df.to_csv('output/influencers.csv', index=False)
    logging.info("Scraping completed. Data saved to influencers.csv")

if __name__ == "__main__":
    run_scraper()