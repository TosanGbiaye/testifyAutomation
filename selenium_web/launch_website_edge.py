import time

from selenium import webdriver

def main():
    driver = webdriver.Edge(executable_path=r"C:\Users\hp\Documents\TAS\Web_Drivers\edgedriver_win64\msedgedriver.exe")
    driver.get("https://www.google.com/")
    time.sleep(2)
    driver.close()

main()