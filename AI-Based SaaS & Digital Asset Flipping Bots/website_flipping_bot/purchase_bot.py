# purchase_bot.py

import requests
import logging
from config import BUDGET

def purchase_website(website):
    """Automate the process of purchasing a website."""
    if website['price'] > BUDGET:
        logging.info(f"Website {website['name']} is too expensive: {website['price']}")
        return
    
    # Example: Place an order via API or web form
    url = "https://flippa.com/api/purchase"
    payload = {
        "website_id": website['id'],
        "price": website['price']
    }
    headers = {"Authorization": "Bearer YOUR_API_TOKEN"}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            logging.info(f"Purchased website: {website['name']}")
        else:
            logging.error(f"Error purchasing website: {response.text}")
    except Exception as e:
        logging.error(f"Error purchasing website: {e}")

def run_purchase_bot():
    """Main function to run the purchase bot."""
    data = pd.read_csv('logs/evaluated_websites.csv')
    
    for _, row in data.iterrows():
        if row['evaluation'].split()[0] >= 7:  # Only purchase high-score websites
            purchase_website(row)

if __name__ == "__main__":
    run_purchase_bot()