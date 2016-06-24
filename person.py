from selenium import webdriver
#import os
import unittest,re,time
#from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import *

username = 'faith@qq.com'
password = 'faithfaith'

driver=webdriver.Firefox()
driver.get("http://192.168.31.121:3020/portal/login")

driver.find_element_by_id('authId').send_keys(username)
driver.find_element_by_id('password').send_keys(password)

driver.find_element_by_class_name('ant-btn').click()


time.sleep(3)
chain = ActionChains(driver)
a = driver.find_elements_by_class_name("ProductItem")[0]
chain.move_to_element(a).perform()
driver.find_element_by_class_name("HoverProduct-button").click()
time.sleep(20)

# driver.forward('http://192.168.31.121:3020/portal/main')


