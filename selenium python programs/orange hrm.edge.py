from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(8)
actual_title = driver.title
expect_title = "OrangeHRM"

print(len(expect_title))
if actual_title == expect_title:
    print("login")
else:
    print("login unsuccesfull")
print(len(driver.page_source.encode("utf-8")))



