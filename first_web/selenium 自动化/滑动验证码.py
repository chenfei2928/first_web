from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import cv2
import time
import requests

web = Chrome()

web.get('https://dun.163.com/trial/sense')
web.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/ul/li[2]').click()  #点击可疑用户-滑动拼图
time.sleep(1)
web.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[1]/span').click() #点击完成验证
time.sleep(1)
bg_img_src = web.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]'
                          '/div/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/img[1]').get_attribute('src')
                        # 背景图

front_img_src = web.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]'
                          '/div/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/img[2]').get_attribute('src')

                        # 滑块

with open("bg.jpg",mode='wb') as f:
    f.write(requests.get(bg_img_src).content)

with open("front.jpg",mode='wb') as f:
    f.write(requests.get(front_img_src).content)


import numpy as np

bg = cv2.imread('bg.jpg')
front = cv2.imread("front.jpg")


# 灰度处理
bg = cv2.cvtColor(bg,cv2.COLOR_BGR2GRAY)
front = cv2.cvtColor(front,cv2.COLOR_BGR2GRAY)


# 处理滑块
front = front[front.any(1)]

#匹配  图像匹配算法
result = cv2.matchTemplate(bg,front,cv2.TM_CCOEFF_NORMED) # 精度最高，速度最慢

# np.argmax(result)  # 返回一维位置

x,y = np.unravel_index(np.argmax(result),result.shape)
div = web.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/'
                                'div[1]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[2]')

ActionChains(web).drag_and_drop_by_offset(div,xoffset=y,yoffset=0).perform()


# print(x,y)
# w,h = front.shape
# cv2.rectangle(bg,(y,x),(y+w,x+h),(38,38,38),2)
#
# cv2.imshow("gray1",bg)
# cv2.imshow("gray2",front)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


