# conftest.py
# Common fixtures for pytest

import pytest
from web3 import Web3

@pytest.fixture
def web3():
    """Returns a Web3 instance connected to the local blockchain."""
    return Web3(Web3.HTTPProvider("http://localhost:8545"))

@pytest.fixture
def deployer_address():
    """Returns the deployer's address."""
    return "0xYourDeployerAddressHere"
