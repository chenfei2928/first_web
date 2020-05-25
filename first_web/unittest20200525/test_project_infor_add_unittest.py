import unittest
import time
from selenium import webdriver

from PIL import Image
import pytesseract
import re



class testhuanweiyun(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url ='http://192.168.10.233:8080/marsCloud/loginController.do?login'

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        print('开始测试---------------------')

    def tearDown(self) -> None:
        print('结束测试-------------------- ')

    def login(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('userName').send_keys('admin')
        self.driver.find_element_by_id('password').send_keys('123456')
        self.driver.find_element_by_id('randCode').send_keys('0000')
        self.driver.find_element_by_id('but_login').click()

    def test_add_document(self):
        login(self)
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath('/html/body/div[4]/nav/div[2]/div[1]/ul/li[3]/a').click()  # 项目管理节点 点击
        self.driver.find_element_by_xpath('//*[@id="side-menu"]/li[3]/ul/li[1]/a').click()  # 项目信息管理 点击
        # 新增项目信息
        self.driver.switch_to.frame('iframe1')  # 切换窗口

        self.driver.find_element_by_xpath('//*[@id="addbuttom"]/span/span').click()  # 添加按钮

        self.driver.switch_to.default_content()

        xck = wb.find_element_by_xpath(
            '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
        # xpath 定位到新窗口对应iframe

        self.driver.switch_to.frame(xck)  # 切换到新窗口 iframe

        self.driver.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[1]/td[4]/input').send_keys('五道口')  # 项目简称

        self.driver.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[2]/td[2]/input').send_keys('五道口项目')  # 项目名称

        from selenium.webdriver.support.ui import Select  # 导入Select类
        select = Select(self.driver.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[2]/td[4]/select'))  # 创建Select对象
        select.select_by_visible_text('城区+村镇')  # 项目类型

        self.driver.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[3]/td[2]/input').send_keys('曹操')  # 项目负责人
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/table/tbody/tr[3]/td[4]/input').send_keys(
            '18612345678')  # 项目负责人电话

        self.driver.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[4]/td[2]/input').send_keys('许褚')  # 云平台负责人

        self.driver.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[4]/td[4]/input').send_keys(
            '18512345678')  # 云平台负责人电话
        self.driver.find_element_by_xpath('//*[@id="standardWorkTime"]').send_keys('8')  # 标准工作时间，小时

        select2 = Select(self.driver.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[5]/td[4]/select'))  # 创建Select2对象
        select2.select_by_visible_text('正式运营')  # 运营状态

        select3 = Select(
            self.driver.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[6]/td[2]/select[1]'))  # 创建Select3对象
        select3.select_by_visible_text('北京市')  # 省

        select4 = Select(
            self.driver.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[6]/td[2]/select[2]'))  # 创建Select4对象
        select4.select_by_visible_text('市辖区')  # 市

        select5 = Select(
            self.driver.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[6]/td[2]/select[3]'))  # 创建Select4对象
        select5.select_by_visible_text('海淀区')  # 区

        self.driver.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[6]/td[2]/input[5]').send_keys('智造大街A座')  # 详细地址

        self.driver.find_element_by_xpath('//*[@id="lng"]').send_keys('116.397128')  # 经度
        self.driver.find_element_by_xpath('//*[@id="lat"]').send_keys('39.916527')  # 维度
        self.driver.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[8]/td[2]/textarea').send_keys(
            '滚滚长江东逝水, 浪花淘尽英雄。 是非成败转头空。 青山依旧在, 几度夕阳红。 白发渔樵江渚上, 惯看秋月春风。')  # 项目简介

        self.driver.switch_to.default_content()

        self.driver.find_element_by_xpath(
            '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/input[1]').click()  # 提交
        # 提交无效，应该是对应不同frame。下周一对比下iframe路径。
        time.sleep(3)

        print('--项目信息录入完成--')

if __name__ == '__main__':
    unittest.main()