"""
* send_keys() 指定文件上传路径。
"""
from selenium import webdriver
import os

file_path = os.path.abspath('./files//')

driver = webdriver.Chrome()
# upload_page = 'file:///' + file_path + 'upfile.html'

# upload_page ='file:///D:/code_file/first_web/book-code-master/webdriver_api/files/upfile.html'

driver.get('file:///D:/code_file/first_web/book-code-master/webdriver_api/files/upfile.html')
print(file_path)
# 定位上传按钮，添加本地文件
driver.find_element_by_id("file").send_keys(file_path + '//test.txt')
# ……

os.path