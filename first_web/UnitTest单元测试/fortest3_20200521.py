import unittest
from selenium import webdriver
import time
from ddt import ddt,data

@ddt
class forTestTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')

    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()

    @data('虚竹','小龙女')
    def test_1(self,txt):
        self.driver.find_element_by_id('kw').send_keys(txt)
        self.driver.find_element_by_id('su').click()

if __name__ == '__main__':
    unittest.main()