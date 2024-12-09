from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome()
driver.get("https://auth.hollandandbarrett.com/u/login")
driver.maximize_window()
time.sleep(5)

edit_box = driver.find_element(By.ID, "username")
edit_box.send_keys("divyach74@gmail.com")
edit_box.send_keys(Keys.RETURN)   # enter values in edit box by press keyboard

edit_box = driver.find_element(By.NAME, "password")
edit_box.send_keys("Divya@2001")
edit_box.send_keys(Keys.RETURN)