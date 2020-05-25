from selenium import webdriver
wd = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wd.implicitly_wait(5)

wd.get('http://cdn1.python3.vip/files/selenium/test2.html')

# 导入Select类
from selenium.webdriver.support.ui import Select

# 创建Select对象
select = Select(wd.find_element_by_id("ss_multi"))

# 清除所有 已经选中 的选项
select.deselect_all()

# 选择小雷老师 和 小凯老师
select.select_by_visible_text("小雷老师")
select.select_by_visible_text("小凯老师")

