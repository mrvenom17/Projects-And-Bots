# data_fetcher.py

import yfinance as yf
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from config import ALPHA_VANTAGE_API_KEY, STOCKS_TO_MONITOR

def fetch_stock_data(stock_symbol):
    """Fetch historical stock data using Yahoo Finance."""
    stock_data = yf.download(stock_symbol, period="1y", interval="1d")
    return stock_data

def fetch_real_time_data(stock_symbol):
    """Fetch real-time stock data using Alpha Vantage."""
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
    data, _ = ts.get_intraday(symbol=stock_symbol, interval='1min', outputsize='full')
    return data

def run_data_fetcher():
    """Main function to fetch stock data."""
    for stock in STOCKS_TO_MONITOR:
        historical_data = fetch_stock_data(stock)
        real_time_data = fetch_real_time_data(stock)
        
        # Save data for further processing
        historical_data.to_csv(f"data/{stock}_historical.csv")
        real_time_data.to_csv(f"data/{stock}_real_time.csv")

if __name__ == "__main__":
    run_data_fetcher()