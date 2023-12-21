# -*- coding: cp1251 -*-
from bs4 import BeautifulSoup
import requests
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk

sys.stdout.reconfigure(encoding="utf-8")
root = tk.Tk()
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title('AnimeCollector')

url ="https://animego.org/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
label = tk.Label()

def collector():
    animeCollection = ""
    # Monday
    animeNamesMonday = soup.findAll('div', id='slide-toggle-monday')
    animeFilteredMonday = []
    animeCollection += "Monday anime:\n"
    for data in animeNamesMonday:
        data = data.findAll('div',class_='media-body')
        for animeFilteredMonday in data:
            animeCollection += '\n' + animeFilteredMonday.get_text()
    # Thuesday
    animeNamesTuesday = soup.findAll('div', id='slide-toggle-tuesday')
    animeFilteredTuesday = []
    animeCollection += '\n\nTuesday anime:'
    for data in animeNamesTuesday:
        data = data.findAll('div',class_='media-body')
        for animeFilteredTuesday in data:
            animeCollection += '\n' + animeFilteredTuesday.get_text()
    # Wednesday
    animeNamesWednesday = soup.findAll('div', id='slide-toggle-wednesday')
    animeFilteredWednesday = []
    animeCollection += '\n\nWednesday anime:'
    for data in animeNamesWednesday:
        data = data.findAll('div',class_='media-body')
        for animeFilteredWednesday in data:
            animeCollection +='\n' + animeFilteredWednesday.get_text()
    # Thursday
    animeNamesThursday = soup.findAll('div', id='slide-toggle-thursday')
    animeFilteredThursday = []
    animeCollection += '\n\nThursday anime:'
    for data in animeNamesThursday:
        data = data.findAll('div',class_='media-body')
        for animeFilteredThursday in data:
            animeCollection +='\n' + animeFilteredThursday.get_text()
    # Friday
    animeNamesFriday = soup.findAll('div', id='slide-toggle-friday')
    animeFilteredFriday = []
    animeCollection += '\n\nFriday anime:'
    for data in animeNamesFriday:
        data = data.findAll('div',class_='media-body')
        for animeFilteredFriday in data:
            animeCollection +='\n' + animeFilteredFriday.get_text()
    # Saturday
    animeNamesSaturday = soup.findAll('div', id='slide-toggle-saturday')
    animeFilteredSaturday = []
    animeCollection += '\n\nSaturday anime:'
    for data in animeNamesSaturday:
        data = data.findAll('div',class_='media-body')
        for animeFilteredSaturday in data:
            animeCollection +='\n' + animeFilteredSaturday.get_text()
    # Sunday
    animeNamesSunday = soup.findAll('div', id='slide-toggle-sunday')
    animeFilteredSunday = []
    animeCollection += '\n\nSunday anime:'
    for data in animeNamesSunday:
        data = data.findAll('div',class_='media-body')
        for animeFilteredSunday in data:
            animeCollection +='\n' + animeFilteredSunday.get_text()

    label.config(text=animeCollection)
label.pack(side=LEFT,expand=True)
def clear():
    label.config(text="")
animeButton = ttk.Button(
   root, 
   text="Collect", 
   command=collector
)

animeButton.pack(
    ipadx=5,
    ipady=5
)
animeClearButton = ttk.Button(
    root,
    text="Clear",
    command=clear
)
animeClearButton.pack(
    ipadx=5,
    ipady=5
)

root.mainloop()