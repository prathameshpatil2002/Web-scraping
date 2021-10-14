from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("https://meet.google.com/?hs=193")

search = driver.find_element_by_name("q")
search.send_keys("Python")
search.send_keys(Keys.RETURN)