import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(2)
driver.close()