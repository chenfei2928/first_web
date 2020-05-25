import os
from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups':0,  # 设为0，表示禁止下载窗口
         'download.default_directory':os.getcwd()}
            # 设置文件下载路径，使用os.getcwd()方法获取当前脚本的目录作为下载文件的保存位置


options.add_experimental_option('prefs',prefs)

driver = webdriver.Chrome(options=options)

driver.get('https://pypi.org/project/selenium/#files')
driver.find_element_by_xpath('//*[@id="files"]/table/tbody/tr[2]/th/a').click()

