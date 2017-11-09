#JS alert handling with selenium
from selenium import webdriver
drive = webdriver.Chrome()
drive.get("http://localhost:85/myfile.html")
#Click onlick button
sub = drive.find_element_by_tag_name("button").click()
#Accept JS alert
drive.switch_to_alert().accept()

#JS prompt handling with selenium
from selenium import webdriver
drive = webdriver.Chrome()
drive.get("http://localhost:85/form2.html")
sub = drive.find_element_by_tag_name("button").click()
alert = drive.switch_to_alert()
#Get user input inside JS prompt
alert.send_keys('vivek')
#Click OK
alert.accept()
alert.send_keys('raj')
alert.accept()

#Login with JS form
from selenium import webdriver
drive = webdriver.Chrome()
drive.get("http://localhost:85/form.html")
pop = drive.find_element_by_link_text("Show Popup Form").click()
#Entering username
name = drive.find_element_by_xpath("//input[@type='text']")
name.send_keys('vivek')
#Entering password
pss = drive.find_element_by_xpath("//input[@type='password']")
pss.send_keys('mypass')
drive.find_element_by_xpath("//input[@type='submit']").click()
