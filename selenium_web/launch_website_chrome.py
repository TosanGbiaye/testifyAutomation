import time

from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path="C:/Users/hp/Documents/TAS/Web_Drivers/chromedriver_win32/chromedriver.exe")
    driver.get("https://www.google.com/")
    time.sleep(2)
    driver.close()

main()