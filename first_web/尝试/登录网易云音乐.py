from selenium import webdriver
browser = webdriver.Chrome(r'D:\develop_study\chromedriver\chromedriver')
browser.implicitly_wait(5)


browser.get('https://www.zhihu.com/signin?')


browser.find_element_by_css_selector('.SignFlow-account input[name="username"]').send_keys('18600890135')
browser.find_element_by_css_selector('.SignFlow-password input[name="password"]').send_keys('cf908cf')

# #获取全屏图片，并截取验证码图片的位置
# driver.get_screenshot_as_file('a.png')
# location = driver.find_element_by_id('imgValidateCode').location
# size = driver.find_element_by_id('imgValidateCode').size
# left = location['x']
# top = location['y']
# right = location['x'] + size['width']
# bottom = location['y'] + size['height']
# a = Image.open("a.png")
# im = a.crop((left,top,right,bottom))
# im.save('a.png')
# time.sleep(1)
# #打开保存的验证码图片
# image = Image.open("a.png")
# #图片转换成字符
# vcode = pytesseract.image_to_string(image)
# print(vcode)
#


browser.find_element_by_css_selector('.Login-options > .Button').click()


