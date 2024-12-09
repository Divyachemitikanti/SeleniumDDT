from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#step:1
baseurl = ("https://demo.automationtesting.in/FileDownload.html")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/FileDownload.html")
time.sleep(2)

driver.find_element(By.ID,"textbox").send_keys("Welcome to selenium python...!Download text file")
driver.find_element(By.ID,"createTxt").click()
driver.find_element(By.ID,"link-to-download").click()
time.sleep(4)

driver.find_element(By.ID, "pdfbox").send_keys('welcome to selenium python...!download pdf file')
driver.find_element(By.ID, "createPdf").click()
driver.find_element(By.ID,"pdf-link-to-download").click()

