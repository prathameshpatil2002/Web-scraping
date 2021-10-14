#Web Scraping geting started projrcts.

from bs4 import BeautifulSoup
import requests
import lxml

Webpage = requests.get("https://timesofindia.indiatimes.com/india/timestopten.cms")

kab = BeautifulSoup(Webpage.content, "lxml")
content = kab.find_all('a', class_="news_title")
#print(content)

for row in content:          # Print all occurrences
    print(row.get_text())