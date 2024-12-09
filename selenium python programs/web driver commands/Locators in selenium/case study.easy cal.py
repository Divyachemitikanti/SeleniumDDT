from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome()
driver.get("https://www.login.hiox.com/login?referrer=easycalculation.com")   #open URL Using chrome browser

driver.maximize_window()
time.sleep(5)

edit_box = driver.find_element(By.ID, "log_email")
edit_box.send_keys("divyach74@gmail.com")
edit_box.send_keys(Keys.RETURN)   # enter values in edit box by press keyboard
time.sleep(9)

edit_box = driver.find_element(By.NAME, "log_password")
edit_box.send_keys("Divya@516")
edit_box.send_keys(Keys.RETURN)   # enter values in edit box by press keyboard
time.sleep(9)


all_links = driver.find_elements(By.XPATH,  ".//a")
print(len(all_links))

for links in all_links:
    print(links.text)
    if links.get_attribute('href'):
        print("link is present")
    else:
        print("link is not present")




footer_links = driver.find_elements(By.XPATH,  ".//div[@class='header_part']//a")
print(len(footer_links))

for links in footer_links:
    print(links.text)
    if links.get_attribute('href'):
        print("link is present")
    else:
        print("link is not present")