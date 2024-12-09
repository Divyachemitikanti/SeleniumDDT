#WAP using selenium web driver commands to print current url,title,and page source
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.hollandandbarrett.com/auth/signup")
driver.maximize_window()
time.sleep(5)

driver.get("https://www.google.com")
time.sleep(5)

driver.back()
time.sleep(5)

driver.forward()
time.sleep(5)

driver.refresh()
time.sleep(5)

print(driver.page_source)
print(driver.current_url)
print(driver.title)