from selenium import webdriver
wb = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wb.get('https://www.baidu.com')

element = wb.find_element_by_id('kw')

element.send_keys('白夜黑羽')

wb.find_element_by_id('su').click()

wb.implicitly_wait(10)

element = wb.find_element_by_id('1')


# print(element.get_attribute('srcid'))   # 获取元素单个属性值

# print(element.get_attribute('outerHTML'))   # 获取整个html

print(element.get_attribute('innerHTML'))    #获取内部html

print(element.get_attribute('innerText'))    #获取内部文本
print(element.get_attribute('textContent'))    #获取内部文本


wb.quit()  # 自动退出浏览器

