# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:34:28 2019

@author: Administrator

数据分析师工作流—从采集、分析到出图

"""
#1、导入模块

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pda 

# 2、网址生成器
def get_urls(n):
    # 需要生成的页数
    urls=[]
    for i in range(1,n+1):
        url = 'https://travel.qunar.com/p-cs300195-hangzhou-meishi?page=%s'%i
        urls.append(url)
    return urls

#3、采集数据
def get_informations(u):   
    # 从分页采集数据
    # U输入的网址
    r = requests.get(u)  #访问
    soup = BeautifulSoup(r.text,'lxml')  # 解析
    ims = soup.find('ul',class_="list_item clrfix").find_all('li')
        # 获取列表内容
    data = []
    for i in ims:
        dic={}
        dic['lat'] = i['data-lat']   # 经度
        dic['lng'] = i['data-lng']   # 维度  待验证
        dic['餐厅名称'] = i.find('span',class_="cn_tit").text
        dic['星级'] = i.find('span',class_="cur_star")['style'].split(':')[1]
        data.append(dic)   
    return data

# 4、嵌套总函数
def get_alldata(n):
    # 从每页采集所有数据，n为需要采集的页数；
    alldata =[]
    for u in get_urls(n):
        alldata.extend(get_informations(u))
    return pd.DataFrame(alldata)


# 读取2页测试
get_alldata(2)
        
#5、全部读取，并装载到csv文件；
df = get_alldata(200)
df.to_csv('餐厅数据1.csv',index=False)


#6、 数据读取清晰
df = pd.read_csv('餐厅数据.csv')
df

df.loc[:,'lat'] = df['lat'].astype('float')
df.loc[:,'lng'] = df['lng'].astype('float')
df.loc[:,'星级'] = df['星级'].str.replace('%','').astype('float')
df

#df.loc[:,'星级'] = df.loc[:,'星级'] / 20

#df

# 7 字段筛选

df['星级'].hist()
        # 直方图


# 筛选星级大于0 的数据；

df_star=df.loc[df['星级']>0]
df_star

df_star['星级'].hist()

df_star.to_csv('餐厅前200星级数据.csv',index=False,encoding='utf-8-sig')


# 生成三维地图

#    1、打开星级数据.csv文件；
#    2、另存为excel
#        选中数据
#        ctrl+d创建图表
#        插入—选中三维地图
#            经度、维度选中，值选星级
#            图样选中热力图
#            即可。预览
#            