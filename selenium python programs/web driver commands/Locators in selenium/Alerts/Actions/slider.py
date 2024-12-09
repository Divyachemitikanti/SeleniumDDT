from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#step:1
baseurl = ("https://jqueryui.com/slider/")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/slider/")
driver.implicitly_wait(4)

driver.switch_to.frame(0)
element = driver.find_element(By.XPATH,"//div[@id='slider']")

try:
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(element, 400, 0).perform()
    print("sliding element successful")
except:
    print("sliding failed on element")
