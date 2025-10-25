import requests
from bs4 import BeautifulSoup
# import csv
# from itertools import zip_longest
# import subprocess

page = requests.get("http://192.168.0.1/index.html#status")

src = page.content
soup = BeautifulSoup(src, "html.parser")



