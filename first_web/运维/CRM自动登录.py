from selenium import webdriver
wd = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wd.implicitly_wait(5)
wd.get('http://crm.soundhw.com:8888/indexbusiness.jsp')

wd.maximize_window()


wd.find_element_by_xpath('//*[@id="username"]').send_keys('gmsdxhw')
wd.find_element_by_xpath('//*[@id="password"]').send_keys('crm123456')
wd.find_element_by_xpath('//*[@id="btnSubmit"]').click()



