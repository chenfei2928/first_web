from selenium import webdriver
from PIL import Image
import pytesseract
import re
import time
from selenium.webdriver.support.ui import Select


def security_code(wb):
    wb.save_screenshot('D:\\security_code\\printscreen.png')  # 截屏
    imgelement = wb.find_element_by_id('randCodeImage')  # 定位验证码
    location = imgelement.location  # 获取验证码x,y坐标
    print(location)
    size = imgelement.size  # 验证码高度、宽度、
    print(size)

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


def login(wb):
    wb.find_element_by_id('userName').send_keys('admin')
    wb.find_element_by_id('password').send_keys('123456')
    yzm = security_code(wb)
    wb.find_element_by_id('randCode').send_keys(yzm)
    wb.find_element_by_id('but_login').click()

def del_document(wb):
    wb.switch_to.default_content()
    wb.find_element_by_xpath('/html/body/div[4]/nav/div[2]/div[1]/ul/li[3]/a').click()  # 项目管理节点 点击
    wb.find_element_by_xpath('//*[@id="side-menu"]/li[3]/ul/li[1]/a').click()  # 项目信息管理 点击
    # 新增项目信息
    wb.switch_to.frame('iframe1')  # 切换窗口
    wb.find_element_by_xpath('//*[@id="soProjectInfoListForm"]/span[1]/span[2]/input').send_keys('五道口')  # 输入查询项目名称
    wb.find_element_by_xpath('//*[@id="soProjectInfoListForm"]/span[2]/span/a[1]/span/span').click()  #点击查询按钮

    wb.find_element_by_xpath('/html/body/div/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div/table/tbody/tr/td[2]/div/input').click()
    # 点击全选复选框

    wb.find_element_by_xpath('//*[@id="soProjectInfoListtb"]/div[2]/span/a[4]/span/span').click()  # 点击删除按钮
    wb.switch_to.default_content()
    wb.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/input[1]').click() # 确定删除
    time.sleep(10)

def main():
    wb = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
    wb.get('http://192.168.10.233:8080/marsCloud/loginController.do?login')
    wb.maximize_window()
    wb.implicitly_wait(5)

    login(wb)
    del_document(wb)
    print('---单据删除完成---')

main()