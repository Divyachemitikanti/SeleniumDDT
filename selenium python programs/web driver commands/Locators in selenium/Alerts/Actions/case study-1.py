from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#step:1
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.spicejet.com/")
time.sleep(2)

#step:2
#scroll down
driver.execute_script("window.scrollBy(0,2000);")
time.sleep(2)
#step:3
#scroll up
driver.execute_script("window.scrollBy(0,-2000);")
time.sleep(2)
#step:4

element = driver.find_element(By.XPATH,"//div[@class='css-76zvg2 r-c20mna r-yy2aun r-1kfrs79 r-1h0z5md r-lgpkq'][normalize-space()='Cargo']")
driver.execute_script("arguments[0].scrollIntoView(true);",element)
time.sleep(4)

driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[13]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]").click()
time.sleep(5)




