# Navigate any browser to https://weather.com/
# Get the current temperature and print it out in the terminal
#Then print out the temperature for morning, afternoon, evening and night.

import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://weather.com/")
current_temp = driver.find_element(By.XPATH, "(//span[@data-testid='TemperatureValue'])[1]")
print("Current Temperature value is ", current_temp.text)
morning_temp = driver.find_element(By.XPATH, "(//span[@data-testid='TemperatureValue'])[4]")
print("Morning Temperature is ", morning_temp.text)
afternoon_temp = driver.find_element(By.XPATH, "(//span[@data-testid='TemperatureValue'])[5]")
print("Afternoon Temperature is ", afternoon_temp.text)
evening_temp = driver.find_element(By.XPATH, "(//span[@data-testid='TemperatureValue'])[6]")
print("Evening Temperature is ", evening_temp.text)
night_temp = driver.find_element(By.XPATH, "(//span[@data-testid='TemperatureValue'])[7]")
print("Night Temperature is ", night_temp.text)
time.sleep(2)
driver.close()