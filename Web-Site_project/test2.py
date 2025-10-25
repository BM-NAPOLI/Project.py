import requests
from bs4 import BeautifulSoup

date = input("Plese enter a Date [YYYY-MM-DD] :")
page = requests.get(f"https://www.kooora.com/كرة-القدم/مواعيد-نتائج/{date}")

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "html.parser")

    # جميع الأقسام لي فيها الماتشات
    championships = soup.find_all("div", {"class": "match-list_match-list__0JCHF"})

    def get_match_info(championship):
        # نجيب اسم الجولة / البطولة
        championship_title = championship.find("div", {"class": "fco-competition-section__header-name"})
        if championship_title:
            print("🏆", championship_title.text.strip())
        else:
            print("❌ ما لقيتش عنوان البطولة")

    if championships:
        get_match_info(championships[0])
    else:
        print("❌ ما لقيتش مباريات فهاد التاريخ")

main(page)
