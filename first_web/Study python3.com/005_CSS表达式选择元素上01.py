from selenium import webdriver
wb = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wb.implicitly_wait(10)

wb.get('http://cdn1.python3.vip/files/selenium/sample1.html')

element = wb.find_element_by_css_selector('.plant')

print(element.get_attribute('outerHTML'))

wb.quit()

