# deploy.py
# Script to deploy smart contracts for the DeArbi Network

from web3 import Web3
import json
import os

# Load environment variables
INFURA_URL = os.getenv("INFURA_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
DEPLOYER_ADDRESS = os.getenv("DEPLOYER_ADDRESS")

# Connect to Ethereum network
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Load compiled contract ABI and bytecode
def load_contract(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Deploy a contract
def deploy_contract(contract_json, deployer_address, private_key):
    abi = contract_json["abi"]
    bytecode = contract_json["bytecode"]
    contract = web3.eth.contract(abi=abi, bytecode=bytecode)
    transaction = contract.constructor().buildTransaction({
        "from": deployer_address,
        "nonce": web3.eth.getTransactionCount(deployer_address),
        "gas": 5000000,
        "gasPrice": web3.toWei("50", "gwei"),
    })
    signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Transaction hash: {web3.toHex(tx_hash)}")
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Contract deployed at: {tx_receipt.contractAddress}")
    return tx_receipt.contractAddress

# Example usage
if __name__ == "__main__":
    arb_token_contract = load_contract("contracts/compiled/ArbToken.json")
    arb_agent_contract = load_contract("contracts/compiled/ArbAgent.json")

    deploy_contract(arb_token_contract, DEPLOYER_ADDRESS, PRIVATE_KEY)
    deploy_contract(arb_agent_contract, DEPLOYER_ADDRESS, PRIVATE_KEY)
