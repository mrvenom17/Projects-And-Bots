# config.py

API_KEY = 'your_binance_api_key'
API_SECRET = 'your_binance_api_secret'

# Grid Trading Parameters
SYMBOL = 'BTC/USDT'  # Trading pair
GRID_LEVELS = 10     # Number of grid levels
LOWER_PRICE = 20000  # Lower bound of grid
UPPER_PRICE = 30000  # Upper bound of grid
ORDER_SIZE = 0.001   # Amount of BTC per order