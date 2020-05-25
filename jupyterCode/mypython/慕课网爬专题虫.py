# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:30:49 2019

@author: Administrator

慕课网爬虫专题学习

"""

#爬取网页的通用框架代码
import requests

def gethtmltext(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.enconding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    
    url="http://www.baidu.com"
    print(gethtmltext(url))
    
    
help(input)

    