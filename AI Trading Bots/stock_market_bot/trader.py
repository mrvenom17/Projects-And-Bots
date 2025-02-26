# trader.py

import alpaca_trade_api as tradeapi
import logging
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, BUDGET, RISK_THRESHOLD, STOCKS_TO_MONITOR

# Configure logging
logging.basicConfig(filename='logs/trader.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def setup_alpaca():
    """Set up connection to Alpaca API."""
    api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url='https://paper-api.alpaca.markets')
    return api

def execute_trade(api, stock_symbol, predicted_price, current_price):
    """Execute a trade based on predicted price movement."""
    account = api.get_account()
    available_cash = float(account.cash)
    risk_amount = available_cash * RISK_THRESHOLD
    
    if predicted_price > current_price:
        # Buy signal
        quantity = int(risk_amount / current_price)
        api.submit_order(
            symbol=stock_symbol,
            qty=quantity,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
        logging.info(f"Bought {quantity} shares of {stock_symbol}")
    elif predicted_price < current_price:
        # Sell signal
        position = api.get_position(stock_symbol)
        if position:
            api.submit_order(
                symbol=stock_symbol,
                qty=int(position.qty),
                side='sell',
                type='market',
                time_in_force='gtc'
            )
            logging.info(f"Sold {position.qty} shares of {stock_symbol}")

def run_trader():
    """Main function to run the trader."""
    api = setup_alpaca()
    
    for stock in STOCKS_TO_MONITOR:
        current_price = api.get_latest_trade(stock).price
        predicted_price = predict_price_movement(stock)  # Replace with actual prediction logic
        
        execute_trade(api, stock, predicted_price, current_price)

if __name__ == "__main__":
    run_trader()