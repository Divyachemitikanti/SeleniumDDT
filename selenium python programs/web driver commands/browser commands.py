from selenium import webdriver
from selenium.webdriver.common.by import By
import time
baseUrl = "https://www.ebay.com/"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
title = driver.title
print("Title of the web page is:" + title)

currentUrl = driver.current_url
print("Current Url of the web page is:" + currentUrl)
driver.refresh()
print("Browser Refreshed 1st time")

driver.get(driver.current_url)
print("Browser Refreshed 2nd time")

driver.get("https://www.ebay.com/")
CurrentUrl = driver.current_url
print("Current Url of the web page is: " + currentUrl)

driver.back()
print("Go one step back in browser history")
currentUrl = driver.current_url
print("Current Url of the web page is: " + currentUrl)

driver.forward()
print("Go one step forward in browser history")
currentUrl = driver.current_url
print("Current Url of the web page is: " + currentUrl)

pageSource = driver.page_source
print(pageSource.encode("utf-8"))
driver.quit()