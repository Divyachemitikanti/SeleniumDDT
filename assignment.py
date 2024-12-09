from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


import time
baseurl = "https://www.letskodeit.com/practice"       #step-1  #User Should select any one browser and Open 
	                                                  #URL "https://www.letskodeit.com/practice" 
		                                            #a.Chrome Browser
		                                              #b.Edge
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseurl)
time.sleep(9)


links =driver.find_elements(By.XPATH,"//div[@class='col-md-12']//a")       #step-2 #Count number Radio buttons and Check boxes and print
print(len(links))

links =driver.find_elements(By.XPATH,"//div[@class='col-md-12']//a")
print(len(links))


element = driver.find_element(By.CLASS_NAME,"dropbtn")            #step-3  #Move hand over on "Mouse Hover" then click on 'Reload'
itemToClickLocator = "//a[normalize-space()='Reload']"
try:
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    print("Mouse Handovered on 'Reload' element")
    time.sleep(4)
    topLink = driver.find_element(By.XPATH, itemToClickLocator)
    actions.move_to_element(topLink).click().perform()

    print("Item Clicked")
except:
    print("House Hover failed on element")
time.sleep(4)


edit_box = driver.find_element(By.NAME, "enter-name")             #step-4  #Enter "Selenium Python" in Editbox Validate both Alerts
edit_box.send_keys("selenium python")
edit_box.send_keys(Keys.RETURN)
time.sleep(9)

driver.find_element(By.XPATH, '//*[@id="alertbtn"]').click()
time.sleep(4)
driver.switch_to.alert.accept()


driver.find_element(By.XPATH,'//*[@id="confirmbtn"]').click()
time.sleep(4)
driver.switch_to.alert.accept()



driver.save_screenshot(".\\error.png")            #step-5  #Take Screen shots of each and every steps
destinationFileName = ".\\screenshot.png"
time.sleep(4)


page_title = driver.title                    #step-6   # Print Page Title, Get page Source and Page Source length 
print(f"Page Title: {page_title}")

page_source = driver.page_source
source_length = len(page_source)
print(f"Page Source Length: {source_length}")
time.sleep(4)

actual_title = driver.title
expected_title = "Practice Page"

if actual_title == expected_title:                               #step-7  #Validate the title with "Practice Page"
    print(f"Title validation successful! Title is: {actual_title}")
else:
    print(f"Title validation failed! Expected: '{expected_title}'")


driver.save_screenshot(".\\error.png")            #step-8  #Take Screenshot of each steps
destinationFileName = ".\\screenshot.png"
time.sleep(4)


driver.find_element(By.LINK_TEXT, "Terms & Conditions").click()      #step-9   #Click Terms and Conditions and then Click Sign in
                                                                                           # enter proper credientails then sign in
driver.find_element(By.XPATH, '//*[@id="navbar-inverse-collapse"]/div/div/a').click()


driver.get("https://www.letskodeit.com/login")
edit_box = driver.find_element(By.ID, "email")
edit_box.send_keys("divyach74@gmail.com")
edit_box.send_keys(Keys.RETURN)
time.sleep(9)

edit_box = driver.find_element(By.NAME, "password")
edit_box.send_keys("Divya@516")
edit_box.send_keys(Keys.RETURN)
time.sleep(9)

driver.close()      #step-10   #Close the Browser Run and Validate test scripts 