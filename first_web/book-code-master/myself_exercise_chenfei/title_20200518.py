from selenium import webdriver
import time


wd = webdriver.Chrome()
wd.maximize_window()
wd.get('https://www.baidu.com')
title = wd.title
print(title)

url = wd.current_url

print(url)
