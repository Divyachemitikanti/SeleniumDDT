from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#step:1
baseurl = ("https://admin:admin@the-internet.herokuapp.com/drag_and_drop")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://admin:admin@the-internet.herokuapp.com/drag_and_drop")
time.sleep(2)

fromElement = driver.find_element(By.ID, "column-a")
toElement = driver.find_element(By.ID, "column-b")
time.sleep(4)

try:
    actions = ActionChains(driver)
    actions.drag_and_drop(fromElement, toElement).perform()
    time.sleep(3)
    actions.drag_and_drop(toElement, fromElement).perform()

    print("Drag And Drop Element succesful")

except:
    print("Drag and Drop failed on element")