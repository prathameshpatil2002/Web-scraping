from bs4 import BeautifulSoup
import requests
import lxml

Webpage = requests.get("https://hi.weather.town/en/forecast/india/state-of-chhattisgarh/dongargarh/")

kab = BeautifulSoup(Webpage.content, "lxml")
Temp = kab.find('div', class_="temp").text
print(Temp)

TempMor = kab.find('div', class_="temperature", id="infTempMorning").text
print(TempMor)

TempNight = kab.find('div', class_="temperature", id="infTempNight").text
print(TempNight)