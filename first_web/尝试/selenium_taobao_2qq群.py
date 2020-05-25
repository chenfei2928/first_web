from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

web = webdriver.Chrome(executable_path='D:\develop_study\chromedriver\chromedriver')
web.get('https://detail.tmall.com/item.htm?id=527774229372&ali_refid=a3_430582_1006:1122325035:N:fICcc//H0AV066KNAOKXET485ECzYa4s:26922aba232a73adddef23ab7aee0d0d&ali_trackid=1_26922aba232a73adddef23ab7aee0d0d&spm=a230r.1.14.11&skuId=3141090064232')

#web.switch_to.frame('sufei-dialog-content')
print('请手动关闭登陆对话框')

time.sleep(5)

web.switch_to.default_content()

web.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[4]/div/div/div[2]/div[2]/a').click() # 加入购物车

