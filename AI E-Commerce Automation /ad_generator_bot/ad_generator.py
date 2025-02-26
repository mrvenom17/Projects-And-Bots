# ad_generator.py

import openai
import pandas as pd
from config import OPENAI_API_KEY, PLATFORMS, PRODUCT_DATA

openai.api_key = OPENAI_API_KEY

# Configure logging
import logging
logging.basicConfig(filename='output/ad_generator.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_ad_copy(product, platform):
    """Generate ad copy using OpenAI GPT-4."""
    prompt = f"Write a compelling ad copy for {platform} to promote the following product:\n" \
             f"Product Name: {product['name']}\n" \
             f"Description: {product['description']}\n" \
             f"Price: {product['price']}\n" \
             f"Include a catchy headline, a short description, and a call-to-action."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def generate_all_ads():
    """Generate ad copies for all products and platforms."""
    logging.info("Starting Ad Copy Generation Bot...")
    all_ads = []
    
    for product in PRODUCT_DATA:
        for platform in PLATFORMS:
            logging.info(f"Generating ad for {product['name']} on {platform}")
            ad_copy = generate_ad_copy(product, platform)
            all_ads.append({
                'platform': platform,
                'product_name': product['name'],
                'ad_copy': ad_copy
            })
    
    df = pd.DataFrame(all_ads)
    df.to_csv('output/ads.csv', index=False)
    logging.info("Ad generation completed. Data saved to ads.csv")

if __name__ == "__main__":
    generate_all_ads()