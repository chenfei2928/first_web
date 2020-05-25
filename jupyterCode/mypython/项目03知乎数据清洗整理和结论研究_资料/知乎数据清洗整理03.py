# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:21:28 2019

@author: Administrator
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#数据读取
data1 = pd.read_csv('C:\\Users\\Administrator\\mypython\\项目03知乎数据清洗整理和结论研究_资料\\知乎数据_201701.csv',engine ='python')

data2 = pd.read_csv('C:\\Users\\Administrator\\mypython\\项目03知乎数据清洗整理和结论研究_资料\\六普常住人口数.csv',engine='python')


#数据清洗
    
def cleandata(df):
    '''
    cleandata:数据清洗函数，将空值替换
    df参数：pandas的二维数组
    返回清洗后的二维数组
    '''
    cols = df.columns
    for col in cols:
        if df[col].dtype == object:
            df[col].fillna('缺失数据',inplace = True)
                #字符串列的话，缺失值填写"缺失数据"
        else:
            df[col].fillna(0,inplace = True)
                #数字列的话，缺失值就填充0
    return df

data1_c=cleandata(data1)

data1_c.head(10)

# 数据处理

df_city = data1_c.groupby('居住地').count()  # 按照居住地统计知友数量
data2['city'] = data2['地区'].str[:-1]   # 城市信息清洗，去掉城市等级文字
#print(df_city.head())  
#print(data2.head())  

                       
q1data = pd.merge(df_city, data2, 
                  left_index = True, 
                  right_on = 'city', 
                  how = 'inner')[['_id','city','常住人口']]
q1data['知友密度'] = q1data['_id']/q1data['常住人口'] 
#print(q1data.head())
# 统计计算知友数量，知友密度

def data_nor(df, *cols):
    colnames = []
    for col in cols:
        colname = col + '_nor'
        df[colname] = (df[col]-df[col].min())/(df[col].max()-df[col].min()) * 100
        colnames.append(colname)
    return(df,colnames)
# 创建函数，结果返回标准化取值，新列列名

resultdata = data_nor(q1data,'_id','知友密度')[0]
resultcolnames = data_nor(q1data,'_id','知友密度')[1]
q1data_top20_sl = resultdata.sort_values(resultcolnames[0], 
                                         ascending=False)[['city',resultcolnames[0]]].iloc[:20]
q1data_top20_md = resultdata.sort_values(resultcolnames[1], 
                                         ascending=False)[['city',resultcolnames[1]]].iloc[:20]
#print(q1data_top20_sl)
# 标准化取值后得到知友数量，知友密度的TOP20数据

plt.rcParams['font.sans-serif'] = ['SimHei']  
    # Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['axes.unicode_minus'] = False    
    # 解决Matplotlib坐标轴负号'-'显示为方块的问题
    
fig1 = plt.figure(num=1,figsize=(12,4))
y1 = q1data_top20_sl[resultcolnames[0]]
plt.bar(range(20),
        y1,
        width = 0.8,
        facecolor = 'yellowgreen',
        edgecolor = 'k',
        tick_label = q1data_top20_sl['city'])
plt.title('知友数量TOP20\n')
plt.grid(True, linestyle = "--",color = "gray", linewidth = "0.5", axis = 'y')  
for i,j in zip(range(20),y1):
    plt.text(i+0.1,2,'%.1f' % j, color = 'k',fontsize = 9)

fig2 = plt.figure(num=2,figsize=(12,4))
y2 = q1data_top20_sl[resultcolnames[0]]
plt.bar(range(20),
        y2,
        width = 0.8,
        facecolor = 'lightskyblue',
        edgecolor = 'k',
        tick_label = q1data_top20_md['city'])
plt.grid(True, linestyle = "--",color = "gray", linewidth = "0.5", axis = 'y')  
plt.title('知友密度TOP20\n')
for i,j in zip(range(20),y2):
    plt.text(i+0.1,2,'%.1f' % j, color = 'k',fontsize = 9)
# 创建图表
    
# 问题2 不同高校知友关注和被关注情况
# 要求：
# ① 按照学校（教育经历字段） 统计粉丝数（‘关注者’）、关注人数（‘关注’），并筛选出粉丝数TOP20的学校，不要求创建函数
# ② 通过散点图 → 横坐标为关注人数，纵坐标为粉丝数，做图表可视化
# ③ 散点图中，标记出平均关注人数（x参考线），平均粉丝数（y参考线）
# 提示：
# ① 可自行设置图表风格

q2data = data1_c.groupby('教育经历').sum()[['关注','关注者']].drop(['缺失数据','大学','本科'])
q2data_c = q2data.sort_values('关注',ascending=False)[:20]
#print(q2data_c)
# 统计计算学校的粉丝数、被关注量

plt.figure(figsize=(10,6))
x = q2data_c['关注']
y = q2data_c['关注者']
follow_mean = q2data_c['关注'].mean()
fans_mean = q2data_c['关注者'].mean()
plt.scatter(x,y,marker='.',
           s = y/1000,
           cmap = 'Blues',
           c = y,
           alpha = 0.8,
           label = '学校')
# 创建散点图
# 此处以下有问题；

plt.axvline(follow_mean,
            hold=None,
            label="平均关注人数：%i人" %follow_mean,
            color='r',
            linestyle="--",
            alpha=0.8)  # 添加x轴参考线

plt.axhline(fans_mean,
            hold=None,
            label="平均粉丝数：%i人" % fans_mean,
            color='g',linestyle="--",
            alpha=0.8)   # 添加y轴参考线
plt.legend(loc = 'upper left')
plt.grid()
# 添加显示内容

for i,j,n in zip(x,y,q2data_c.index):
    plt.text(i+500,j,n, color = 'k')
# 添加注释