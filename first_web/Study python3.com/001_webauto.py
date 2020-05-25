# 根据ID选择元素、定位元素

from selenium import webdriver

#调用浏览器驱动
wb = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')

#访问目标网站

wb.get('https://www.baidu.com')

#根据id选择元素，返回的就是该元素对应的WebElement对象

element = wb.find_element_by_id('kw')

# 通过该WebElement对象，就可以对页面元素进行操作了

# 比如输入字符串到 这个输入框中
element.send_keys('白夜黑羽')

# 找到百度一下按钮
element = wb.find_element_by_id('su')

# 点击
element.click()

wb.implicitly_wait(10)


# id 为 1 的元素 就是第一个搜索结果
element = wb.find_element_by_id('1')

# 打印出 第一个搜索结果的文本字符串
print (element.text)

