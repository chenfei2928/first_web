from selenium import webdriver
wd = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wd.implicitly_wait(5)

wd.get('http://cdn1.python3.vip/files/selenium/test1.html')

elements = wd.find_elements_by_xpath('/html/body/div')
      # 绝对路径 /
#  相对路径 //
# 所有子节点  *


for element in elements:
    print('--------------------')
    print(element.get_attribute('outerHTML'))

wd.quit()
