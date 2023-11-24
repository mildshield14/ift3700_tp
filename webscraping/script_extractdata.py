import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import unquote
from urllib.parse import unquote, urlsplit
import re

# Read URLs from the PHP file
with open("view.php", 'r') as file:
    php_code = file.read()

# Extract URLs using regex
urls = re.findall(r'"ulnk_url":"(https://en\.wikipedia\.org/wiki/[^"]+)"', php_code)

# Initialize a counter for file names
count = 1

# Iterate through the URLs
for url in urls:
    response = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all tables with the specified class
    tables = soup.find_all('table', {'class': 'wikitable'})

     # Get page title from the URL
    page_title = unquote(urlsplit(url).path.split('/')[-1])

    # Initialize an empty list to store DataFrames for each table on the current page
    dfs_per_page = []

    # Iterate through the list of tables and convert each to a DataFrame
    for i, table in enumerate(tables):
        df = pd.read_html(str(table), header=0)[0]  # Assuming headers are in the first row
        dfs_per_page.append(df)

        # Create a folder for each page if it doesn't exist
        page_folder = f'csv_rawdata/{count}.{page_title}'
        os.makedirs(page_folder, exist_ok=True)

        # Write each DataFrame to a separate CSV file
        filename = f'{page_folder}/{count}.{i + 1} table.csv'
        with open(filename, 'w', newline='') as file:
            df.to_csv(file, index=False)


    # Increment the counter
    count += 1

print("done")
