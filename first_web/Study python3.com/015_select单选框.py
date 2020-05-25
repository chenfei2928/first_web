from selenium import webdriver
wd = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wd.implicitly_wait(5)

wd.get('http://cdn1.python3.vip/files/selenium/test2.html')


from selenium.webdriver.support.ui import Select


select = Select(wd.find_element_by_id('ss_single'))


select.select_by_visible_text("小雷老师")
