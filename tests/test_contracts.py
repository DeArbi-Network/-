# test_contracts.py
# Unit tests for smart contracts

from web3 import Web3
import pytest

@pytest.fixture
def web3():
    return Web3(Web3.HTTPProvider("http://localhost:8545"))

@pytest.fixture
def contract(web3):
    abi = [{"constant": True, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}], "type": "function"}]
    return web3.eth.contract(address="0x0000000000000000000000000000000000000000", abi=abi)

def test_contract_connection(contract):
    assert contract.functions.symbol().call() == "ARBOT"
