import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_and_extract(url, table_class):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    data = None

    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find_all('table', {'class': table_class})

        if table:
            data = pd.read_html(str(table))[0]
            print("Table found!")
            print(data.head())
        else:
            print("No table found with the specified class name.")
    else:
        print(f"Failed to retrieve content. Status code: {page.status_code}")

    return data

# Test the function with your specific URL and table class name
url = 'https://www.wsj.com/market-data/quotes/TSLA/financials/annual/balance-sheet'
table_class = 'cr_dataTable'
data = fetch_and_extract(url, table_class)


