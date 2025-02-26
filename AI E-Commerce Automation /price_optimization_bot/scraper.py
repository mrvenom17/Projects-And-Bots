# scraper.py

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from config import COMPETITOR_URLS

# Configure logging
import logging
logging.basicConfig(filename='logs/scraper.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver():
    """Set up Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def scrape_amazon(driver, url):
    """Scrape product prices from Amazon."""
    driver.get(url)
    time.sleep(3)  # Avoid rate-limiting
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    prices = []
    for item in soup.find_all('div', {'data-component-type': 's-search-result'}):
        price = item.find('span', class_='a-price-whole')
        prices.append(float(price.text.strip()) if price else None)
    
    return [p for p in prices if p is not None]

def scrape_aliexpress(driver, url):
    """Scrape product prices from AliExpress."""
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    prices = []
    for item in soup.find_all('div', class_='manhattan--price-sale--1CCSZfK'):
        price = item.text.strip().replace('$', '')
        prices.append(float(price) if price else None)
    
    return [p for p in prices if p is not None]

def scrape_ebay(driver, url):
    """Scrape product prices from eBay."""
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    prices = []
    for item in soup.find_all('span', class_='s-item__price'):
        price = item.text.strip().replace('$', '')
        prices.append(float(price) if price else None)
    
    return [p for p in prices if p is not None]

def run_scraper():
    """Main function to run the scraper."""
    logging.info("Starting Price Scraper...")
    driver = setup_driver()
    all_prices = []
    
    for url in COMPETITOR_URLS:
        if 'amazon' in url:
            all_prices.extend(scrape_amazon(driver, url))
        elif 'aliexpress' in url:
            all_prices.extend(scrape_aliexpress(driver, url))
        elif 'ebay' in url:
            all_prices.extend(scrape_ebay(driver, url))
    
    driver.quit()
    df = pd.DataFrame(all_prices, columns=['price'])
    df.to_csv('logs/competitor_prices.csv', index=False)
    logging.info("Scraping completed. Data saved to competitor_prices.csv")

if __name__ == "__main__":
    run_scraper()