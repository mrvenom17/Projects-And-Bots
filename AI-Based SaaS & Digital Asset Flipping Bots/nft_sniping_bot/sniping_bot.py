# sniping_bot.py

import requests
from web3 import Web3
import logging
from config import OPENSEA_API_KEY, PRIVATE_KEY, WALLET_ADDRESS, NFT_CONTRACT_ADDRESSES, MAX_BUDGET, RARITY_THRESHOLD

# Configure logging
logging.basicConfig(filename='logs/nft_sniping.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_nft_data(contract_address):
    """Fetch NFT data from OpenSea API."""
    url = f"https://api.opensea.io/api/v1/assets?asset_contract_address={contract_address}&order_direction=asc&limit=50"
    headers = {"X-API-KEY": OPENSEA_API_KEY}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['assets']
        else:
            logging.error(f"Error fetching NFT data: {response.text}")
            return []
    except Exception as e:
        logging.error(f"Error fetching NFT data: {e}")
        return []

def buy_nft(web3, nft):
    """Buy an NFT using Web3."""
    contract_address = Web3.toChecksumAddress(nft['asset_contract']['address'])
    token_id = int(nft['token_id'])
    price = float(nft['sell_orders'][0]['current_price']) / 1e18  # Convert from wei to ETH
    
    if price > MAX_BUDGET:
        logging.info(f"NFT {token_id} is too expensive: {price} ETH")
        return
    
    # Example: Interact with NFT contract
    abi = [...]  # Replace with actual NFT contract ABI
    contract = web3.eth.contract(address=contract_address, abi=abi)
    
    tx = contract.functions.purchase(token_id).buildTransaction({
        'from': WALLET_ADDRESS,
        'value': Web3.toWei(price, 'ether'),
        'gas': 200000,
        'gasPrice': web3.eth.gas_price,
        'nonce': web3.eth.getTransactionCount(WALLET_ADDRESS)
    })
    
    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    logging.info(f"Purchased NFT {token_id}: {receipt}")

def run_sniping_bot():
    """Main function to run the NFT sniping bot."""
    logging.info("Starting NFT Sniping Bot...")
    web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))
    
    for contract_address in NFT_CONTRACT_ADDRESSES:
        assets = fetch_nft_data(contract_address)
        
        for asset in assets:
            rarity_score = analyze_rarity(asset)  # Replace with actual rarity analysis
            if rarity_score >= RARITY_THRESHOLD:
                logging.info(f"Found rare NFT: {asset['token_id']} with rarity score: {rarity_score}")
                buy_nft(web3, asset)

if __name__ == "__main__":
    run_sniping_bot()