import time

from selenium import webdriver

def main():
    driver = webdriver.Firefox(executable_path=r"C:\Users\hp\Documents\TAS\Web_Drivers\geckodriver-v0.32.0-win64\geckodriver.exe")
    driver.get("https://www.google.com/")
    time.sleep(2)
    driver.close()

main()