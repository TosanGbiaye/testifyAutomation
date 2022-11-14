import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(2)
driver.close()