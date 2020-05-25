# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:30:17 2019

@author: Administrator
"""
import pymongo

#连接mongodb

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#tdb = myclient.alpha87

#post = tdb.test

#post.insert({'name':"李白", "age":"30", "skill":"Python"})



db2 = myclient['直播0812']
table2 = db2['test']


table2.delete_many({}) # 数据库清空



dic = {'a':10,'b':20}

table2.insert_one(dic)
    # 插入一条文档
    # 执行多次，会插入多条重复数据
    
