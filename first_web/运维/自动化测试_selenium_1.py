from selenium import webdriver
wd = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wd.implicitly_wait(5)
wd.get('http://www.baidu.com')
print(wd.title)

print(wd.current_url)

#ele = wd.find_element_by_id('kw')  # id查找元素
#ele = wd.find_element_by_name('wd')  # name 查找元素
#ele = wd.find_element_by_class_name('s_ipt')  # class值 查找元素
#ele1 = wd.find_element_by_tag_name('input')   # 当多个相同值存在时，无效。


print(ele.size)
print(ele1.size)

ele.send_keys('111\n')

# ele.clear()       # 清空输入框内容
# ele.send_keys('麦子学院\n')   # 输入字符串

# wd.back()  # 返回上一个搜索

# wd.title 判断访问是否有效
# wd.current_url  判断访问是否有效