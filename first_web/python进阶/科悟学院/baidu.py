from selenium import webdriver
def login():
    wd = webdriver.Chrome()
    wd.maximize_window()
    wd.get('https://www.baidu.com')