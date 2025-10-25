import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import subprocess

# فتح CSV مباشرة
file_path = r"C:\Users\Rachid\Desktop\PROJECT.python\Web-Site_project\RAM9.csv"
subprocess.Popen(['start', '', file_path], shell=True)

# إعداد القوائم
job_title = []
company_name = []
location_name = []
job_skil = []
links = []
salary = []
responsabilitis = []

# طلب الصفحة الرئيسية مع Header
url = "https://wuzzuf.net/search/jobs?a=spbg&q=PYTHON"
headers = {"User-Agent": "Mozilla/5.0"}
result = requests.get(url, headers=headers, timeout=10)
soup = BeautifulSoup(result.content, "html.parser")

# استخراج البيانات
job_titles = soup.find_all("h2", {"class": "css-193uk2c"})
company_names = soup.find_all("a", {"class": "css-ipsyv7"})
location_names = soup.find_all("span", {"class": "css-16x61xq"})
job_skils = soup.find_all("div", {"class": "css-1rhj4yg"})

for i in range(len(job_titles)):
    job_title.append(job_titles[i].text.strip())

    # روابط كاملة
    link = job_titles[i].find("a").attrs["href"]
    if not link.startswith("http"):
        link = "https://wuzzuf.net" + link
    links.append(link)

    company_name.append(company_names[i].text.strip())
    location_name.append(location_names[i].text.strip())
    job_skil.append(job_skils[i].text.strip())

# استخراج الرواتب لكل إعلان
for link in links:
    try:
        result = requests.get(link, headers=headers, timeout=10)
        soup = BeautifulSoup(result.content, "html.parser")

        salaries = soup.find("span", {"class": "css-2rozun"})
        if salaries and salaries.text.strip():
            # غادي يخرج كل ما مكتوب: فعلي، Confidential، أو Social & Medical Insurances
            salary.append(salaries.text.strip())
        else:
            salary.append("Not mentioned")
    except Exception as e:
        salary.append(f"Error: {e}")
    rec = soup.find_all("div", {"dir","auto"},{"class": "css-1lqavbg"})
    responsabilitis.append(rec)

# تصدير CSV مع UTF-8
file_list = [job_title, company_name, location_name, job_skil, links, salary, responsabilitis]
exported = zip_longest(*file_list)

with open(file_path, "w", newline="", encoding="utf-8-sig") as FileDelMe:
    wr = csv.writer(FileDelMe)
    wr.writerow(["Job Title", "Company Name", "Location Names", "Job Skils", "Links", "Salary" , "responsabilitis"])
    wr.writerows(exported)

print("CSV تم إنشاؤه بنجاح ✅")
