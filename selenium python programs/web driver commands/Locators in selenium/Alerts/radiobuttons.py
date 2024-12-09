from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/practice")           #step-1

driver.maximize_window()
time.sleep(5)
bmwradiobtn = driver.find_element(By.ID, "bmwradio")
bmwradiobtn.click()
time.sleep(5)

benzradiobtn = driver.find_element(By.ID,"benzradio")
benzradiobtn.click()
time.sleep(4)

bmwCheckbox =  driver.find_element(By.ID, "bmwcheck")
bmwCheckbox.click()
time.sleep(5)

benzCheckbox = driver.find_element(By.ID,"benzcheck")
benzCheckbox.click()

print("BMW Radio Button is selected ? " + str(bmwradiobtn.is_selected()))
print("Benz Radio Button is selected ? " + str(benzradiobtn.is_selected()))
print("BMW check box is selected ? " + str(bmwCheckbox.is_selected()))
print("Benz check box is selected ? " + str(benzCheckbox.is_selected()))

radio_buttons = driver.find_elements(By.XPATH,"//input[@id='benzradio']")
count = len(radio_buttons)
print(f"Total number of radio buttons: {count}")




