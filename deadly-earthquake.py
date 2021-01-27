# Web Scrapping Using BeautifulSoup
# List of deadly earthquakes since 1900

from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_deadly_earthquakes_since_1900'
r = requests.get(url)
html_content = r.text
html_soup = BeautifulSoup(html_content, 'html.parser')

earthquakes_table = html_soup.find_all('table', class_='wikitable')

earthquakes = []

for table in earthquakes_table:
    headers = []
    rows = table.find_all('tr')
    for header in table.find('tr').find_all('th'):
        headers.append(header.text)
    for row in table.find_all('tr')[1:]:
        values = []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if values:
            earthquake_dict = {headers[i]: values[i] for i in range(len(values))}
            earthquakes.append(earthquake_dict)

for earthquake in earthquakes:
    print(earthquake)

print(len(earthquakes))

import pandas as pd

df = pd.DataFrame.from_dict(earthquakes)
df.head()
df.columns
df.info()
df.to_csv('Deadly_Earthquake.csv')