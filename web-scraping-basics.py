import requests
from bs4 import BeautifulSoup
import pandas as pd

start_url = 'https://en.wikipedia.org/wiki/Tesla,_Inc.'

downloaded_html = requests.get(start_url)

soup = BeautifulSoup(downloaded_html.text, features="html.parser")

with open('downloaded_html', 'w', encoding="utf-8") as file:
    file.write(soup.prettify())
    
    full_table = soup.select('table.wikitable tbody')[0]
    table_head = full_table.select('tr th')
    table_rows = full_table.select('tr')
    table_columns = []
    table_data = []
    
    for index, element in enumerate(table_rows):
        column_label = element.get_text(separator=" ", strip=True)
        #column_label = column_label.replace(' ', '_')
        table_columns.append(column_label)
        
        if index > 0:
         row_list = []
         values = element.select('td')
         for value in values:
            row_list.append(value.text.strip())
         table_data.append(row_list)   
        print(column_label)
    print('---------------------------')
    df = pd.DataFrame(table_data, columns=table_columns)
    #print(table_columns)
    
    df
    #print(table_rows)
