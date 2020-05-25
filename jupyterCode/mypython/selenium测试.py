# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:08:49 2019

@author: Administrator

vip音乐获取
"""

from selenium import webdriver
import requests
import json
import re



driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\Chrome\\Application\\chromedriver.exe')

url ='https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E4%BC%A4%E5%BF%83%E5%A4%AA%E5%B9%B3%E6%B4%8B'


def get_url():
    driver.get(url)
    driver.implicitly_wait(5)  #智能等待
    data = driver.find_element_by_xpath('//*[@id="song_box"]/div[2]/ul[2]/li[1]/div/div[2]/span[1]/a').get_attribute('href')
    print(data)
    dic = {'mid':data}
    return dic

def get_music_url(data):
    url = 'http://www.douqq.com/qqmusic/qqapi.php'
    req = requests.post(url,data = data).text
    req = json.loads(req)
    req = req.replace('\/\/','//').replace('\/','/')
   # print(req)
    rg = re.compile('"mp3_l":(.*?)",')
    rs = re.findall(rg,req)[0]
    return rs

def get_music(rs):
    
    
    
def go():
    data = get_url()
    get_music(data)

go()


# 本程序参考b站学习，后面没有了
