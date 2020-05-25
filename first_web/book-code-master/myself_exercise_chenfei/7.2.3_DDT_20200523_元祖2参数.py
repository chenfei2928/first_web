import unittest
from time import sleep
from selenium import webdriver
from ddt import  ddt,data,file_data,unpack

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

    #参数化使用方式二 元祖
    @data(('case1','selenium'),('case2','ddt'),('case3','python'))
    @unpack
    def test_search2(self,case,search_key):
        print('第二组测试用例 列表',case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+'_百度搜索')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

