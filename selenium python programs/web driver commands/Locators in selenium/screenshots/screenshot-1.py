from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://auth.hollandandbarrett.com/u/login")

driver.maximize_window()
time.sleep(5)


edit_box = driver.find_element(By.ID, "username")
edit_box.send_keys("divyach74@gmail.com")
edit_box.send_keys(Keys.RETURN)   # enter values in edit box by press keyboard
time.sleep(9)
driver.save_screenshot(".//username screenshot.png")

edit_box = driver.find_element(By.NAME, "password")
edit_box.send_keys("Divya@516")
#edit_box.send_keys(Keys.RETURN)
time.sleep(9)
driver.save_screenshot(".//password screenshot.png")


driver.find_element(By.XPATH,"//button[normalize-space()='Sign In']").click()
time.sleep(6)
driver.save_screenshot(".//clicked on signin screenshot.png")

driver.save_screenshot(".\\error.png")
destinationFileName = ".\\screenshot.png"

fileName = str(round(time.time() * 10000)) + ".png"
screenshotDirectory = ".\\screenshot.png"
destinationFile = screenshotDirectory + fileName

try:
    driver.save_screenshot(destinationFile)
    print("Screenshot saved to directory --> :: " + destinationFile)
except NotADirectoryError:
    print("Not A directory issue")



