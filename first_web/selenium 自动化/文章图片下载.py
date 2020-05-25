from selenium.webdriver import Chrome
import requests
import time
from selenium.webdriver.chrome.options import Options

# 无头浏览器----
chrome_option = Options()
chrome_option.add_argument('headless')  # headless前 是否加-- 好像效果一样
web = Chrome(options=chrome_option)


web.get('https://www.jianshu.com/p/b4155eeabaa6')

img1 = web.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div[1]/section[1]/article/div[3]/div[1]/div[2]/img').get_attribute('data-original-src')
time.sleep(1)

img1_addr = 'https:'+img1


with open("tupian1.jpg",mode='wb') as f:
    f.write(requests.get(img1_addr).content)


web.quit()
