# -*- coding: cp1251 -*-
from bs4 import BeautifulSoup
import requests
import sys

sys.stdout.reconfigure(encoding="utf-8")

url ="https://dzen.ru/retaility.ru"
page = requests.get(url)
animeNames = []
soup = BeautifulSoup(page.text, "html.parser")
animeNames = soup.findAll()
animeFiltered = []
print(soup)