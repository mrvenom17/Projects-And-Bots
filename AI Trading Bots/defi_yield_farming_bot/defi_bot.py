# defi_bot.py

from web3 import Web3
import logging
from config import PRIVATE_KEY, WALLET_ADDRESS, INFURA_PROJECT_ID, AAVE_CONTRACT_ADDRESS, COMPOUND_CONTRACT_ADDRESS, UNISWAP_ROUTER_ADDRESS

# Configure logging
logging.basicConfig(filename='logs/defi_bot.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def setup_web3():
    """Set up connection to Ethereum blockchain."""
    web3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}"))
    if not web3.isConnected():
        logging.error("Failed to connect to Ethereum node.")
        return None
    return web3

def stake_in_aave(web3, amount):
    """Stake tokens in Aave protocol."""
    abi = [...]  # Replace with actual Aave contract ABI
    contract = web3.eth.contract(address=AAVE_CONTRACT_ADDRESS, abi=abi)
    
    tx = contract.functions.deposit(
        Web3.toChecksumAddress("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"),  # WETH token
        amount
    ).buildTransaction({
        'from': WALLET_ADDRESS,
        'gas': 200000,
        'gasPrice': web3.eth.gas_price,
        'nonce': web3.eth.getTransactionCount(WALLET_ADDRESS)
    })
    
    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    logging.info(f"Staked in Aave: {receipt}")

def lend_in_compound(web3, amount):
    """Lend tokens in Compound protocol."""
    abi = [...]  # Replace with actual Compound contract ABI
    contract = web3.eth.contract(address=COMPOUND_CONTRACT_ADDRESS, abi=abi)
    
    tx = contract.functions.mint(amount).buildTransaction({
        'from': WALLET_ADDRESS,
        'gas': 200000,
        'gasPrice': web3.eth.gas_price,
        'nonce': web3.eth.getTransactionCount(WALLET_ADDRESS)
    })
    
    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    logging.info(f"Lent in Compound: {receipt}")

def provide_liquidity_in_uniswap(web3, token_a, token_b, amount_a, amount_b):
    """Provide liquidity in Uniswap."""
    abi = [...]  # Replace with actual Uniswap router ABI
    contract = web3.eth.contract(address=UNISWAP_ROUTER_ADDRESS, abi=abi)
    
    tx = contract.functions.addLiquidity(
        token_a,
        token_b,
        amount_a,
        amount_b,
        0,
        0,
        WALLET_ADDRESS,
        int(time.time()) + 10 * 60  # Deadline: 10 minutes
    ).buildTransaction({
        'from': WALLET_ADDRESS,
        'gas': 300000,
        'gasPrice': web3.eth.gas_price,
        'nonce': web3.eth.getTransactionCount(WALLET_ADDRESS)
    })
    
    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    logging.info(f"Provided liquidity in Uniswap: {receipt}")

def run_defi_bot():
    """Main function to run the DeFi bot."""
    logging.info("Starting DeFi Yield Farming Bot...")
    web3 = setup_web3()
    
    if web3:
        stake_in_aave(web3, Web3.toWei(1, 'ether'))  # Stake 1 ETH in Aave
        lend_in_compound(web3, Web3.toWei(1, 'ether'))  # Lend 1 ETH in Compound
        provide_liquidity_in_uniswap(web3, "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", Web3.toWei(1, 'ether'), Web3.toWei(2000, 'ether'))  # Provide 1 ETH and 2000 USDC in Uniswap

if __name__ == "__main__":
    run_defi_bot()