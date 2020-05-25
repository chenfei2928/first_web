# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:38:13 2019

@author: Administrator

目标：豆瓣电影 top250信息获取
"""

import requests
from bs4 import BeautifulSoup


urllist=[]
for i in range(0,226,25):
    list=('https://movie.douban.com/top250?start=%i&filter=' %i)
    urllist.append(list)
print(urllist)
    # 每页25个，10页提取成功

url = 'https://movie.douban.com/top250?start=0&filter='
r = requests.get(url)     #页面访问
soup =BeautifulSoup(r.text,'lxml') #解析网页

div = soup.find('div',class_="article")
        #  获取25个明细项目的整体大框。
        
us = div.find_all('span',class_="title")

uus = us.find_all(re.compile("t"))

uus

us       #   获取电影名称

import re
for n in us:

    print(n)
    if ’[re\s*]‘ not in n:
        dic={}
        dic['电影名称'] = n.text
        
    print(dic)
    
    //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]
    //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[2]
      .a.span()  
    
names = re.findall('<a href="/films/.*?" title="(.*?)" class="image-link"',res.text)
   


