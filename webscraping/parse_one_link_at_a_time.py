import requests
from bs4 import BeautifulSoup
import pandas as pd
#proposed by chatgpt to get url content name
from urllib.parse import unquote

#source:https://medium.com/analytics-vidhya/web-scraping-a-wikipedia-table-into-a-dataframe-c52617e1f451

url="https://en.wikipedia.org/wiki/List_of_countries_by_spending_on_education_as_percentage_of_GDP"

response=requests.get(url)
soup=BeautifulSoup(response.content, 'html.parser')

#find table 
table=soup.find('table',{'class':"wikitable"})

df=pd.read_html(str(table))
# convert list to dataframe
df=pd.DataFrame(df[0])

#proposed by chatgpt to get url content name
page_title = unquote(url.split('/')[-1])

filename = 'table' + str(40) + "_" + page_title + '.csv'
#write in files:
with open(filename, 'a', newline='') as file:
    df.to_csv(file, index=False, header=not file.tell())
