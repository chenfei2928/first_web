from selenium import webdriver
import time
from PIL import Image
import pytesseract
import re

wb = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wb.get('http://192.168.10.233:8080/marsCloud/loginController.do?login')

wb.maximize_window()
wb.implicitly_wait(5)
wb.find_element_by_id('userName').send_keys('admin')
wb.find_element_by_id('password').send_keys('123456')


wb.save_screenshot('D:\\security_code\\printscreen.png')  # 截屏
imgelement = wb.find_element_by_id('randCodeImage')  # 定位验证码
location = imgelement.location  # 获取验证码x,y坐标
print(location)
size = imgelement.size # 验证码高度、宽度、
print(size)

left = int(location['x']+246)
top = int(location['y']+75)
right = int(location['x']+size['width']+263)
bottom = int(location['y']+size['height']+83)


img = Image.open('D:\\security_code\\printscreen.png').crop((left,top,right,bottom)) #打开截图
img2 = img.convert('RGB')
img2.save('D:\\security_code\\save.png')
code = pytesseract.image_to_string(Image.open('D:\\security_code\\save.png'))
print(code.strip())


# 正则表达式去除空格或其他特殊符号
b=''
for i in code.strip():
    pattern = re.compile(r'[a-zA-Z0-9]')
    m = pattern.search(i)
    if m!=None:
        b+=i
    #输出去特殊符号以后的验证码
print (b)


wb.find_element_by_id('randCode').send_keys(b)
wb.find_element_by_id('but_login').click()
#
# cookie = wb.get_cookies()
# print(cookie)

# wb.find_element_by_xpath('//*[@id="side-menu"]/li[3]/a/span[1]').click()
# //*[@id="side-menu"]/li[3]/a
# /html/body/div[4]/nav/div[2]/div[1]/ul/li[3]/a

wb.find_element_by_xpath('/html/body/div[4]/nav/div[2]/div[1]/ul/li[3]/a').click()
wb.find_element_by_xpath('//*[@id="side-menu"]/li[3]/ul/li[1]/a').click()  # 项目信息管理 点击
