from selenium import webdriver
import pickle
import time

# pickle模块实现了基本的数据序列化和反序列化。
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储；
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。



driver = webdriver.Chrome(executable_path='D:\develop_study\chromedriver\chromedriver')
driver.maximize_window()
driver.get('https://douban.com')


time.sleep(30)

cookies = driver.get_cookies()
with open('D:/test_cookies/db_cookie_1','wb') as f:  # db_cookie_1 为文件，不是文件夹，只需要建立一个test_cookies文件即可。
    pickle.dump(cookies,f)
print ('done')

# 上面示例演示通过selenium打开豆瓣网，你要在豆瓣网上输入账号密码点击登录，程序会把登录成功后的豆瓣网cookie保存到指定文件夹下面。
# 保存cookies到文件是用pickle库的dump方法来完成的，它可以帮助你序列化数据，很方便。
# 上面睡眠60秒是给你足够时间输入账号密码。