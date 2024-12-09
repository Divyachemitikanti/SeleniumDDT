from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome()
driver.get("https://www.easycalculation.com/index.php")   #open URL Using chrome browser

driver.maximize_window()
time.sleep(5)

element = driver.find_element(By.CLASS_NAME,"lang")
itemToClickLocator = "//div[@class='header_part']//header[@class='tbl-explore-more-site-header']//li[2]//a[1]"
try:
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    print("Mouse Handovered on 'deutschland' element")
    time.sleep(4)
    topLink = driver.find_element(By.XPATH, itemToClickLocator)
    actions.move_to_element(topLink).click().perform()

    print("Item Clicked")
except:
    print("mouse Hover failed on element")
