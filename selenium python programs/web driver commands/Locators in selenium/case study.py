from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome()
driver.get("https://www.easycalculation.com/index.php")      #Launch URL using Chrome Browser

driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,    '//*[@id="wrap"]/div[2]/div[2]/span[2]/a/span').click()    #click sign-in button
edit_box = driver.find_element(By.ID, "log_email")         #Enter email/mobile and password
edit_box.send_keys("divyach74@gmail.com")
edit_box.send_keys(Keys.RETURN)
time.sleep(9)

edit_box = driver.find_element(By.NAME, "log_password")
edit_box.send_keys("Divya@516")
edit_box.send_keys(Keys.RETURN)   # Return----enter values in edit box by press keyboard
time.sleep(9)

driver.find_element(By.XPATH,'//*[@id="log_frm"]/div[4]/input[1]').click()    #click login button
time.sleep(9)

edit_box = driver.find_element(By.NAME, "q")      #enter bangalore in edit box
edit_box.send_keys("Bangalore")
time.sleep(9)

driver.find_element(By.XPATH,'//*[@id="cse-search-box"]/span[2]/button').click()       #click search button
#driver.find_element(By.XPATH,'//*[@id="inner-sbox"]/div/div/div/div[5]/div[2]/div/div/div[1]/div[1]/div/div[1]/div/a').click()       #click first link from the open page
driver.quit()           #close the browser