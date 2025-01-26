# test_transactions.py
# Script to test interactions with deployed smart contracts

from web3 import Web3
import json
import os

# Load environment variables
INFURA_URL = os.getenv("INFURA_URL")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
ACCOUNT_ADDRESS = os.getenv("ACCOUNT_ADDRESS")

# Connect to Ethereum network
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Load contract ABI
def load_contract_abi(file_path):
    with open(file_path, "r") as file:
        return json.load(file)["abi"]

# Example: Test transferring tokens
if __name__ == "__main__":
    abi = load_contract_abi("contracts/compiled/ArbToken.json")
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

    tx = contract.functions.transfer(
        "0xRecipientAddressHere",
        web3.toWei(10, "ether")
    ).buildTransaction({
        "from": ACCOUNT_ADDRESS,
        "nonce": web3.eth.getTransactionCount(ACCOUNT_ADDRESS),
        "gas": 200000,
        "gasPrice": web3.toWei("50", "gwei"),
    })

    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Transaction hash: {web3.toHex(tx_hash)}")
