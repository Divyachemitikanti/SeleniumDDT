from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome()
driver.get("https://www.nopcommerce.com/en")          #open URL Using chrome browser

driver.maximize_window()
time.sleep(5)

all_links = driver.find_elements(By.XPATH,  ".//a")
print(len(all_links))

for links in all_links:
    print(links.text)
    if links.get_attribute('href'):
        print("link is present")
    else:
        print("link is not present")

footer_links = driver.find_elements(By.XPATH,  ".//div[@class='footer-upper-wrapper']//a")
print(len(footer_links))

for links in footer_links:
    print(links.text)
    if links.get_attribute('href'):
        print("link is present")
    else:
        print("link is not present")
