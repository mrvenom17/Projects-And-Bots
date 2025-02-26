# utils.py

def calculate_floor_price(nft_data):
    """Calculate the floor price of an NFT collection."""
    prices = [float(asset['sell_orders'][0]['current_price']) / 1e18 for asset in nft_data if asset['sell_orders']]
    return min(prices) if prices else None