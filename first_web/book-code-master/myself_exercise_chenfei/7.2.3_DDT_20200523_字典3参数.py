import unittest
from time import sleep
from selenium import webdriver
from ddt import  ddt,data,feed_data,unpack

@ddt
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.base_url = 'https://www.baidu.com'

    def baidu_search(self,search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(3)

    # 参数化使用方式三 字典
    @data({'search_key':'selenium'},{'search_key':'ddt'},{'search_key':'python'})
    @unpack
    def test_search3(self,search_key):
        print('第三组测试用例：',search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+'_百度搜索')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

