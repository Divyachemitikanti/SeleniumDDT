from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#step:1
baseurl = ("https://testautomationpractice.blogspot.com/")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

driver.execute_script("window.scrollBy(0, 1500);")
time.sleep(4)

fromElement = driver.find_element(By.ID, "draggable")
toElement = driver.find_element(By.ID, "droppable")
time.sleep(4)

try:
    actions = ActionChains(driver)
    actions.drag_and_drop(fromElement, toElement).perform()
    time.sleep(3)
    actions.drag_and_drop(toElement, fromElement).perform()

    print("Drag And Drop Element succesful")

except:
    print("Drag and Drop failed on element")