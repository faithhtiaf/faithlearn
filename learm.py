# -*- coding: utf-8 -*-

from selenium import  webdriver
import time

driver=webdriver.Firefox()
first_url="http://www.baidu.com"
print "now access %s"%(first_url)
driver.get(first_url)
second_url="http://news.baidu.com/"
print "now access %s"%(second_url)
driver.get(second_url)
time.sleep(10)
driver.back()
time.sleep(10)
driver.forward()
time.sleep(10)

driver.quit()