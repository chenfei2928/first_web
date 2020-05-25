import unittest
import time
from selenium import webdriver

class testBaidu(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.base_url ='https://www.baidu.com'

    def test_serarch_key_selenium(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(10)
        title = self.driver.title
        self.assertEqual(title,"selenium_百度搜索")

    def test_serarch_key_unittest(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys('unittest')
        self.driver.find_element_by_id('su').click()
        time.sleep(10)
        title = self.driver.title
        self.assertEqual(title,"unittest_百度搜索")

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

