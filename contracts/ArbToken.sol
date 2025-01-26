// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// ERC20 token contract for $ARBOT
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract ArbToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("ArbToken", "ARBOT") {
        _mint(msg.sender, initialSupply);
    }
}
