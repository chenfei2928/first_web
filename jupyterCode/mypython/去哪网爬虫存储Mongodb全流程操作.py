# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:58:54 2019

@author: 陈飞
"""

import requests
from bs4 import BeautifulSoup

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db2 = myclient['直播0812']
table = db2['去哪儿网丽江']  # 创建数据库/集合
table.delete_many({})   # 清空数据库


u ='http://travel.qunar.com/p-cs300079-lijiang-jingdian'
r = requests.get(url=u)     #页面访问

soup =BeautifulSoup(r.text,'lxml') #解析网页

ul = soup.find('ul',class_="list_item clrfix")
lis =ul.find_all('li')


for li in lis:    
    dic = {}
    dic['景点名称']=li.find('span',class_="cn_tit").text
    dic['评论数']= li.find('div',class_="comment_sum").text
    table.insert_one(dic)  # 数据入库操作
    print('成功采集数据！')
    print(dic)
    # 寻找标签并存储


‘’‘
数据分析
’‘’
import pandas as pd
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db2 = myclient['直播0812']
table = db2['去哪儿网丽江'] 

df = pd.DataFrame(list(table.find()))
df['评论数']=df['评论数'].astype('int')
df


import matplotlib.style as psl
psl.uer('ggplot')

df['评论数'].plot.box()