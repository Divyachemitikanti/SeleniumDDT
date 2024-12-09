from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://auth.hollandandbarrett.com/u/login")
driver.maximize_window()
time.sleep(8)
actual_title = driver.title
expect_title = "sign in - to your account, for the best experience"

if actual_title == expect_title:
    print("login is successful .... well done python")
else:
    print("login unsuccesful ..... very good girl!")