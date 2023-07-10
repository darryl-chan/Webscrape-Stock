# import re
# import json
# import csv
# from io import StringIO
# from bs4 import BeautifulSoup
# import requests

# stock_url = "https://sg.finance.yahoo.com/quote/{}/history"

# params = {
#     'range': '10y',
#     'interval': '1d',
#     'events': 'history'   
# }

# # response = requests.get(stock_url.format('C6L.SI'), params=params)
# # file = StringIO(response.text)
# # reader = csv.reader(file)
# # data = list(reader)
# # for row in data:
# #     print(row)

# response = requests.get(stock_url.format('C6L.SI'))
# soup = BeautifulSoup(response.content, "html.parser")
# table = soup.find('table', attrs={"class": "W(100%) M(0)"})
# print(table)

import requests
from bs4 import BeautifulSoup

url = "https://sg.finance.yahoo.com/quote/C6L.SI/history?p=C6L.SI"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element by class
table = soup.find('div', class_='Pb(10px) 0vx(a) W(100%)')

# Extract the table rows
rows = table.find_all('tr')

# Iterate over the rows and print the data in each cell
for row in rows:
    cells = row.find_all('td')
    for cell in cells:
        print(cell.text)





