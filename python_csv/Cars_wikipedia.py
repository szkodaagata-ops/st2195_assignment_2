#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/w/index.php?title=Comma-separated_values&diff=prev&oldid=1075295751"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

html = response.text

soup = BeautifulSoup(html, "html.parser")

find_all_pre = soup.find_all("pre")

csv_text = None

for tag in find_all_pre:
    text = tag.get_text()
    if text.startswith("Year,Make,Model,Description,Price"):
        csv_text = text
        break

with open("cars.csv", "w", encoding="utf-8") as f:
    f.write(csv_text)