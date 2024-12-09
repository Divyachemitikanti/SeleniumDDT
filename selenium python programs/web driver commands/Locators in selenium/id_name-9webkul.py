from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome()
driver.get("https://store.webkul.com/")

driver.maximize_window()
time.sleep(5)

edit_box = driver.find_element(By.ID, "wk-login-email")
edit_box.send_keys("divyach74@gmail.com")
edit_box.send_keys(Keys.RETURN)   # enter values in edit box by press keyboard
time.sleep(9)

edit_box = driver.find_element(By.NAME, "login[password]")
edit_box.send_keys("Divya@516")
edit_box.send_keys(Keys.RETURN)
time.sleep(9)