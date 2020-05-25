from selenium import webdriver
from PIL import Image
import pytesseract
import re
import time

wb = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver') #加载驱动
wb.get('http://192.168.10.233:8080/marsCloud/loginController.do?login')
wb.maximize_window()
wb.implicitly_wait(5) # 隐式等待


def security_code(wb):
    wb.save_screenshot('D:\\security_code\\printscreen.png')  # 截屏
    imgelement = wb.find_element_by_id('randCodeImage')  # 定位验证码
    location = imgelement.location  # 获取验证码x,y坐标
    # print(location)
    size = imgelement.size  # 验证码高度、宽度、
    # print(size)

    left = int(location['x'] + 246)
    top = int(location['y'] + 75)
    right = int(location['x'] + size['width'] + 263)
    bottom = int(location['y'] + size['height'] + 83)

    img = Image.open('D:\\security_code\\printscreen.png').crop((left, top, right, bottom))  # 打开截图
    img2 = img.convert('RGB')
    img2.save('D:\\security_code\\save.png')
    code = pytesseract.image_to_string(Image.open('D:\\security_code\\save.png'))
    print(code.strip())

    # 正则表达式去除空格或其他特殊符号
    b = ''
    for i in code.strip():
        pattern = re.compile(r'[a-zA-Z0-9]')
        m = pattern.search(i)
        if m != None:
            b += i
    print(b)
    return b

def add_document(wb):
    wb.switch_to.default_content()
    wb.find_element_by_xpath('/html/body/div[4]/nav/div[2]/div[1]/ul/li[3]/a').click()  # 项目管理节点 点击
    wb.find_element_by_xpath('//*[@id="side-menu"]/li[3]/ul/li[1]/a').click()  # 项目信息管理 点击
    # 新增项目信息
    wb.switch_to.frame('iframe1')  # 切换窗口

    wb.find_element_by_xpath('//*[@id="addbuttom"]/span/span').click()  # 添加按钮

    wb.switch_to.default_content()

    xck = wb.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
    # xpath 定位到新窗口对应iframe

    wb.switch_to.frame(xck)  # 切换到新窗口 iframe

    wb.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[1]/td[4]/input').send_keys('五道口')  # 项目简称

    wb.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[2]/td[2]/input').send_keys('五道口项目')  # 项目名称

    from selenium.webdriver.support.ui import Select  # 导入Select类
    select = Select(wb.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[2]/td[4]/select'))  # 创建Select对象
    select.select_by_visible_text('城区+村镇')  # 项目类型

    wb.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[3]/td[2]/input').send_keys('曹操')  # 项目负责人
    wb.find_element_by_xpath('/html/body/div[1]/div[2]/form/table/tbody/tr[3]/td[4]/input').send_keys(
        '18612345678')  # 项目负责人电话

    wb.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[4]/td[2]/input').send_keys('许褚')  # 云平台负责人

    wb.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[4]/td[4]/input').send_keys('18512345678')  # 云平台负责人电话
    wb.find_element_by_xpath('//*[@id="standardWorkTime"]').send_keys('8')  # 标准工作时间，小时

    select2 = Select(wb.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[5]/td[4]/select'))  # 创建Select2对象
    select2.select_by_visible_text('正式运营')  # 运营状态

    select3 = Select(wb.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[6]/td[2]/select[1]'))  # 创建Select3对象
    select3.select_by_visible_text('北京市')  # 省

    select4 = Select(wb.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[6]/td[2]/select[2]'))  # 创建Select4对象
    select4.select_by_visible_text('市辖区')  # 市

    select5 = Select(wb.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[6]/td[2]/select[3]'))  # 创建Select4对象
    select5.select_by_visible_text('海淀区')  # 区

    wb.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[6]/td[2]/input[5]').send_keys('智造大街A座')  # 详细地址

    wb.find_element_by_xpath('//*[@id="lng"]').send_keys('116.397128')  # 经度
    wb.find_element_by_xpath('//*[@id="lat"]').send_keys('39.916527')  # 维度
    wb.find_element_by_xpath('//*[@id="formobj"]/table/tbody/tr[8]/td[2]/textarea').send_keys(
        '滚滚长江东逝水, 浪花淘尽英雄。 是非成败转头空。 青山依旧在, 几度夕阳红。 白发渔樵江渚上, 惯看秋月春风。')  # 项目简介

    wb.switch_to.default_content()

    wb.find_element_by_xpath(
        '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/input[1]').click()  # 提交
    # 提交无效，应该是对应不同frame。下周一对比下iframe路径。
    time.sleep(3)

    print('--项目信息录入完成--')

def login(wb):

    wb.find_element_by_id('userName').send_keys('admin')
    wb.find_element_by_id('password').send_keys('123456')
    yzm = security_code(wb)
    wb.find_element_by_id('randCode').send_keys(yzm)
    wb.find_element_by_id('but_login').click()



login(wb)
add_document(wb)



