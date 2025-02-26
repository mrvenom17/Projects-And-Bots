# forex_bot.py

import MetaTrader5 as mt5
import pandas as pd
import talib
from config import MT4_LOGIN, MT4_PASSWORD, MT4_SERVER, SYMBOL, TIMEFRAME, LOT_SIZE, STOP_LOSS, TAKE_PROFIT
import logging

# Configure logging
logging.basicConfig(filename='logs/forex_bot.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_mt5():
    """Initialize MetaTrader 5."""
    if not mt5.initialize(login=MT4_LOGIN, password=MT4_PASSWORD, server=MT4_SERVER):
        logging.error("Failed to initialize MetaTrader 5")
        return False
    return True

def get_market_data():
    """Fetch live market data."""
    rates = mt5.copy_rates_from_pos(SYMBOL, getattr(mt5, f"TIMEFRAME_{TIMEFRAME}"), 0, 100)
    data = pd.DataFrame(rates)
    data['time'] = pd.to_datetime(data['time'], unit='s')
    return data

def generate_signal(data):
    """Generate buy/sell signals using technical indicators."""
    data['RSI'] = talib.RSI(data['close'], timeperiod=14)
    data['MACD'], _, _ = talib.MACD(data['close'], fastperiod=12, slowperiod=26, signalperiod=9)
    
    if data['RSI'].iloc[-1] < 30 and data['MACD'].iloc[-1] > 0:
        return 'BUY'
    elif data['RSI'].iloc[-1] > 70 and data['MACD'].iloc[-1] < 0:
        return 'SELL'
    return None

def place_order(signal):
    """Place a trade based on the signal."""
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": SYMBOL,
        "volume": LOT_SIZE,
        "type": mt5.ORDER_BUY if signal == 'BUY' else mt5.ORDER_SELL,
        "price": mt5.symbol_info_tick(SYMBOL).ask if signal == 'BUY' else mt5.symbol_info_tick(SYMBOL).bid,
        "sl": mt5.symbol_info_tick(SYMBOL).ask - STOP_LOSS * 0.0001 if signal == 'BUY' else mt5.symbol_info_tick(SYMBOL).bid + STOP_LOSS * 0.0001,
        "tp": mt5.symbol_info_tick(SYMBOL).ask + TAKE_PROFIT * 0.0001 if signal == 'BUY' else mt5.symbol_info_tick(SYMBOL).bid - TAKE_PROFIT * 0.0001,
        "deviation": 20,
        "magic": 123456,
        "comment": "AI Forex Bot",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    
    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        logging.error(f"Order failed: {result.comment}")
    else:
        logging.info(f"Order placed successfully: {result}")

def run_bot():
    """Main function to run the Forex trading bot."""
    if not initialize_mt5():
        return
    
    while True:
        try:
            data = get_market_data()
            signal = generate_signal(data)
            
            if signal:
                logging.info(f"Signal detected: {signal}")
                place_order(signal)
            
            time.sleep(60)  # Wait before checking again
        except KeyboardInterrupt:
            logging.info("Bot stopped by user.")
            break
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    run_bot()