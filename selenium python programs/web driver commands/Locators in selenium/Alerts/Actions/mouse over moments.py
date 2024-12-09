from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("https://www.rajasthanroyals.com/login")           #step-1

driver.maximize_window()
time.sleep(5)

element = driver.find_element(By.CLASS_NAME,"nav-anchor")
itemToClickLocator = "//span[normalize-space()='Squad']"

try:
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    print("Mouse Handovered on 'Squad' element")
    time.sleep(4)
    topLink = driver.find_element(By.XPATH, itemToClickLocator)
    actions.move_to_element(topLink).click().perform()

    print("Item Clicked")
except:
    print("mouse Hover failed on element")