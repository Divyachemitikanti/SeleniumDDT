from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/campaign/landing.php")

driver.maximize_window()
time.sleep(5)



dropdown = driver.find_element(By.ID,"day")
select = Select(dropdown)
time.sleep(5)

num_options = len(select.options)
print(f"there are {num_options} options in the month Dropdown.")

for option in select.options:
    print(option.text)