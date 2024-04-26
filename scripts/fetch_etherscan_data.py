# fetch_etherscan_data.py
import requests
import json
import sys

def fetch_transactions(api_key, address, output_file):
    url = "https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "asc",
        "apikey": api_key
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        transactions = response.json()
        # Write the data to a JSON file
        with open(output_file, 'w') as file:
            json.dump(transactions, file)
        print("Transactions fetched successfully.")
    else:
        print("Failed to fetch transactions, Status code:", response.status_code)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python fetch_etherscan_data.py <API_KEY> <ETH_ADDRESS> <OUTPUT_FILE>")
    else:
        API_KEY = sys.argv[1]
        ADDRESS = sys.argv[2]
        OUTPUT_FILE = sys.argv[3]
        fetch_transactions(API_KEY, ADDRESS, OUTPUT_FILE)
