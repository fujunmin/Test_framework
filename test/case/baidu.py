#! /usr/bin/python
#! coding=UTF-8
import json
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://www.baidu.com"
# base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
# driver_path = os.path.abspath(base_path+'\drivers\chromedriver.exe')

locator_kw = (By.ID, 'kw')
locator_su = (By.ID, 'su')
locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')
keyword = json.dumps('selenium')
print type(keyword)


driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.get(URL)
# try:
driver.find_element(*locator_kw).send_keys('selenium')
driver.find_element(*locator_su).click()
time.sleep(2)
links = driver.find_elements(*locator_result)
for link in links:
    print(link.text)
time.sleep(2)

# except:
driver.quit()
