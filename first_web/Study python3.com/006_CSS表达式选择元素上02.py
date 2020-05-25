from selenium import webdriver
wb = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wb.implicitly_wait(10)

wb.get('http://cdn1.python3.vip/files/selenium/sample1.html')

#elements = wb.find_elements_by_css_selector('span')

elements = wb.find_elements_by_css_selector('#searchtext')  # id用 # 号

for element in elements:
    print(element.get_attribute('outerHTML'))

wb.quit()

