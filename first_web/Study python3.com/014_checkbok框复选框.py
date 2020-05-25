from selenium import webdriver
wd = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wd.implicitly_wait(5)

wd.get('http://cdn1.python3.vip/files/selenium/test2.html')

# 先把 已经选中的选项全部点击一下
elements = wd.find_elements_by_css_selector(
  '#s_checkbox input[checked="checked"]')

for element in elements:
    element.click()

# 再点击 小雷老师
wd.find_element_by_css_selector(
  "#s_checkbox input[value='小雷老师']").click()