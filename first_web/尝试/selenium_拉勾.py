from selenium.webdriver import  Chrome
from selenium.webdriver.common.keys import Keys
import time
web = Chrome()   # 把chromedriver.exe 放到 python路径下，就不用写路径了。
#web.get('https://www.baidu.com')

web.get('https://www.lagou.com')
web.find_element_by_xpath('//*[@id="cboxClose"]').click()
time.sleep(2)
web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)
time.sleep(1)
web.find_element_by_xpath('/html/body/div[8]/div/div[2]').click() #给也不要


alist = web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li/div[1]/div[1]/div[1]/a/h3')

print(len(alist))

for a in alist:
    a.click()
    time.sleep(2)
    web.switch_to.window(web.window_handles[-1])  #最后一个窗口
    job_desc = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]').text
    print(job_desc)
    print('----------------------------------------------------------------------------')
    web.close()
    web.switch_to.window((web.window_handles[0]))  #切换会第一个窗口

