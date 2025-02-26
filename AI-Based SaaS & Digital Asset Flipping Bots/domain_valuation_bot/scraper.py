# scraper.py

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from config import DOMAIN_MARKETPLACES

# Configure logging
import logging
logging.basicConfig(filename='output/domain_scraper.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver():
    """Set up Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def scrape_flippa(driver):
    """Scrape domain data from Flippa."""
    driver.get("https://flippa.com/domains")
    time.sleep(3)  # Avoid rate-limiting
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    domains = []
    for item in soup.find_all('div', class_='listing-card'):
        name = item.find('h3', class_='listing-title')
        price = item.find('span', class_='price')
        traffic = item.find('span', class_='traffic')
        backlinks = item.find('span', class_='backlinks')
        
        domains.append({
            'name': name.text.strip() if name else None,
            'price': price.text.strip() if price else None,
            'traffic': int(traffic.text.strip().replace(',', '')) if traffic else 0,
            'backlinks': int(backlinks.text.strip()) if backlinks else 0,
            'platform': 'Flippa'
        })
    return domains

def scrape_sedo(driver):
    """Scrape domain data from Sedo."""
    driver.get("https://sedo.com/search/")
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    domains = []
    for item in soup.find_all('div', class_='domain-item'):
        name = item.find('h3', class_='domain-name')
        price = item.find('span', class_='price-tag')
        traffic = item.find('span', class_='traffic-info')
        backlinks = item.find('span', class_='backlink-count')
        
        domains.append({
            'name': name.text.strip() if name else None,
            'price': price.text.strip() if price else None,
            'traffic': int(traffic.text.strip().replace(',', '')) if traffic else 0,
            'backlinks': int(backlinks.text.strip()) if backlinks else 0,
            'platform': 'Sedo'
        })
    return domains

def run_scraper():
    """Main function to run the scraper."""
    logging.info("Starting Domain Scraper...")
    driver = setup_driver()
    all_domains = []
    
    for marketplace in DOMAIN_MARKETPLACES:
        if 'flippa' in marketplace:
            all_domains.extend(scrape_flippa(driver))
        elif 'sedo' in marketplace:
            all_domains.extend(scrape_sedo(driver))
    
    driver.quit()
    df = pd.DataFrame(all_domains)
    df.to_csv('output/domains.csv', index=False)
    logging.info("Scraping completed. Data saved to domains.csv")

if __name__ == "__main__":
    run_scraper()