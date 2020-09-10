#Selenium
#Automatic Login To Facebook

from selenium import webdriver
browser=webdriver.Chrome('D:\\webdriver\\chromedriver.exe')
browser.get('https://www.facebook.com')

user_id=input("enter your email")
password=input("enter the password")

ep=browser.find_element_by_id("email")
ep.send_keys(user_id)

pw=browser.find_element_by_id("pass")
pw.send_keys(password)

login=browser.find_element_by_id("u_0_b")
login.click()
