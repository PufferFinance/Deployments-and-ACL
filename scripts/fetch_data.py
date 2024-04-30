# fetch_etherscan_data.py
import requests
import json
import sys






# def fetch_transactions(api_key, address, output_file):
#     url = "https://api.etherscan.io/api"
#     params = {
#         "module": "account",
#         "action": "txlist",
#         "address": address,
#         "startblock": 0,
#         "endblock": 99999999,
#         "sort": "asc",
#         "apikey": api_key
#     }
    
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         transactions = response.json()
#         # Write the data to a JSON file
#         with open(output_file, 'w') as file:
#             json.dump(transactions, file)
#         print("Transactions fetched successfully.")
#     else:
#         print("Failed to fetch transactions, Status code:", response.status_code)



def decode_input(payload, output_file):
    payload_json = json.loads(payload)
    # Write the data to a JSON file
    with open(output_file, 'w') as file:
        json.dump(payload_json, file)

    print("Transactions fetched successfully: %s " %payload_json)




if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python fetch_etherscan_data.py JSON_PAYLOAD <OUTPUT_FILE>")
    else:
        PAYLOAD = sys.argv[1]
        # ADDRESS = sys.argv[2]
        OUTPUT_FILE = sys.argv[2]

        decode_input(PAYLOAD, OUTPUT_FILE)
        # fetch_transactions(API_KEY, ADDRESS, OUTPUT_FILE)
