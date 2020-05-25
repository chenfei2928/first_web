from selenium import webdriver
wd = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
wd.implicitly_wait(5)
wd.get('http://fr.soundhw.com:9999/')

wd.maximize_window()

wd.switch_to.frame('reportFrame')

wd.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/input').send_keys('admin')
wd.find_element_by_xpath('//*[@id="wrapper"]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[2]/input').send_keys('123.com')
wd.find_element_by_xpath('//*[@id="wrapper"]/div/div[2]/div/div/div/div[6]/div/div[1]').click()

#wd.find_element_by_css_selector('.bi-absolute-layout > input[placeholder="用户名"]')


