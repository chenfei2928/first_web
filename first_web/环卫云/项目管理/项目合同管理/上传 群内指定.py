import selenium.webdriver as drivers
import time



driver = drivers.Chrome()
driver.implicitly_wait(20)
driver.get("http://www.baidu.com/")
driver.find_element_by_class_name('soutu-btn').click()
time.sleep(1)
driver.find_element_by_class_name('upload-pic').send_keys(r'C:\Users\Administrator\Desktop\临时\2223.jpeg')