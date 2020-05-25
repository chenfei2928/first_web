from selenium import webdriver

#调用浏览器驱动
driver = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')

#登陆目标网站
driver.get('http://www.51job.com')


ele = driver.find_element_by_id('kwdselectid')

ele.send_keys('python')

ele = driver.find_element_by_id('work_position_input')

ele.click()


eles = driver.find_elements_by_css_selector(
    '#work_position_click_center_right_list_000000 em[class=on]')


for ele in eles:
    ele.click()

driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()


pass