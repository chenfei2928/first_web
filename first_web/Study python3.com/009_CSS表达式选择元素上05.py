from selenium import webdriver
wb = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wb.implicitly_wait(5)

wb.get('http://cdn1.python3.vip/files/selenium/sample1.html')


# elements = wb.find_elements_by_css_selector('#container > div')  #  大于号 >直接子节点

#elements = wb.find_elements_by_css_selector('[href="http://www.miitbeian.gov.cn"]')

elements = wb.find_elements_by_css_selector('[href]')

for element in elements:
    print('----------------------')
    print(element.get_attribute('outerHTML'))

wb.quit()

