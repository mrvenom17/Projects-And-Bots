# monitor.py

import requests
import logging
from config import HIBP_API_KEY, USER_DATA

# Configure logging
logging.basicConfig(filename='logs/identity_monitor.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_data_breach(email):
    """Check if an email has been involved in a data breach."""
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": HIBP_API_KEY}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            breaches = response.json()
            logging.warning(f"Data breaches detected for {email}: {breaches}")
            return breaches
        elif response.status_code == 404:
            logging.info(f"No breaches found for {email}")
            return []
        else:
            logging.error(f"Error checking breaches: {response.text}")
            return []
    except Exception as e:
        logging.error(f"Error checking breaches: {e}")
        return []

def run_monitor():
    """Main function to run the identity monitor."""
    logging.info("Starting Identity Protection Bot...")
    
    for key, value in USER_DATA.items():
        if key == 'email':
            breaches = check_data_breach(value)
            if breaches:
                logging.warning(f"Breaches detected for {key}: {value}")

if __name__ == "__main__":
    run_monitor()