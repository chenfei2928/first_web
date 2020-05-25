from selenium import webdriver
from selenium.webdriver.chrome.options import Options
req_url = "https://www.baidu.com"
options=Options()
#设置chrome浏览器无界面模式
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options)

# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


# 开始请求
browser.get(req_url)
#打印页面源代码
print(browser.page_source)
#关闭浏览器
browser.close()
#关闭chreomedriver进程
browser.quit()
