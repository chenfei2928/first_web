from selenium import webdriver
wb = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wb.implicitly_wait(5)

wb.get('http://cdn1.python3.vip/files/selenium/sample2.html')

# 切换到Frame里面去
wb.switch_to_frame('frame1')

elements = wb.find_elements_by_css_selector('.plant')

for element in elements:
    print('----------------------')
    print(element.get_attribute('outerHTML'))
# 切换到外层
wb.switch_to_default_content()

wb.find_element_by_id('outerbutton').click()

#wb.quit()

