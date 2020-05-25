from selenium.webdriver import Chrome
import time

wd = Chrome()
wd.get('https://www.baidu.com')
wd.maximize_window()
wd.find_element_by_xpath('//*[@id="s-usersetting-top"]').click()  # 设置
wd.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]').click() # 搜索设置

time.sleep(2)

wd.find_element_by_xpath('//*[@id="se-setting-7"]/a[2]').click()  # 保存设置

alert = wd.switch_to.alert  # 获取警告框

alert_text = alert.text
print(alert_text)  # 输出警告内容

alert.accept() # 接受警告内容


