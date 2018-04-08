#! /usr/bin/python
#! coding=UTF-8
'''

'''

import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print BASE_DIR

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH



class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    print URL

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver = webdriver.Firefox()
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys('selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)
        time.sleep(5)

    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('Python selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)
        time.sleep(5)



if __name__ == '__main__':
    unittest.main()