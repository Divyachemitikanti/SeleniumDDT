from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")           #step-1

driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@title='Sign in']").click()
time.sleep(4)

