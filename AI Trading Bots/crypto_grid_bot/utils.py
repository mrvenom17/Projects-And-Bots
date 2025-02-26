# utils.py

def fetch_balance(exchange, symbol):
    """Fetch account balance for a specific asset."""
    balance = exchange.fetch_balance()
    return balance['total'][symbol]

def log_performance():
    """Log bot performance metrics (e.g., PnL)."""
    # Implement logic to calculate profit/loss
    pass