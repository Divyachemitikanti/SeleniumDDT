from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome()
driver.get("https://www.login.hiox.com/login?referrer=easycalculation.com")

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


driver.find_element(By.XPATH,     '//*[@id="log_frm"]/div[4]/input[1]').click()
time.sleep(9)