from selenium import webdriver
from selenium.webdriver import ActionChains  # 动作链

wd = webdriver.Chrome()
wd.maximize_window()
wd.get('https://www.baidu.com')

# above = wd.find_element_by_link_text('设置')
above = wd.find_element_by_xpath('//*[@id="s-usersetting-top"]')

ActionChains(wd).move_to_element(above).perform()

