# Ethereum Contract Interactor

This project is a Python application that interacts with a specific Ethereum Goerli Test Network's smart contract. It uses the Web3.py library to connect to the Goerli Test Network, fetch data from the contract and display information about given addresses.

## Features

- Fetches and displays token IDs associated with a given address
- Calculates and displays the remaining time until each token's license expires
- Finds and displays the token with the longest remaining time

## Requirements

- Python 3.6 or higher
- Web3.py

The `datetime` and `config` modules are part of the Python Standard Library, so you don't need to install them.

## Installation

1. Clone this repository.
2. Install the required Python packages using pip:

    ```
    pip install web3
    ```

3. Run the main script:

    ```
    python main.py
    ```
