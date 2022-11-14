import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(By.ID, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "pass").send_keys("password")
driver.find_element(By.NAME, "login").click()
time.sleep(2)
driver.close()