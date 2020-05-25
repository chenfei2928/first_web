import unittest
import time
from selenium import webdriver

class testBaidu(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.base_url ='https://www.baidu.com'

    def baidu_search(self,search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        time.sleep(10)


    def test_search_key_selenium(self):
        search_key = 'selenium'
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")

    def test_search_key_unittest(self):
        search_key = 'unittest'
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

