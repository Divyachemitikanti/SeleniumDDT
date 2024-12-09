from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


baseUrl="https://demo.automationtesting.in/FileDownload.html"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
time.sleep(5)

driver.find_element(By.ID,"textbox").send_keys('Welcome to selenium python...! Download text File')
driver.find_element(By.ID,"createTxt").click()
driver.find_element(By.ID,"link-to-download").click()
time.sleep(3)

driver.find_element(By.ID,"pdfbox").send_keys("Welcome to selenium python.....! Download pdf File ")
driver.find_element(By.ID,"createPdf").click()
driver.find_element(By.ID,"pdf-link-to-download").click()