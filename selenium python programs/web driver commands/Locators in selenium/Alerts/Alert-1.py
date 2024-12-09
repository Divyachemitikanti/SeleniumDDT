from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")           #step-1

driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']").click()
time.sleep(4)
driver.switch_to.alert.accept()
result = driver.find_element(By.ID, 'result').text
print("value of attribute is: " + result)
assert "You succesfully clicked an alert", result

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
time.sleep(4)
driver.switch_to.alert.accept()
result = driver.find_element(By.ID, 'result').text
print("value of attribute is: " + result)
assert "You clicked: ok", result

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
time.sleep(4)
driver.switch_to.alert.dismiss()
result = driver.find_element(By.ID, 'result').text
print("value of attribute is: " + result)
assert ("You clicked: cancle" + result)

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(4)
driver.switch_to.alert.send_keys('welcome')
driver.switch_to.alert.accept()
result = driver.find_element(By.ID,"result").text
print("value of attribute is: " + result)
assert "You entered:welcome", result

driver.get("https:admin:admin@the-internet.herokuapp.com/basic_auth");
value = driver.find_element(By.XPATH, "//p[contains(text(),'Congratulations! You must have the proper credentials')]").text
time.sleep(3)
print("value of attribute is: " + value)
assert "Congratulations! You must have the proper credentials", value