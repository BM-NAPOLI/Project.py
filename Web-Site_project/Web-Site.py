import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import subprocess

# file_path = r"C:\Users\Rachid\Desktop\PROJECT.python\Web-Site_project\RAM9.csv"
# subprocess.Popen(['start', '', file_path], shell=True)
# # import os

# file_path = r"C:\Users\Rachid\Desktop\PROJECT.python\Web-Site_project\RAM9.csv"
# os.startfile(file_path)


imei = []
# company_name = []
# location_name = []
# job_skil = []
# links = []
# salary = []
# responsabilitis = []

result = requests.get("http://192.168.0.1/index.html#status")

#todo 2. جلب المحتوى
src = result.content
soup = BeautifulSoup(src, "html.parser")


#! 3. استخراج البيانات
# استخراج IMEI
imei_div = soup.find("div", {"class": "span8", "data-bind": "text: imei"})
imei_value = imei_div.get_text(strip=True)   # تاخذ النص فقط بلا مسافات
imei.append(imei_value)

print("IMEI:", imei_value)
IMSI = soup.find_all("a", {"class": "css-ipsyv7"})
Force_du_signal = soup.find_all("span", {"class":"css-16x61xq"})
Nom_du_réseau_SSID = soup.find_all("div", {"class": "css-1rhj4yg"})






# print(len(location_names))
# print(job_title)
# print("\n")
# print(company_name)
# print("\n")
# print(location_name)
# print("\n")
# print(job_skil)
# print("\n")
# print(links)
# print("\n")
# print(slr)

# file_list = [job_title, company_name, location_name, job_skil, links, salary, responsabilitis]
# exported = zip_longest(*file_list)
with open(r"C:\Users\Rachid\Desktop\PROJECT.python\Web-Site_project\RAM9.csv","w") as FileDelMe1:
    wr = csv.writer(FileDelMe1)
    wr.writerow(["Job Title", "Company Name", "Location Names", "Job Skils", "links", "salary", "responsabilitis"])
    # wr.writerows(exported)