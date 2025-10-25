import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import subprocess


date = input("Plese enter a Date [YYYY-MM-DD] :")
page = requests.get(f"https://www.kooora.com/كرة-القدم/مواعيد-نتائج/{date}")

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "html.parser")

    matches_details = []

    championships = soup.find_all("div", {"class": "match-list_match-list__0JCHF"})

    def get_match_info(championship):
        championship_title = championship.find("div", {"class": "fco-competition-section__round-name"})
        print(championship_title.text.strip())

    get_match_info(championships[1])
main(page)    

# 2025-08-27
