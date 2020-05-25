import unittest
import time
from selenium import webdriver

class testBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.base_url = 'https://www.baidu.com'


    def setUp(self) -> None:
        print('我没用了吗，开始')

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
        print('我没用了吗，那我走了')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()


"""
1.用setUp与setUpClass区别

    setup():每个测试case运行前运行
    teardown():每个测试case运行完后执行
    setUpClass():必须使用@classmethod 装饰器,所有case运行前只运行一次
    tearDownClass():必须使用@classmethod装饰器,所有case运行完后只运行一次

2.@是修饰符，classmethod是python里的类方法

"""