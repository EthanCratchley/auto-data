# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to fetch and extract a table from a webpage
def fetch_and_extract(url, table_class):
    # Headers to mimic a real browser visit to the site, which can help avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Send a GET request to the specified URL with the headers
    page = requests.get(url, headers=headers)

    # Initialize the data variable to None. It will hold the extracted table data if found
    data = None

    # Check if the GET request was successful (status code 200)
    if page.status_code == 200:
        # Parse the HTML content of the page with Beautiful Soup
        soup = BeautifulSoup(page.text, 'html.parser')

        # Search for all tables with the specified class name
        table = soup.find_all('table', {'class': table_class})

        # If a table is found
        if table:
            # Convert the table HTML into a pandas DataFrame
            data = pd.read_html(str(table))[0]

            # Print confirmation and display the head of the DataFrame
            print("Table found!")
            print(data.head())

        else:
            # Print a message if no table with the specified class name is found
            print("No table found with the specified class name.")

    else:
        # Print an error message if the GET request was not successful
        print(f"Failed to retrieve content. Status code: {page.status_code}")

    # Return the extracted table data as a pandas DataFrame, or None if not found
    return data

# Test the function with a specific URL and table class name
# This URL and class name should be updated to target different webpages/tables as needed
url = 'https://www.wsj.com/market-data/quotes/TSLA/financials/annual/balance-sheet'
table_class = 'cr_dataTable'

# Call the fetch_and_extract function and store the extracted data in the 'data' variable
data = fetch_and_extract(url, table_class)
