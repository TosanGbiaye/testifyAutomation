# Navigate to https://www.bbc.com/ and print out top 10 news from the browser.
# auto-suggestion technique applied by me

import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.bbc.com/")
driver.find_element(By.CLASS_NAME, "orbit-search-button-icon-with-text").click()
driver.find_element(By.XPATH, "//input[@id='search-input']").send_keys("top 10 news")
driver.find_element(By.XPATH, "//button[@class='ssrcss-19dw7l7-Button etotop31']").click()
top10news = driver.find_elements(By.XPATH, "//a[@class='ssrcss-1ynlzyd-PromoLink e1f5wbog0']")
print(len(top10news))

for element in range(len(top10news)):
    if top10news[element].is_displayed():
        print("Top 10 news is: ", top10news[element].text)


time.sleep(3)
driver.quit()


