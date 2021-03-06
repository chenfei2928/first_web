# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:13:11 2019

@author: Administrator

本代码由热心网友提供：微信名称 优秀的人；

"""

#coding=utf-8

import requests, random, bs4, openpyxl

wb = openpyxl.Workbook()
# 创建工作薄
sheet = wb.active
# 获取工作薄的活动表
sheet.title = 'movies'
# 工作表重命名
sheet['A1'] = '序号'  # 加表头，给A1单元格赋值
sheet['B1'] = '电影名'  # 加表头，给B1单元格赋值
sheet['C1'] = '评分'  # 加表头，给C1单元格赋值
sheet['D1'] = '推荐语'  # 加表头，给D1单元格赋值
sheet['E1'] = '链接'  # 加表头，给E1单元格赋值

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x * 25) + '&filter='
    res = requests.get(url)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em', class_="").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span', class_="rating_num").text
        url_movie = titles.find('a')['href']

        if titles.find('span', class_="inq") != None:
            tes = titles.find('span', class_="inq").text
            sheet.append([num, title, comment, tes, url_movie])
            # 把num, title, comment, tes和url_movie写成列表，用append函数多行写入Excel
            print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes + '\n' + url_movie)
        else:
            sheet.append([num, title, comment, None, url_movie])
            print(num + '.' + title + '——' + comment + '\n' + '\n' + url_movie)

wb.save('movieTop250.xlsx')