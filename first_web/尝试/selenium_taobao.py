from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

web = webdriver.Chrome(executable_path='D:\develop_study\chromedriver\chromedriver')
web.get('https://www.taobao.com/')

web.find_element_by_xpath('//*[@id="q"]').send_keys('篮球',Keys.ENTER)

while web.current_url.startswith("https://login.taobao.com/"):
    print('请用户扫码或输入账号密码登陆')
    time.sleep(4)

print('淘宝网登陆成功')

