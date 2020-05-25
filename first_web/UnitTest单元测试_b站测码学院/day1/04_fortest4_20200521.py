import unittest
from selenium import webdriver
import time
from ddt import ddt,data,unpack

@ddt
class forTestTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # @data('虚竹','小龙女')
    # def test_1(self,txt):
    #     self.driver.find_element_by_id('kw').send_keys(txt)
    #     self.driver.find_element_by_id('su').click()

    @data(('二哈','三十而立'),('异常帅气的虚竹','kkkkkkkkkkk'))
    @unpack # 解包
    def test_2(self,txt,p):
        print(txt)
        print(p)
        print('**************************')
if __name__ == '__main__':
    unittest.main()