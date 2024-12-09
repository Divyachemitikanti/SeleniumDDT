from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.freecrm.com/en")
driver.maximize_window()

time.sleep(8)
actual_title = driver.title
expect_title = "Cogmento Free CRM with AI Customer Relationship Management"
print(len(expect_title))
if actual_title == expect_title:
    print("login")
else:
    print("login unsuccesfull")
print(len(driver.page_source.encode("utf-8")))
