# grid_trading.py

import ccxt
import time
import logging
from config import API_KEY, API_SECRET, SYMBOL, GRID_LEVELS, LOWER_PRICE, UPPER_PRICE, ORDER_SIZE

# Configure logging
logging.basicConfig(filename='logs/grid_bot.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Binance exchange
exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
})

def calculate_grid_prices():
    """Calculate grid prices between lower and upper bounds."""
    price_range = UPPER_PRICE - LOWER_PRICE
    step = price_range / GRID_LEVELS
    return [LOWER_PRICE + i * step for i in range(GRID_LEVELS + 1)]

def place_orders(grid_prices):
    """Place buy/sell orders at grid levels."""
    try:
        for price in grid_prices:
            # Place buy order below current price
            if price < exchange.fetch_ticker(SYMBOL)['last']:
                exchange.create_limit_buy_order(SYMBOL, ORDER_SIZE, price)
                logging.info(f"Placed BUY order at {price}")
            
            # Place sell order above current price
            else:
                exchange.create_limit_sell_order(SYMBOL, ORDER_SIZE, price)
                logging.info(f"Placed SELL order at {price}")
    except Exception as e:
        logging.error(f"Error placing orders: {e}")

def cancel_all_orders():
    """Cancel all open orders."""
    try:
        open_orders = exchange.fetch_open_orders(SYMBOL)
        for order in open_orders:
            exchange.cancel_order(order['id'], SYMBOL)
            logging.info(f"Cancelled order ID: {order['id']}")
    except Exception as e:
        logging.error(f"Error cancelling orders: {e}")

def run_bot():
    """Main function to run the grid trading bot."""
    logging.info("Starting Grid Trading Bot...")
    grid_prices = calculate_grid_prices()
    
    while True:
        try:
            # Cancel existing orders before placing new ones
            cancel_all_orders()
            
            # Place new grid orders
            place_orders(grid_prices)
            
            # Wait for a while before recalculating
            time.sleep(60)
        except KeyboardInterrupt:
            logging.info("Bot stopped by user.")
            break
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    run_bot()