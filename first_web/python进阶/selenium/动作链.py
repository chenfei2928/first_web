from selenium import webdriver
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome()
url ='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)

browser.switch_to.frame('iframeResult')  # 切换iframe

fr = browser.find_element_by_css_selector('#draggable') # 源框
to = browser.find_element_by_css_selector('#droppable') # 目标框

actions = ActionChains(browser)
actions.click_and_hold(fr)
time.sleep(3)
for i in range(5):
    actions.move_by_offset(xoffset =17,yoffset=0).perform()  # perform 执行
    time.sleep(1)

actions.release()  #释放
