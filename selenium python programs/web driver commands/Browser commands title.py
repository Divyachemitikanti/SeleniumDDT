from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://automationpractice.com/index.php")
time.sleep(5)
page_title = driver.title
title_length = len(page_title)
print(f"Page Title: {page_title}")
print(f"Title Length: {title_length}")
current_url = driver.current_url
if current_url == "http://automationpractice.com/index.php":
    print("URL is correct.")
else:
    print("URL is incorrect.")
page_source = driver.page_source
source_length = len(page_source)
print(f"Page Source Length: {source_length}")
driver.quit()