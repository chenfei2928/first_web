from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path='D:\develop_study\chromedriver\chromedriver') # 打开浏览器
driver.maximize_window()    #浏览器最大化
driver.get('https://www.yuanrenxue.com') # 打开目标网站

#定位右上角搜索图标并点击
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,'search-show'))
    )
    element.click()
except:
    print('not locate serarch-show')
    driver.quit()



driver.find_element_by_class_name('search-show').click()
# 找到输入框
search = driver.find_element_by_class_name("search-input")
# 输入 Python教程
search.send_keys(u'python教程')
search.send_keys(Keys.ENTER)


#time.sleep(30)

element = driver.find_element_by_tag_name('body')
time.sleep(10)
element.send_keys(Keys.DOWN)
time.sleep(10)
element.send_keys(Keys.DOWN)
time.sleep(5)
driver.quit()




