import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import subprocess

page = requests.get("https://www.seuil.com/auteur/mohammed-khair-eddine/3375")

src = page.content
soup = BeautifulSoup(src, "html.parser")

name = soup.find("h1", {"itemprop": "name"}).text.strip()
biographie = soup.find("div", {"id": "bio"}).text.strip()

print(f"                                                                                           | {name} |")
print("\n")
print(f"_{biographie}")