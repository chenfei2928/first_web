from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Administrator\\AppData\Local\\Google\\Chrome\\User Data")
        # add_argument()方法里填你Chrome浏览器保存Cookies的路径。


options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
        # add_experimental_option()方法是访问https的网站，Selenium可能会报错，使用这个方法可以忽略报错。

driver = webdriver.Chrome(executable_path="D:\develop_study\chromedriver\chromedriver",options=options)

driver.maximize_window()

driver.get('https://www.weibo.com')

print(driver.get_cookies())
    # get_cookies()方法可以得到当前访问网站的Cookies。