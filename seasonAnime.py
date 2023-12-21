# -*- coding: cp1251 -*-
from bs4 import BeautifulSoup
import requests
import sys

sys.stdout.reconfigure(encoding="utf-8")

url ="https://animego.org/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
animeNames = soup.findAll('div', class_='animes-grid-item-body card-body px-0')
animeFiltered = []
print('Season anime:')
for data in animeNames:
    if data is not None:
        animeFiltered.append(data.text)
for data in animeFiltered:
    print(data)