# Transaction Correction and Visualization

This project is designed to correct transaction prices in an Excel spreadsheet and visualize the data using a bar chart. The provided Python script reads the original transaction data, applies a correction to the prices, and generates a bar chart to display the updated information.

## Project Overview

The project involves the following steps:
1. Load the transaction data from an Excel file (`transactions.xlsx`).
2. Apply a correction to the prices (reduce each price by 10%).
3. Insert the corrected prices into a new column.
4. Create a bar chart to visualize the product IDs, original prices, and corrected prices.
5. Save the updated data and chart to a new Excel file (`transactions2.xlsx`).

## Usage

1. Ensure you have an Excel file named `transactions.xlsx` with the following columns:
    - `transaction_id`
    - `product_id`
    - `price`
  
2. Place the Python script in the same directory as `transactions.xlsx`.

3. Run the script:
```bash
python app.py

## Source 
[Python Tutorial - Python Full Course for Beginners](https://www.youtube.com/watch?v=_uQrJ0TkZlc)