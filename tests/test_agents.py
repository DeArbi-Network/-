# test_agents.py
# Unit tests for AI agents

import pytest
from agents.arb_agent import ArbitrageAgent

@pytest.fixture
def agent():
    return ArbitrageAgent(config_path="agents/config.yaml")

def test_agent_initialization(agent):
    assert agent.trading_pairs is not None
    assert isinstance(agent.trading_pairs, list)

def test_find_arbitrage_opportunities(agent):
    market_data = [
        {"pair": "ETH/USD", "exchange": "A", "price": 1600},
        {"pair": "ETH/USD", "exchange": "B", "price": 1595},
    ]
    opportunity = agent.find_arbitrage_opportunities(market_data)
    assert opportunity is not None
