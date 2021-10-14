from bs4 import BeautifulSoup
import requests
import lxml

Webpage = requests.get("https://www.thingbits.in/products/raspberry-pi-400-computer?utm_source=google&utm_medium=cpc&gclid=CjwKCAjwqIiFBhAHEiwANg9szgyS916LtuGJ90s6FrP41BAj2OCyfyvLIBiiGiWMNHvqL8Ug9mZh9RoCFD4QAvD_BwE")

kab = BeautifulSoup(Webpage.content, "lxml")
content = kab.find('h1', class_="product-title h2").text
print(content)
price = kab.find('div', class_="h3 pr-1").text
print(price)
