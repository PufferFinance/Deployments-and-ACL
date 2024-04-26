# convert_to_markdown.py
import json
import sys

def convert_to_markdown(input_file, output_file):
    try:
        # Read the transaction data from the JSON file
        with open(input_file, 'r') as file:
            data = json.load(file)
        
        transactions = data.get('result', [])
        markdown_lines = ["# Transaction Report\n"]

        for tx in transactions:
            markdown_lines.append(f"## Transaction Hash: {tx['hash']}")
            markdown_lines.append(f"- **Block Number**: {tx['blockNumber']}")
            markdown_lines.append(f"- **From**: {tx['from']}")
            markdown_lines.append(f"- **To**: {tx['to']}")
            markdown_lines.append(f"- **Value**: {tx['value']} wei")
            markdown_lines.append(f"- **Confirmations**: {tx['confirmations']}\n")

        # Writing the markdown data to a file
        with open(output_file, 'w') as file:
            file.write("\n".join(markdown_lines))
        print("Markdown file created successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_to_markdown.py <INPUT_JSON_FILE> <OUTPUT_MD_FILE>")
    else:
        INPUT_FILE = sys.argv[1]
        OUTPUT_FILE = sys.argv[2]
        convert_to_markdown(INPUT_FILE, OUTPUT_FILE)
