# scraper.py

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from config import PLATFORMS, CATEGORIES, MAX_PAGES

# Configure logging
import logging
logging.basicConfig(filename='output/scraping.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver():
    """Set up Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def scrape_amazon(driver, category):
    """Scrape product data from Amazon."""
    products = []
    for page in range(1, MAX_PAGES + 1):
        url = f"https://www.amazon.com/s?k={category}&page={page}"
        driver.get(url)
        time.sleep(3)  # Avoid rate-limiting
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        for item in soup.find_all('div', {'data-component-type': 's-search-result'}):
            name = item.find('span', class_='a-size-medium')
            price = item.find('span', class_='a-price-whole')
            rating = item.find('span', class_='a-icon-alt')
            
            products.append({
                'name': name.text.strip() if name else None,
                'price': price.text.strip() if price else None,
                'rating': rating.text.strip() if rating else None,
                'platform': 'Amazon'
            })
    return products

def scrape_aliexpress(driver, category):
    """Scrape product data from AliExpress."""
    products = []
    for page in range(1, MAX_PAGES + 1):
        url = f"https://www.aliexpress.com/wholesale?SearchText={category}&page={page}"
        driver.get(url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        for item in soup.find_all('div', class_='manhattan--content--1KpBbUi'):
            name = item.find('h1')
            price = item.find('div', class_='manhattan--price-sale--1CCSZfK')
            rating = item.find('span', class_='manhattan--evaluation--3cSMntr')
            
            products.append({
                'name': name.text.strip() if name else None,
                'price': price.text.strip() if price else None,
                'rating': rating.text.strip() if rating else None,
                'platform': 'AliExpress'
            })
    return products

def scrape_ebay(driver, category):
    """Scrape product data from eBay."""
    products = []
    for page in range(1, MAX_PAGES + 1):
        url = f"https://www.ebay.com/sch/i.html?_nkw={category}&_pgn={page}"
        driver.get(url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        for item in soup.find_all('div', class_='s-item__info'):
            name = item.find('h3', class_='s-item__title')
            price = item.find('span', class_='s-item__price')
            rating = item.find('div', class_='x-star-rating')
            
            products.append({
                'name': name.text.strip() if name else None,
                'price': price.text.strip() if price else None,
                'rating': rating.text.strip() if rating else None,
                'platform': 'eBay'
            })
    return products

def run_scraper():
    """Main function to run the scraper."""
    logging.info("Starting Product Research Bot...")
    driver = setup_driver()
    all_products = []
    
    for platform in PLATFORMS:
        for category in CATEGORIES:
            logging.info(f"Scraping {category} from {platform}")
            if platform == 'amazon':
                all_products.extend(scrape_amazon(driver, category))
            elif platform == 'aliexpress':
                all_products.extend(scrape_aliexpress(driver, category))
            elif platform == 'ebay':
                all_products.extend(scrape_ebay(driver, category))
    
    driver.quit()
    df = pd.DataFrame(all_products)
    df.to_csv('output/products.csv', index=False)
    logging.info("Scraping completed. Data saved to products.csv")

if __name__ == "__main__":
    run_scraper()