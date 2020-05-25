
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 键盘
import time


wd = webdriver.Chrome()
wd.maximize_window()
wd.get('https://www.baidu.com')

wd.find_element_by_id('kw').send_keys('seleniummm')
time.sleep(5)
wd.find_element_by_id('kw').send_keys(Keys.BACKSPACE)  # 两个backspace 好像没区别
wd.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)

wd.find_element_by_id('kw').send_keys(Keys.SPACE)  #空格
wd.find_element_by_id('kw').send_keys('python')

wd.find_element_by_id('kw').send_keys(Keys.ENTER)  # 回车
