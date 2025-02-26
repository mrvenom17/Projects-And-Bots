# scraper.py

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from config import WEBSITE_MARKETPLACES

# Configure logging
import logging
logging.basicConfig(filename='logs/website_scraper.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver():
    """Set up Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def scrape_flippa(driver):
    """Scrape website data from Flippa."""
    driver.get("https://flippa.com/websites")
    time.sleep(3)  # Avoid rate-limiting
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    websites = []
    for item in soup.find_all('div', class_='listing-card'):
        name = item.find('h3', class_='listing-title')
        price = item.find('span', class_='price')
        traffic = item.find('span', class_='traffic')
        revenue = item.find('span', class_='revenue')
        
        websites.append({
            'name': name.text.strip() if name else None,
            'price': price.text.strip() if price else None,
            'traffic': int(traffic.text.strip().replace(',', '')) if traffic else 0,
            'revenue': float(revenue.text.strip().replace('$', '')) if revenue else 0,
            'platform': 'Flippa'
        })
    return websites

def scrape_empire_flippers(driver):
    """Scrape website data from Empire Flippers."""
    driver.get("https://empireflippers.com/marketplace/")
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    websites = []
    for item in soup.find_all('div', class_='website-item'):
        name = item.find('h3', class_='website-name')
        price = item.find('span', class_='price-tag')
        traffic = item.find('span', class_='traffic-info')
        revenue = item.find('span', class_='revenue-info')
        
        websites.append({
            'name': name.text.strip() if name else None,
            'price': price.text.strip() if price else None,
            'traffic': int(traffic.text.strip().replace(',', '')) if traffic else 0,
            'revenue': float(revenue.text.strip().replace('$', '')) if revenue else 0,
            'platform': 'Empire Flippers'
        })
    return websites

def run_scraper():
    """Main function to run the scraper."""
    logging.info("Starting Website Scraper...")
    driver = setup_driver()
    all_websites = []
    
    for marketplace in WEBSITE_MARKETPLACES:
        if 'flippa' in marketplace:
            all_websites.extend(scrape_flippa(driver))
        elif 'empireflippers' in marketplace:
            all_websites.extend(scrape_empire_flippers(driver))
    
    driver.quit()
    df = pd.DataFrame(all_websites)
    df.to_csv('logs/websites.csv', index=False)
    logging.info("Scraping completed. Data saved to websites.csv")

if __name__ == "__main__":
    run_scraper()