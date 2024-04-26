# Transaction Reports

## Overview

This directory contains generated reports of blockchain transactions associated with Puffer Protocol smart contracts. These reports are formatted in Markdown for easy readability and accessibility.

## Contents

- **transactions.md**: A Markdown file that lists recent transactions, including details such as transaction hashes, amounts transferred, decoded data, and the addresses involved.

## Purpose

These reports provide transparency and allow for easy tracking of all transactions made by Puffer smart contracts. They serve as an audit trail for developers, stakeholders, and external auditors.

This can be particularly useful for:
- Auditing purposes.
- Verifying contract interactions.
- Tracking operational activities.

## Generating Reports

Reports are automatically generated through a scheduled script that fetches data from Etherscan and formats it into Markdown. Ensure that the script `fetch_etherscan_data.py` and `convert_to_markdown.py` are correctly configured to run as scheduled.
