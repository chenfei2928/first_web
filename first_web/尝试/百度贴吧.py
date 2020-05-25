from selenium import webdriver
browser = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
browser.implicitly_wait(5)


browser.get('https://tieba.baidu.com/index.html?qq-pf-to=pcqq.group')

browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div/div/div[2]/div/div[1]/form/input[1]').send_keys('轮胎')