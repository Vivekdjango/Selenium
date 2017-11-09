from selenium import webdriver
from bs4 import BeautifulSoup as BS

drive = webdriver.Chrome()
drive.get("http://localhost:8000/admin")
user = drive.find_element_by_id("id_username")
user.send_keys("admin")
passwd = drive.find_element_by_id("id_password")
passwd.send_keys("Python@1234")
sub = drive.find_element_by_css_selector(".submit-row")
sub.click()
#To click change password URL
#element = drive.find_element_by_link_text("CHANGE PASSWORD").click()
'''
#Delete an user
#To click a url having href
get_user = drive.find_element_by_xpath("//a[contains(@href,'/admin/auth/user/')]").click()
#To select dropdown option
sel = drive.find_element_by_xpath("//select/option[@value='delete_selected']").click()
#Select a user e.g vivek
check = drive.find_element_by_xpath("//input[@value='3']").click()
go = drive.find_element_by_name("index").click()
#back = drive.find_element_by_link_text("No, take me back").click()
delete = drive.find_element_by_xpath("//input[@type='submit']").click()
drive.close()

html = drive.page_source
soup = BS(html)
print soup
drive.close()

'''
#New single user addition
'''
add_user = drive.find_element_by_xpath("//tr[@class='model-user']//a[@class='addlink']").click()
name = drive.find_element_by_id("id_username")
name.send_keys("%s"%(i))
pwd = drive.find_element_by_id("id_password1")
pwd.send_keys("Mypassword@12")
pwd1 = drive.find_element_by_id("id_password2")
pwd1.send_keys("Mypassword@12")
save = drive.find_element_by_xpath("//div[@class='submit-row']//input[@class='default']").click()
'''
name_list = ['vk2','vk3','vk4']
#Add multiple users at once
for i in name_list:
    add_user = drive.find_element_by_xpath("//tr[@class='model-user']//a[@class='addlink']").click()
    name = drive.find_element_by_id("id_username")
    name.send_keys("%s"%(i))
    pwd = drive.find_element_by_id("id_password1")
    pwd.send_keys("Mypassword@12")
    pwd1 = drive.find_element_by_id("id_password2")
    pwd1.send_keys("Mypassword@12")
    save = drive.find_element_by_xpath("//div[@class='submit-row']//input[@class='default']").click()
#Go to Home location
    home = drive.find_element_by_xpath("//a[contains(@href,'/admin/')]").click()
#Get users lists
get_user = drive.find_element_by_xpath("//a[contains(@href,'/admin/auth/user/')]").click()
drive.close()
