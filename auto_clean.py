# Importing necessary libraries and modules
from auto_scrape import fetch_and_extract
import pandas as pd
import numpy as np

# URL of the webpage containing the table to be scraped
url = 'https://www.wsj.com/market-data/quotes/TSLA/financials/annual/balance-sheet'

# The class name of the table to be scraped
table_class = 'cr_dataTable'

# Call the fetch_and_extract function to scrape data from the given URL and table class
data = fetch_and_extract(url, table_class)

# Check if data was successfully scraped
if data is not None:
    # If data is found, save it as a CSV file
    data.to_csv('data_assets.csv', index=False)
    print("Data saved to data.csv")
else:
    # If no data is found, print a message
    print("No data to clean and save.")

# Function to clean the scraped data
def clean_data(file_name, rows_to_drop):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_name)
        print(f"Original DataFrame:\n{df}\n")

        # Replace '-' characters with NaN to allow for dropping them later
        df.replace('-', np.nan, inplace=True)

        # Drop specific rows based on the provided indices
        df.drop(index=rows_to_drop, inplace=True)

        # Drop columns beyond the 5th index to clean up the DataFrame
        df.drop(columns=df.columns[6:], inplace=True)

        # Drop rows where all values are NaN
        df.dropna(how='all', inplace=True)

        # Optionally, drop rows where all values in specific columns are NaN
        df.dropna(subset=df.columns[1:], how='all', inplace=True)

        # Print the cleaned DataFrame
        print(f"Cleaned DataFrame:\n{df}\n")
        return df

    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred while processing {file_name}: {e}")

# Indices of rows to be dropped for assets and liabilities
rows_to_drop_assets = [1,4,10,11,18,20,26,29,32,35,36,37,38,39,40, 41,42,43,45,52,56]
rows_to_drop_liab = [8,22,27,29,33,35,36,37,38,39,44,45,46,47, 49,50]

# Cleaning the data for assets and liabilities
cleaned_assets = clean_data('data_assets.csv', rows_to_drop_assets)
cleaned_liab = clean_data('data_liab.csv', rows_to_drop_liab)

# Save the cleaned data to new CSV files
if cleaned_assets is not None:
    cleaned_assets.to_csv('cleaned_assets.csv', index=False)

if cleaned_liab is not None:
    cleaned_liab.to_csv('cleaned_liab.csv', index=False)
