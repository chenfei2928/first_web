from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path='D:\develop_study\chromedriver\chromedriver')
driver.maximize_window()
driver.get('https://www.yuanrenxue.com')
time.sleep(5)
element = driver.find_element_by_tag_name('body')
element.send_keys(Keys.CONTROL,'a')

element.send_keys(Keys.CONTROL,'w')  #关闭窗口无效。
