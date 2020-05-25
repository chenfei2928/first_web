"""
使用 setUpModule/ tearDownModule 减少浏览器的启动
"""
import unittest
from time import sleep
from selenium import webdriver


class Browser:
    driver = None
    base_url = None


def setUpModule():
    Browser.driver = webdriver.Chrome()
    Browser.base_url = "https://www.baidu.com"


def tearDownModule():
    Browser.driver.quit()


def baidu_search(search_key):
    Browser.driver.get(Browser.base_url)
    Browser.driver.find_element_by_id("kw").send_keys(search_key)
    Browser.driver.find_element_by_id("su").click()
    sleep(2)


class TestBaidu(unittest.TestCase):
    """百度搜索测试"""

    def test_search_key_selenium(self):
        '''搜索关键字：selenium '''
        search_key = "selenium"
        baidu_search(search_key)
        self.assertEqual(Browser.driver.title, search_key + "_百度搜索")

    def test_search_key_unttest(self):
        '''搜索关键字：unittest '''
        search_key = "unittest"
        baidu_search(search_key)
        self.assertEqual(Browser.driver.title, search_key + "_百度搜索")


class TestBaidu2(unittest.TestCase):
    """百度搜索测试2"""
    def test_search_key_python(self):
        """搜索关键字：python"""
        search_key = "python"
        baidu_search(search_key)
        self.assertEqual(Browser.driver.title, search_key + "_百度搜索")


if __name__ == '__main__':
    unittest.main()
