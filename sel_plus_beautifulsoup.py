from selenium import webdriver
from bs4 import BeautifulSoup

user = "admin"
passwd = "Password@123"

drive = webdriver.Chrome()
drive.get('http://localhost:8000/admin')
#Getting login with admin credential
username = drive.find_element_by_id("id_username")
username.send_keys(user)
password = drive.find_element_by_id("id_password")
password.send_keys(passwd)
login = drive.find_element_by_css_selector(".submit-row")
login.click()
#Change password of user
view = drive.find_element_by_link_text('CHANGE PASSWORD').click()
old = drive.find_element_by_id("id_old_password")
old.send_keys(passwd)
new = drive.find_element_by_id("id_new_password1")
new.send_keys("Python@1234")
new2 = drive.find_element_by_id("id_new_password2")
new2.send_keys("Python@1234")
sub = drive.find_element_by_css_selector(".default").click(
html = drive.page_source
soup = BeautifulSoup(html)
print soup
drive.close()
