from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")           #step-1

driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='confirmbtn']").click()
time.sleep(4)

