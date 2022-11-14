# challenge 2 :
# Using the firefox browser navigate to https://www.google.com/ ,
# enter the text Python in the search box then send the Enter key.
# Get the text from the wikipedia brief on the right side and print the value in the console
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element(By.NAME, "q").send_keys("Python")
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()
driver.find_element(By.XPATH, "//input[@name='q']").click()

#driver.find_element(By.XPATH, "//span[ text()='python']")
p1 = driver.find_elements(By.XPATH, "//a[@class='l']")

# the below line will print the total no of values in the list
print(len(p1))

for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)

time.sleep(4)
driver.close()