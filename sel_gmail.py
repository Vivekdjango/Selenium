# Modules to be imported.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Your login details.
email = "<Email-id>"
passwd = "<Password>"

# Browser : Firefox.
driver = webdriver.Chrome()
driver.get("http://www.gmail.com")
time.sleep(2)

# GMAIL login.
username=driver.find_element_by_css_selector(".whsOnd")
username.send_keys(email)
time.sleep(2)
next=driver.find_element_by_css_selector(".RveJvd")
next.click()
time.sleep(2)
password=driver.find_element_by_css_selector(".whsOnd")
password.send_keys(passwd)
time.sleep(2)
login=driver.find_element_by_css_selector(".CwaK9")
login.click()
#Wait till get mailbox
time.sleep(5)
#Click on compose button
comp = driver.find_element_by_class_name("z0").click()
time.sleep(2)
#Write TO address
to = driver.find_element_by_xpath("//textarea[@class='vO']")
to.send_keys('vivekkumar.sinha@vvdntech.in')
#Write subject name
subj = driver.find_element_by_xpath("//input[@class='aoT']")
subj.send_keys('testing2')
#Write Text message
cont = driver.find_element_by_xpath("//div[@class='Am Al editable LW-avf']")
cont.send_keys('Mytest')
#Send mail
send = driver.find_element_by_xpath("//div[@class='J-J5-Ji btA']").click()
#Click on hide logout option
clk = driver.find_element_by_xpath("//span[@class='gb_bb gbii']").click()
#Click on logout
logout = driver.find_element_by_xpath("//a[@id='gb_71']").click()
# Closing Browser.
driver.quit()
