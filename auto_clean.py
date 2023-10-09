from auto_scrape import fetch_and_extract
import pandas as pd
import numpy as np

# Specify URL and table class name
url = 'https://www.wsj.com/market-data/quotes/TSLA/financials/annual/balance-sheet'
table_class = 'cr_dataTable'

# Fetch and extract data
data = fetch_and_extract(url, table_class)

if data is not None:
    # Clean the data if needed
    # For example, remove NaN values, convert data types, etc.

    # Save to CSV
    data.to_csv('data_assets.csv', index=False)
    print("Data saved to data.csv")
else:
    print("No data to clean and save.")


def clean_data(file_name, rows_to_drop):
    try:
        df = pd.read_csv(file_name)
        print(f"Original DataFrame:\n{df}\n")

        # Replace '-' with NaN
        df.replace('-', np.nan, inplace=True)

        # Drop specified rows
        df.drop(index=rows_to_drop, inplace=True)

        # Drop columns beyond the 5th index
        df.drop(columns=df.columns[6:], inplace=True)

        # Drop any remaining rows where all values are NaN
        df.dropna(how='all', inplace=True)

        # Optional: Drop any remaining rows where all values are NaN across a specific set of columns
        df.dropna(subset=df.columns[1:], how='all', inplace=True)

        print(f"Cleaned DataFrame:\n{df}\n")
        return df

    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred while processing {file_name}: {e}")


# Specify the rows to drop for each dataset
rows_to_drop_assets = [1,4,10,11,18,20,26,29,32,35,36,37,38,39,40,
                       41,42,43,45,52,56]
rows_to_drop_liab = [8,22,27,29,33,35,36,37,38,39,44,45,46,47,
                     49,50]

cleaned_assets = clean_data('data_assets.csv', rows_to_drop_assets)
cleaned_liab = clean_data('data_liab.csv', rows_to_drop_liab)

if cleaned_assets is not None:
    cleaned_assets.to_csv('cleaned_assets.csv', index=False)

if cleaned_liab is not None:
    cleaned_liab.to_csv('cleaned_liab.csv', index=False)