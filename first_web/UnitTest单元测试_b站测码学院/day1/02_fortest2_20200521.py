import unittest
from selenium import webdriver
import time

class forTestTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()


    def test_1(self):
        self.driver.find_element_by_id('kw').send_keys('虚竹')
        self.driver.find_element_by_id('su').click()

    def test_2(self):
        self.driver.find_element_by_id('kw').send_keys('小龙女')
        self.driver.find_element_by_id('su').click()

if __name__ == '__main__':
    unittest.main()