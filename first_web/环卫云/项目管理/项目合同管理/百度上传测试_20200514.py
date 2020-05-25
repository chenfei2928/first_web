from selenium import webdriver
import time

wd = webdriver.Chrome()  # 加载Chrome浏览器对应selenium驱动
wd.maximize_window()  #最大化浏览器
wd.get('https://www.baidu.com/')  #打开目标网址

wd.find_element_by_xpath('//*[@id="form"]/span[1]/span[1]').click()  # 按图片搜索
time.sleep(2)

# wd.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[2]/input').send_keys(r'C:\Users\Administrator\Desktop\临时\2223.jepg')
# wd.find_element_by_class_name('upload-pic').send_keys(r'C:\Users\Administrator\Desktop\临时\2223.jepg')
wd.find_element_by_class_name('upload-pic').send_keys(r'C:\Users\Administrator\Desktop\临时\2223.jpeg')

