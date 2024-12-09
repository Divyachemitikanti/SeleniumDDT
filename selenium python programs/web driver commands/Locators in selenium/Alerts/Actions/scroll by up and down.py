from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")           #step-1

driver.maximize_window()
time.sleep(5)
#scroll down
driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(4)
#scroll up
driver.execute_script("window.scrollBy(0, -1000);")
time.sleep(4)
#scroll element into view
element = driver.find_element(By.ID,"mousehover")
driver.execute_script("arguments[0].scrollIntoView(true);",  element)
time.sleep(4)
driver.execute_script("window.scrollBy(0, -150);")

