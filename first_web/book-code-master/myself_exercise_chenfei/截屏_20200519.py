from selenium.webdriver import Chrome

wd = Chrome()

wd.get('https://www.baidu.com')

wd.save_screenshot('./baidu_img.png')