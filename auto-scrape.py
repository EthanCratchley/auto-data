import requests
from bs4 import BeautifulSoup

# Fetch the web page
url = 'https://www.example.com'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data (modify this according to the data you need)
data = soup.find_all('tag_name', class_='class_name')

# Print or process the data
for item in data:
    print(item.text)