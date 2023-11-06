import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
import re
#proposed by chatgpt to get url content name
from urllib.parse import unquote

#source:https://medium.com/analytics-vidhya/web-scraping-a-wikipedia-table-into-a-dataframe-c52617e1f451

#url="https://en.wikipedia.org/wiki/List_of_sovereign_states_by_Internet_connection_speeds"

count=0


with open("view.php", 'r') as file:
    php_code=file.read()

urls = re.findall(r'"ulnk_url":"(https://en\.wikipedia\.org/wiki/[\w()]+)"', php_code)

for url in (urls):
    response=requests.get(url)
    time.sleep(1)
    soup=BeautifulSoup(response.content, 'html.parser')

    #find table 
    table=soup.find('table',{'class':"wikitable"})

    df=pd.read_html(str(table))
    # convert list to dataframe
    df=pd.DataFrame(df[0])


    count=count+1

    #proposed by chatgpt to get url content name
    page_title = unquote(url.split('/')[-1])

    filename = 'table' + str(count) + "_" + page_title + '.csv'
    #write in files:
    with open(filename, 'a', newline='') as file:
        df.to_csv(file, index=False, header=not file.tell())


print("done")