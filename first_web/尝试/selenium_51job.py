from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

web = webdriver.Chrome(executable_path='D:\develop_study\chromedriver\chromedriver')
web.get('https://www.51job.com/')

web.find_element_by_xpath('//*[@id="kwdselectid"]').send_keys('电工',Keys.ENTER)  # 发送键盘信息
div_list = web.find_element_by_id("resultList").find_elements_by_class_name('el')[1:]
for div in div_list:
    a = div.find_element_by_xpath('p/span/a')
    a.click()
    time.sleep(1)
    #切换窗口
    web.switch_to.window((web.window_handles[-1]))
    details = web.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div')
    print(details.text)
    web.close()
    web.switch_to.window(web.window_handles[0])
    time.sleep(2)
    print('----------------------------------------------------')

