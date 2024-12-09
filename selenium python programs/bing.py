from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.bing.com/")
driver.maximize_window()

time.sleep(8)
actual_title = driver.title
expect_title = "Bing"
print(len(expect_title))
if actual_title == expect_title:
    print("login")
else:
    print("login unsuccesfull")
print(len(driver.page_source.encode("utf-8")))
