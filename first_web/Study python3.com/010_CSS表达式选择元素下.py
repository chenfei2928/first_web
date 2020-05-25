from selenium import webdriver
wb = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wb.implicitly_wait(5)

wb.get('http://cdn1.python3.vip/files/selenium/sample1b.html')

elements = wb.find_elements_by_css_selector('span:nth-child(2)')

for element in elements:
    print('----------------------')
    print(element.get_attribute('outerHTML'))

wb.quit()

