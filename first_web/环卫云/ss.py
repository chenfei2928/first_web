from selenium.webdriver import Chrome

wd = Chrome()

wd.get('https://www.baidu.com')
wd.find_element_by_id('kw').send_keys('自动化\n')


