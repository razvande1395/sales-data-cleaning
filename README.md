# sales-data-cleaning

This project provides a Python script to clean and preprocess raw sales datasets.  
It standardizes dates, trims whitespace, enforces numeric columns, removes invalid rows, and flags possible data issues.

## Requirements
- Python 3.12 (tested, should work on Python 3.8+)
- pandas (see requirements.txt)


## Features
- Strips extra spaces in text fields
- Converts and validates dates (`YYYY-MM-DD`)
- Ensures numeric columns are properly formatted
- Removes negative prices and duplicate rows
- Normalizes customer names
- Provides a summary log of cleaning steps

## Installation
git clone https://github.com/razvande1395/sales-data-cleaning.git

cd sales-data-cleaning

pip install -r requirements.txt

## Usage
python sales-cleaning.py

