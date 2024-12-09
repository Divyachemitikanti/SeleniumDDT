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

driver.execute_script("window.scrollBy(0,1300);")
time.sleep(5)

driver.find_element(By.ID,"singleFileInput").send_keys("C://Users//DELL//OneDrive//Pictures")
time.sleep(4)

try:
    actions = ActionChains(driver)

    print("File uploading succesful")
except:
    print("File upload not successful")
