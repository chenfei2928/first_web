from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import requests
from PIL import Image
import pytesseract
import re

wd = webdriver.Chrome()  # 加载Chrome浏览器对应selenium驱动
wd.maximize_window()  #最大化浏览器
wd.get('http://192.168.10.233:8080/marsCloud/loginController.do?login')  #打开目标网址
wd.implicitly_wait(5)  # 隐式等待

def login():  # 登陆
    wd.find_element_by_id('userName').send_keys('admin')
    wd.find_element_by_name('password').send_keys('123456')
    yzm = security_code()
    wd.find_element_by_css_selector('#randCode').send_keys(yzm)
    wd.find_element_by_class_name('bigger-110').click()

def security_code():
    wd.save_screenshot('D:\\security_code\\printscreen.png')  # 截屏
    imgelement = wd.find_element_by_id('randCodeImage')  # 定位验证码
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

def add_contract(): # 添加项目合同信息
    wd.find_element_by_xpath('//*[@id="side-menu"]/li[3]/a').click()    # 项目管理 目录
    wd.find_element_by_xpath('//*[@id="side-menu"]/li[3]/ul/li[2]/a/span').click()     # 项目合同管理

    wd.switch_to.frame('iframe2')  # 切换iframe
    wd.find_element_by_xpath('//*[@id="contractInfoListForm"]/span[1]/span[2]/input').send_keys('五道口项目\n')
    wd.find_element_by_xpath('//*[@id="contractInfoListForm"]/span[1]/span[2]/div/p').click()

    wd.find_element_by_xpath('//*[@id="contractInfoListtb"]/div[2]/span/a[1]/span/span').click()  #录入

    wd.switch_to.default_content()

    lurukuang = wd.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')

    wd.switch_to.frame(lurukuang)
    time.sleep(0.5)

#合同基本信息

    wd.find_element_by_xpath('//*[@id="formobj"]/div/div[4]/div/div[2]/input').send_keys('8888') #服务户数
    wd.find_element_by_xpath('//*[@id="formobj"]/div/div[5]/div/div[2]/input').send_keys('16888')  # 服务人口数
    wd.find_element_by_xpath('//*[@id="formobj"]/div/div[6]/div/div[2]/input').send_keys('五道口307垃圾桶清理') # 合同名称

    contract_type_select = Select(wd.find_element_by_xpath('//*[@id="formobj"]/div/div[7]/div/div[2]/select'))  # 合同类型
    contract_type_select.select_by_visible_text('城区合同')

    wd.find_element_by_xpath('//*[@id="formobj"]/div/div[8]/div/div[2]/input').send_keys(2)   #合同年限 number类型
    wd.find_element_by_xpath('//*[@id="totalAmount"]').send_keys('22.2')  # 总金额 万元
    wd.find_element_by_xpath('//*[@id="formobj"]/div/div[10]/div/div[2]/input').send_keys('11.1')   #年度金额 万元
    wd.find_element_by_xpath('//*[@id="startDate"]').send_keys('2020-05-13')# 合同开始时间
    wd.find_element_by_xpath('//*[@id="endDate"]').send_keys('2022-05-12')  # 合同结束时间
    wd.find_element_by_xpath('//*[@id="formobj"]/div/div[13]/div/div[2]/input').send_keys('2020-04-10') # 中标日期
    wd.find_element_by_xpath('//*[@id="formobj"]/div/div[14]/div/div[2]/input').send_keys('2020-05-14') # 进场时间
    wd.find_element_by_xpath('//*[@id="formobj"]/div/div[15]/div/div[2]/input').send_keys(3) # 环卫人数
    wd.find_element_by_xpath('//*[@id="formobj"]/div/div[16]/div/div[2]/input').send_keys(1) # 车辆数量
    wd.find_element_by_xpath('//*[@id="formobj"]/div/div[17]/div/div[2]/input').send_keys('0.003')  # 服务面积（万平方米）

    fwfw = wd.find_element_by_xpath('//*[@id="formobj"]/div/div[18]/div/div[2]') #服务范围
    fwfw.find_element_by_xpath('div[1]/ins').click()  # 人工清扫保洁
    # fwfw.find_element_by_xpath('div[2]/ins').click()  # 机械洗扫
    fwfw.find_element_by_xpath('div[3]/ins').click() # 垃圾收运

    wd.find_element_by_class_name('webuploader-element-invisible').send_keys(r'C:\Users\Administrator\Desktop\临时\2223.jpeg')
    # wd.find_element_by_xpath('//*[@id="info_btn_sub"]').click()   # 合同基本信息保存
        # 每保存一次 生成一条记录。

# 人工清扫保洁
    road_grade = Select(wd.find_element_by_xpath('//*[@id="shfit_emp"]/div[2]/div/div[2]/select')) # 道理等级
    road_grade.select_by_visible_text('背街小巷')
    time.sleep(1)
    wd.find_element_by_xpath('//*[@id="empshift"]/tr[2]/td[6]/input').click() # 新增
    time.sleep(1)

    wd.find_element_by_xpath('/html/body/div[1]/div[2]/form[2]/div/div[3]/table/tbody/tr[3]/td[1]/input').send_keys('白日班次2') #班次名称
    wd.find_element_by_xpath('/html/body/div[1]/div[2]/form[2]/div/div[3]/table/tbody/tr[3]/td[2]/input').send_keys('07:00')  # 开始时间-夏季
    wd.find_element_by_xpath('/html/body/div[1]/div[2]/form[2]/div/div[3]/table/tbody/tr[3]/td[3]/input').send_keys('17:00')  # 结束时间-夏季
    wd.find_element_by_xpath('/html/body/div[1]/div[2]/form[2]/div/div[3]/table/tbody/tr[3]/td[4]/input').send_keys('07:30')  # 开始时间-冬季
    wd.find_element_by_xpath('/html/body/div[1]/div[2]/form[2]/div/div[3]/table/tbody/tr[3]/td[5]/input').send_keys('17:30')  # 结束时间-冬季
    # wd.find_element_by_xpath('/html/body/div[1]/div[2]/form[2]/div/div[3]/table/tbody/tr[3]/td[6]/input').click()  # 删除行

# 机械清扫保洁

    road_grade2 = Select(wd.find_element_by_xpath('/html/body/div[1]/div[2]/form[3]/div/div[2]/div/div[2]/select')) # 道理等级
    road_grade2.select_by_visible_text('三级道路')

    time.sleep(1)
    wd.find_element_by_xpath('//*[@id="carshift"]/tr[2]/td[6]/input').click() # 新增
    time.sleep(1)

    wd.find_element_by_xpath('//*[@id="workingShifts_car0"]').send_keys('机械清扫班次') #班次名称
    wd.find_element_by_xpath('//*[@id="startTime_car0"]').send_keys('07:01')  # 开始时间-夏季
    wd.find_element_by_xpath('//*[@id="endTime_car0"]').send_keys('17:01')  # 结束时间-夏季
    wd.find_element_by_xpath('//*[@id="startTime2_car0"]').send_keys('07:32')  # 开始时间-冬季
    wd.find_element_by_xpath('//*[@id="endTime2_car0"]').send_keys('17:31')  # 结束时间-冬季
    # wd.find_element_by_xpath('//*[@id="carshift"]/tr[3]/td[6]/input').click() # 删除

# 垃圾收运清扫
    wd.find_element_by_xpath('//*[@id="car2shift"]/tr[2]/td[6]/input').click()  # 新增
    time.sleep(1)
    wd.find_element_by_xpath('//*[@id="workingShifts_car20"]').send_keys('垃圾收运班次')  # 班次名称
    wd.find_element_by_xpath('//*[@id="startTime_car20"]').send_keys('07:02') # 开始时间-夏季
    wd.find_element_by_xpath('//*[@id="endTime_car20"]').send_keys('17:02')   # 结束时间-夏季
    wd.find_element_by_xpath('//*[@id="startTime2_car20"]').send_keys('07:33') # 开始时间-冬季
    wd.find_element_by_xpath('//*[@id="endTime2_car20"]').send_keys('17:33')   # 结束时间-冬季
    # wd.find_element_by_xpath('//*[@id="car2shift"]/tr[3]/td[6]/input').click()  # 删除行

# 提交
    wd.switch_to.default_content()
    wd.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/input[1]').click() # 提交
    print('---项目合同管理信息录入完成---')

login()
add_contract()



"""
测试细节-项目合同管理

1、子菜单名称不统一
    人工清扫保洁
    机械保洁清扫
    垃圾收运清扫
2、保存按钮太多，什么情况下用保存，什么情况下用提交
    三个子菜单，提交后好像没有保存上？？
3、父菜单级别，无法前台删除。 
4、无项目编码，无唯一标识。
"""