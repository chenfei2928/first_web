
from selenium import webdriver
import pickle
import time

driver =webdriver.Chrome(executable_path='D:\develop_study\chromedriver\chromedriver')

driver.get('https://www.douban.com')
#删掉cookies
driver.delete_all_cookies()

with open('D:/test_cookies/db_cookie_1','rb') as f:
    cookies = pickle.load(f)
for cookie in cookies:
    driver.add_cookie(cookie)
    print(cookie)

    # cookie = pickle.load(f)
    # driver.add_cookie(cookie)
    # print(cookie)



#带我们保存的cookie访问豆瓣
driver.get('https://www.douban.com')

print('done')

#有问题，需继续调试
