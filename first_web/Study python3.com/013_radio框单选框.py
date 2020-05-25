from selenium import webdriver
wd = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wd.implicitly_wait(5)

wd.get('http://cdn1.python3.vip/files/selenium/test2.html')

# 获取当前选中的元素
element = wd.find_element_by_css_selector(
  '#s_radio input[checked=checked]')
print('当前选中的是: ' + element.get_attribute('value'))

# 点选 小雷老师
wd.find_element_by_css_selector(
  '#s_radio input[value="小雷老师"]').click()