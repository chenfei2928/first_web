
import unittest
import time
from selenium import webdriver

class testBaidu(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.base_url ='http://192.168.10.233:8080/marsCloud/loginController.do?login'


    def test_login(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('userName').send_keys('admin')
        self.driver.find_element_by_id('password').send_keys('123456')
        self.driver.find_element_by_id('randCode').send_keys('0000')
        self.driver.find_element_by_id('but_login').click()
        title = self.driver.title
        self.assertEqual(title, "百度搜索")

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

