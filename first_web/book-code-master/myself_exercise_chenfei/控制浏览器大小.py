from selenium.webdriver import Chrome
import time
wd = Chrome()
wd.get('https://www.baidu.com')

print('设置浏览器大小')
wd.maximize_window()
# wd.find_element_by_id('kw').send_keys('selenium\n')
# time.sleep(3)
# wd.back()
# time.sleep(3)
# wd.refresh()

# search = wd.find_element_by_id('kw')
# print(search.size)
#
#
# sub = wd.find_element_by_xpath('//*[@id="s-bottom-layer-right"]/a/span')
# print(sub.text)
#
# time.sleep(10)
# wd.quit()

att = wd.find_element_by_id('kw').get_attribute('type')
print(att)


rssult = wd.find_element_by_id('kw').is_displayed()
print(rssult)