from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php?id_category=4&controller=category")          #open URL Using chrome browser

driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,     '//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()       #click on sign in button



edit_box = driver.find_element(By.ID, "email")    #enter email id
edit_box.send_keys("divyach74@gmail.com")
edit_box.send_keys(Keys.RETURN)   # enter values in edit box by press keyboard
time.sleep(9)

edit_box = driver.find_element(By.NAME, "passwd")   #enter password and click on sign in
edit_box.send_keys("Divya@2001")
edit_box.send_keys(Keys.RETURN)
time.sleep(9)

driver.find_element(By.XPATH,     '//*[@id="block_top_menu"]/ul/li[2]/a').click()                 #click on dresses
driver.find_element(By.XPATH,     '//*[@id="columns"]/div[1]/span[2]/span[1]/a/span').click()                 #click on women
driver.quit()