from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/DELL/Downloads/frame.html")           #base url

driver.maximize_window()
time.sleep(5)

driver.switch_to.frame("HollandandBarrett")
driver.get("https://auth.hollandandbarrett.com/u/login")
driver.find_element(By.ID, "username").send_keys("divyach74@gmail.com")
driver.find_element(By.ID, "password").send_keys("Divya@516")
driver.find_element(By.XPATH,"/html/body/main/section/div/div/div/form/div[2]/button").click()
time.sleep(4)

driver.get("file:///C:/Users/DELL/Downloads/frame.html")
time.sleep(4)

driver.find_element(By.XPATH,"/html/body/a").click()

driver.get("https://www.selenium.dev/")
driver.find_element(By.XPATH,"/html/body/div/main/section[2]/div/div/div[1]/div/div[1]/h4").click()
time.sleep(4)

driver.get("file:///C:/Users/DELL/Downloads/frame.html")
driver.switch_to.frame("My Store")
driver.get("https://demo.opencart.com/")
time.sleep(5)

driver.find_element(By.NAME,"search").send_keys("product")
time.sleep(4)
driver.find_element(By.XPATH, "//i[contains(@class,'fa-solid fa-magnifying-glass')]").click()
time.sleep(2)

driver.find_element(By.XPATH,"/html").click()
