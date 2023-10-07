from auto_scrape import fetch_and_extract
import pandas as pd

# Specify URL and table class name
url = 'https://www.wsj.com/market-data/quotes/TSLA/financials/annual/balance-sheet'
table_class = 'cr_dataTable'

# Fetch and extract data
data = fetch_and_extract(url, table_class)

if data is not None:
    # Clean the data if needed
    # For example, remove NaN values, convert data types, etc.

    # Save to CSV
    data.to_csv('data_0.csv', index=False)
    print("Data saved to data.csv")
else:
    print("No data to clean and save.")
