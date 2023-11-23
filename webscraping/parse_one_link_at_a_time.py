import requests
from bs4 import BeautifulSoup
import pandas as pd
#proposed by chatgpt to get url content name
from urllib.parse import unquote

#source:https://medium.com/analytics-vidhya/web-scraping-a-wikipedia-table-into-a-dataframe-c52617e1f451

url="https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all tables with the specified class
tables = soup.find_all('table', {'class': 'wikitable'})

# Get page title from the URL
page_title = unquote(url.split('/')[-1])

# Initialize an empty list to store DataFrames for each table on the current page
dfs_per_page = []

# Iterate through the list of tables and convert each to a DataFrame
for i, table in enumerate(tables):
    df = pd.read_html(str(table), header=0)[0]  # Assuming headers are in the first row
    dfs_per_page.append(df)

    # Write each DataFrame to a separate CSV file
    filename = 'table_test_1.'+ str(i+1) + "_" + page_title + '.csv'
    with open(filename, 'w', newline='') as file:
        df.to_csv(file, index=False)

print("done")
