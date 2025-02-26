# utils.py

def calculate_risk(current_price, budget, risk_threshold):
    """Calculate the maximum amount to risk per trade."""
    return budget * risk_threshold / current_price