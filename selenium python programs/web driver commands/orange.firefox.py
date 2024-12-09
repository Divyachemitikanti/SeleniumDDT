from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
page_title = driver.title
title_length = len(page_title)
print(f"Page Title: {page_title}")
print(f"Title Length: {title_length}")
current_url = driver.current_url
if current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login":
    print("URL is correct.")
else:
    print("URL is incorrect.")
page_source = driver.page_source
source_length = len(page_source)
print(f"Page Source Length: {source_length}")
driver.quit()