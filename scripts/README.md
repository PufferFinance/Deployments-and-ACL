# Usage

These scripts are used in the recurring Github actions, such as to fetch data from Etherscan and format it into Markdown. The scripts are scheduled to run at regular intervals to ensure that the transaction reports are up-to-date and accurate.




# fetch_etherscan_data.py
```
python fetch_etherscan_data.py etherscan_API_Key 0xYourEthereumAddress logs/transactions.json
```


# convert_to_markdown.py
```
python convert_to_markdown.py logs/transactions.json logs/transactions.md
```