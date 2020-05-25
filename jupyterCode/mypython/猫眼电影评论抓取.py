# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:33:51 2019

@author: Administrator

猫眼电影评论抓取
"""
import requests
import json
import pandas as pd

#import io
#import sys
#import csv

        # 两个内置模块

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')  # 执行报错

headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36'
        }


#    
#def spare_json(text):    #字典格式存储
#    data= {}
#    content = json.loads(text)
#    comments = content['data'].get('comments')
#    for i in comments:
#        data['gender'] = i.get('gender')   # 0,未知性别，1男，2女；
#        data['score'] = i.get('scores')    #评分
#        data['content'] = i.get('content')  # 评论内容
#        data['upCount'] = i.get('upCount')  # 评论点赞数
#        data['userLevel'] = i.get('userLevel') # 用户等级
##        print(data)
#    return data
#
#def get_json_data(ur):  # 获取json格式数据
#    url = ur    
#    response = requests.get(url,headers = headers)    
#    print(response.content)
#    spare_json(response.content)

def get_urls(x):   #获取url列表
    urls=[]
    for i in range(0,x,15):    
        url =('http://m.maoyan.com/review/v2/comments.json?movieId=1211270&userId=-1&offset=%i&limit=15&ts=1566365411311&type=3'%i)
        urls.append(url)
#    print(urls)
    return urls

def get_data():   # 获取数据
    datas={}
    for ur in urls:
        url = ur    
        response = requests.get(url,headers = headers)    
        data= {}
        content = json.loads(response.content)
        comments = content['data'].get('comments')
        
        for q in comments:
            data['gender'] = q.get('gender')   # 0,未知性别，1男，2女；
            data['score'] = q.get('scores')    #评分
            data['content'] = q.get('content')  # 评论内容
            data['upCount'] = q.get('upCount')  # 评论点赞数
            data['userLevel'] = q.get('userLevel') # 用户等级
    #        print(data)
        datas.append(data)
    print(datas)
        

if __name__ =='__main__':
    get_urls(30)
    get_data()


#2、数据的分析
#3、影评分析
#://m.maoyan.com/review/v2/comments.json?movieId=1211270&userId=-1&offset=30&limit=15&ts=1566365411311&type=3
#://m.maoyan.com/review/v2/comments.json?movieId=1211270&userId=-1&offset=45&limit=15&ts=1566365411311&type=3