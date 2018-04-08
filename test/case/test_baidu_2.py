import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH
from utils.log import logger



#
# URL = Config().get('URL')
# # driver = webdriver.Chrome(executable_path=DRIVER_PATH + '/chromedriver.exe')
# driver = webdriver.Chrome()
# driver.get(URL)


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        _chrome_options = Options()
        _chrome_options.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '/chromedriver',chrome_options=_chrome_options)
        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '/chromedriver')
        # self.driver = webdriver.Chrome(chrome_options=_chrome_options)
        # self.driver = webdriver.Firefox()
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys('selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)

    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('Pythonselenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)


if __name__ == '__main__':
    unittest.main()
    # passURL = Config().get('URL')