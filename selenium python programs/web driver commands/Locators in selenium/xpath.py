from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID, "email").send_keys("divyach74@gmail.com")
driver.find_element(By.NAME, "password").send_keys("Divya@516")
driver.find_element(By.XPATH, '//*[@id="login"]').click()
time.sleep(5)
