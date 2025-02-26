# optimizer.py

import pandas as pd
import requests
from config import SHOP_URL, SHOP_API_KEY, PRODUCT_IDS, PRICE_MARGIN

# Configure logging
import logging
logging.basicConfig(filename='logs/optimizer.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def update_product_price(product_id, new_price):
    """Update product price in the store."""
    url = f"{SHOP_URL}/admin/api/2023-01/products/{product_id}.json"
    headers = {"X-Shopify-Access-Token": SHOP_API_KEY}
    payload = {
        "product": {
            "id": product_id,
            "variants": [{"price": new_price}]
        }
    }
    response = requests.put(url, json=payload, headers=headers)
    if response.status_code == 200:
        logging.info(f"Updated price for product {product_id} to {new_price}")
    else:
        logging.error(f"Failed to update price for product {product_id}: {response.text}")

def optimize_prices():
    """Optimize product prices based on competitor data."""
    logging.info("Starting Price Optimization...")
    competitor_prices = pd.read_csv('logs/competitor_prices.csv')['price']
    avg_competitor_price = competitor_prices.mean()
    
    for product_id in PRODUCT_IDS:
        new_price = avg_competitor_price * (1 + PRICE_MARGIN)
        update_product_price(product_id, round(new_price, 2))

if __name__ == "__main__":
    optimize_prices()