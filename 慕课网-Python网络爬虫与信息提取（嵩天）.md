

# 慕课网-Python网络爬虫与信息提取（嵩天）

## 第一周：网络爬虫之规则

### 单元1：requests库入门

```
>>> import requests
>>> r = requests.get('http://www.baidu.com')
>>> r.status_code
200
>>> r.encoding ='uft-8'
>>> r
<Response [200]>
>>> r.text
```

#### Requests库的7个主要方法

| 方法               | 说明                                   |
| ------------------ | -------------------------------------- |
| requests.request() | 构造一个请求，支撑以下各方法的基础方法 |
| requests.get()     | 获取HTML网页的主要方法                 |
| requests.head()    | 获取HTML网页头信息的方法               |
| requests.post()    | 向HTML网页提交POST请求的方法           |
| requests.put()     | 向HTML网页提交PUT请求的方法            |
| requests.patch()   | 向HTML网易提交局部修改请求             |
| requests.delete    | 向HTML网易提交删除请求                 |

#### requests.get方法

![1586747228303](file:///C:/%5CUsers%5CAdministrator%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5C1586747228303.png)

##### Response对象的属性

| 属性                | 说明                                               |
| ------------------- | -------------------------------------------------- |
| r.status_code       | 请求返回状态，200 连接成功；404 连接失败           |
| r.text              | 响应内容的字符串形式，即URL对应的页面内容          |
| r.encoding          | 从header中猜测的响应内容编码方式                   |
| r.apparent_encoding | 从内容中分析出中的响应内容编码方式（备选编码方式） |
| r.content           | 响应内容的二进制样式                               |

##### 示例

```
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> import requests
>>> r = requests.get('http://www.baidu.com')
>>> r.status_code
200
>>> r.text

'<!DOCTYPE html>\r\n<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css><title>ç\x99¾åº¦ä¸\x80ä¸\x8bï¼\x8cä½\xa0å°±ç\x9f¥é\x81\x93</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=ç\x99¾åº¦ä¸\x80ä¸\x8b class="bg s_btn"></span> </form> </div> </div> <div id=u1> <a href=http://news.baidu.com name=tj_trnews class=mnav>æ\x96°é\x97»</a> <a href=http://www.hao123.com name=tj_trhao123 class=mnav>hao123</a> <a href=http://map.baidu.com name=tj_trmap class=mnav>å\x9c°å\x9b¾</a> <a href=http://v.baidu.com name=tj_trvideo class=mnav>è§\x86é¢\x91</a> <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>è´´å\x90§</a> <noscript> <a href=http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 name=tj_login class=lb>ç\x99»å½\x95</a> </noscript> <script>document.write(\'<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u=\'+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ \'" name="tj_login" class="lb">ç\x99»å½\x95</a>\');</script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">æ\x9b´å¤\x9aäº§å\x93\x81</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a href=http://home.baidu.com>å\x85³äº\x8eç\x99¾åº¦</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>ä½¿ç\x94¨ç\x99¾åº¦å\x89\x8då¿\x85è¯»</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>æ\x84\x8fè§\x81å\x8f\x8dé¦\x88</a>&nbsp;äº¬ICPè¯\x81030173å\x8f·&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>\r\n'
>>> 

>>> r.encoding
'ISO-8859-1'
>>> r.apparent_encoding
'utf-8'
>>> r.encoding = 'utf-8'
>>> r.text

'<!DOCTYPE html>\r\n<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css><title>百度一下，你就知道</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=百度一下 class="bg s_btn"></span> </form> </div> </div> <div id=u1> <a href=http://news.baidu.com name=tj_trnews class=mnav>新闻</a> <a href=http://www.hao123.com name=tj_trhao123 class=mnav>hao123</a> <a href=http://map.baidu.com name=tj_trmap class=mnav>地图</a> <a href=http://v.baidu.com name=tj_trvideo class=mnav>视频</a> <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>贴吧</a> <noscript> <a href=http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 name=tj_login class=lb>登录</a> </noscript> <script>document.write(\'<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u=\'+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ \'" name="tj_login" class="lb">登录</a>\');</script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">更多产品</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a href=http://home.baidu.com>关于百度</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>使用百度前必读</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>意见反馈</a>&nbsp;京ICP证030173号&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>\r\n'
>>> 
```

#### 爬取网页的通用代码框架

##### Requests库的异常

| 异常                      | 说明                                    |
| ------------------------- | --------------------------------------- |
| requests.ConnectionError  | 网络连接错误，如DNS查询失败、拒绝连接等 |
| requests.HTTPError        | HTTP错误异常                            |
| requests.URLRequired      | URL缺失异常                             |
| requests.TooManyRedirects | 超过最大重定向次数，产生重定向异常      |
| requests.ConnectTimeout   | 连接远程服务器超时异常                  |
| requests.Timeout          | 请求URL超时，产生超时异常               |

##### 通用代码

```
import requests

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status() #如果返回不是200，返回异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
            return "产生异常"

if __name__ == "__main__":
    url = 'http://www.baidu.com'
    print(getHTMLText(url))
```

#### HTTP协议及requests库主要方法

HTTP 超文本传输协议

##### head方法

```
>>> import requests
>>> r = requests.head('http://httpbin.org/get')
>>> r.headers
{'Date': 'Mon, 13 Apr 2020 05:30:55 GMT', 'Content-Type': 'application/json', 'Content-Length': '305', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
>>> r.text
''
```

##### psot方法

```
>>> payload = {'key1':'value1','key2':'value2'}
>>> r = requests.post('http://httpbin.org/post',data=payload)
>>> print.(r.text)
SyntaxError: invalid syntax
>>> print(r.text)
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "23", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.23.0", 
    "X-Amzn-Trace-Id": "Root=1-5e93fa0c-ca170ac8131ca8be595a1a54"
  }, 
  "json": null, 
  "origin": "61.50.105.30", 
   "url": "http://httpbin.org/post"
}
r = requests.post('http://httpbin.org/post',data = 'ABC')
>>> print(r.text)
{
  "args": {}, 
  "data": "ABC", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "3", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.23.0", 
    "X-Amzn-Trace-Id": "Root=1-5e93fab9-139eb74dbc89fb6237f88e2f"
  }, 
  "json": null, 
  "origin": "61.50.105.30", 
  "url": "http://httpbin.org/post"
}
```

#### Requests库主要解析方法

params 修改URL

```
import requests

kv = {'key1':'value1','key2':'value2'}

r = requests.request('get','http://python123.io/ws',params=kv)
print(r.url)
```

data

json

headers

cookies

auth

files

timeout

proxies

allow_redirects

stream

verify

cert

#### 单元小结

requests.get()

requests.head()

重点掌握

爬取网页的通用代码框架 掌握

### 单元2：网络爬虫的 “盗亦有道”

#### 网络爬虫引发的问题

Requests 小规模数据爬取

Scrapy 中规模数据爬取。

服务器

性能骚扰

法律风险

隐私泄露

来源审查 ：判断User-Agent 进行限制

发布公告：Rebots协议

网络爬虫排除标准

在网站根目录下 rebots.txt

无此文件，允许所有爬取。

#### Rebots协议

##### 京东robots协议

https://www.jd.com/robots.txt

```
User-agent: * 
Disallow: /?* 
Disallow: /pop/*.html 
Disallow: /pinpai/*.html?* 
User-agent: EtaoSpider 
Disallow: / 
User-agent: HuihuiSpider 
Disallow: / 
User-agent: GwdangSpider 
Disallow: / 
User-agent: WochachaSpider 
Disallow: /
```

##### 百度robots协议

```
User-agent: Baiduspider
Disallow: /baidu
Disallow: /s?
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Googlebot
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: MSNBot
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Baiduspider-image
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: YoudaoBot
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Sogou web spider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Sogou inst spider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Sogou spider2
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Sogou blog
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Sogou News Spider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Sogou Orion spider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: ChinasoSpider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: Sosospider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh


User-agent: yisouspider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: EasouSpider
Disallow: /baidu
Disallow: /s?
Disallow: /shifen/
Disallow: /homepage/
Disallow: /cpro
Disallow: /ulink?
Disallow: /link?
Disallow: /home/news/data/
Disallow: /bh

User-agent: *
Disallow: /
```

#### Robots协议的遵守方式

约束性：网络爬虫可以不遵守，但存在法律风险。

类人类行为，可以不参考rebots协议。

#### 单元小结

### 单元3：Requests库网络爬虫实战（5个案例）

#### 实例1：京东商品页面的爬取

```
import requests

url = 'https://item.jd.com/100005787046.html'

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('爬取失败')
```

代码结果与课程不一致，运行结果链接 需要登录京东。

```
"<script>window.location.href='https://passport.jd.com/uc/login?ReturnUrl=http://item.jd.com/100005787046.html'</script>"
```

#### 实例2：亚马逊商品页面的爬取

```
import requests

url = 'https://www.amazon.cn/dp/B0785D5L1H/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=%E6%9E%81%E7%AE%80&qid=1586760393&sr=8-1'

try:
    kv = {'user-agent':'Mozilla/5.0'}  # 伪装浏览器
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('爬取失败')
```

#### 实例3：百度/360搜索关键词提交

```
>>> kv = {'wd':'python'}
>>> r = requests.get('http://www.baidu.com/s',params = kv)
>>> r.status_code
200
>>> r.request.url
'https://wappass.baidu.com/static/captcha/tuxing.html?&ak=c27bbc89afca0463650ac9bde68ebe06&backurl=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3Dpython&logid=7947542543176541686&signature=3fed0b3a823c62d34101863c3639b327&timestamp=1586761583'
>>> len(r.text)
1519
import requests
keyword = 'Python'

try:
    kv = {'wd':keyword}
    r = requests.get("http://www.baidu.com/s",params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')
import requests
keyword = 'Python'

try:
    kv = {'q':keyword}
    r = requests.get("http://www.so.com/s",params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')
```

#### 实例4：网络图片的爬取和存储

```
>>> path = "D:/abc.jpg"
>>> url = "http://image.ngchina.com.cn/2015/0323/20150323111422966.jpg"
>>> r = requests.get(url)
>>> r.status_code
200
>>> with open(path,'wb') as f:
	f.write(r.content)

	
625427
>>> f.close()
import requests
import os

url ='http://image.ngchina.com.cn/2015/0323/20150323111422966.jpg'
root = 'D://pic//'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')
```

#### 实例5：IP地址归属地的自动查询

```
import requests
url ='https://m.ip138.com/iplookup.asp?ip='

try:
    r = requests.get(url+'202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print('爬取失败')
    
```

执行结果 爬取失败

r = requests.get(url+'202.204.80.112') 执行报错

```
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> url ='https://m.ip138.com/iplookup.asp?ip='
>>> r = requests.get(url+ '202.204.80.112')
Traceback (most recent call last):
  File "D:\develop_study\python\Python38-32\lib\site-packages\urllib3\connection.py", line 156, in _new_conn
    conn = connection.create_connection(
  File "D:\develop_study\python\Python38-32\lib\site-packages\urllib3\util\connection.py", line 84, in create_connection
    raise err
  File "D:\develop_study\python\Python38-32\lib\site-packages\urllib3\util\connection.py", line 74, in create_connection
    sock.connect(sa)
TimeoutError: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\develop_study\python\Python38-32\lib\site-packages\urllib3\connectionpool.py", line 665, in urlopen
    httplib_response = self._make_request(
  File "D:\develop_study\python\Python38-32\lib\site-packages\urllib3\connectionpool.py", line 387, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "D:\develop_study\python\Python38-32\lib\http\client.py", line 1230, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "D:\develop_study\python\Python38-32\lib\http\client.py", line 1276, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "D:\develop_study\python\Python38-32\lib\http\client.py", line 1225, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "D:\develop_study\python\Python38-32\lib\http\client.py", line 1004, in _send_output
    self.send(msg)
  File "D:\develop_study\python\Python38-32\lib\http\client.py", line 944, in send
    self.connect()
  File "D:\develop_study\python\Python38-32\lib\site-packages\urllib3\connection.py", line 184, in connect
    conn = self._new_conn()
  File "D:\develop_study\python\Python38-32\lib\site-packages\urllib3\connection.py", line 168, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x03E697C0>: Failed to establish a new connection: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。
```

#### 单元小结

requests的强大功能



## 第二周 网络爬虫之规则



### 本周课程导学

​	内容介绍



### 单元4:  Beautiful Soup库入门



#### 安装

```
>pip install beautifulsoup4
```



```
import requests
from bs4 import BeautifulSoup

r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo,"html.parser")
print(soup)
print(soup.prettify())  # 美化输出


```



#### 基本元素



Beautiful Soup 库是解析、遍历、维护“标签树”的功能库



| 基本元素        | 说明                              |
| --------------- | --------------------------------- |
| Tag             | 最基本的信息组织单元              |
| Name            | 名字    <tag>.name                |
| Attribute       | 属性   <tag>.attrs                |
| NavigableString | 标签内非属性字符串   <tag>.string |
| Comment         | 标签内字符串的注释部分            |



```
import requests
from bs4 import BeautifulSoup

r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo,"html.parser")
#print(soup)
print(soup.title)
print(soup.a.name)
print(soup.a.parent.name)
print(soup.a.parent.parent.name)

print('--fengexian-----------------')


tag  = soup.a
print(tag)
print(tag.attrs)
print(tag.attrs['class'])
print(tag.attrs['href'])
print(type(tag.attrs))
print(type(tag))
print('--fengexian-------string----------')

print(soup.a.string)
print(soup.p.string)

print('--fengexian----------注释-------')



```

```
D:\develop_study\python\Python38-32\python.exe D:/code_file/first_web/爬虫/慕课/慕课01.py
<title>This is a python demo page</title>
a
p
body
--fengexian-----------------
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
{'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
['py1']
http://www.icourse163.org/course/BIT-268001
<class 'dict'>
<class 'bs4.element.Tag'>
--fengexian-------string----------
Basic Python
The demo python introduces several python courses.
--fengexian----------注释-------

Process finished with exit code 0

```



#### 基于bs4库的HTML内容遍历方法

##### 下行遍历

| 属性         | 说明                                                    |
| ------------ | ------------------------------------------------------- |
| .contents    | 子节点的列表，将<tag>所有儿子节点存入列表               |
| .children    | 子节点的迭代类型，与.contents类似，用于循环遍历儿子节点 |
| .descendants | 子孙节点的迭代类型，包含所有子孙节点，用于循环遍历      |



```
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> import requests
>>> from bs4 import BeautifulSoup
>>> r = requests.get('https://python123.io/ws/demo.html')
>>> demo = r.text
>>> soup = BeautifulSoup(demo,"html.parser")
>>> soup.head
<head><title>This is a python demo page</title></head>

>>> soup.head.contents
[<title>This is a python demo page</title>]
>>> soup.body.contents
['\n', <p class="title"><b>The demo python introduces several python courses.</b></p>, '\n', <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:

<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>, '\n']
>>> len(soup.body.contents)
5
>>> soup.body.contents[1]
<p class="title"><b>The demo python introduces several python courses.</b></p>
>>> for child in soup.body.children:
	print(child)

	


<p class="title"><b>The demo python introduces several python courses.</b></p>


<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:

<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>


>>> 
```



##### 上行遍历



| 属性     | 说明                                         |
| -------- | -------------------------------------------- |
| .parent  | 节点的父亲标签                               |
| .parents | 节点先辈标签的迭代类型，用于循环遍历先辈节点 |



```
import requests
from bs4 import BeautifulSoup

r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo,"html.parser")

for parent in soup.a.parents:
	if parent is None:
		print(parent)
	else:
		print(parent.name)
```



```
p
body
html
[document]

```





##### 平行遍历



| 属性               | 说明                                                 |
| ------------------ | ---------------------------------------------------- |
| .next_sibling      | 返回按照HTML文本顺序的下一个平行节点标签             |
| .previous_sibling  | 返回按照HTML文本顺序的上一个平行节点标签             |
| .next_siblings     | 迭代类型，返回按照HTML文本顺序的后续所有平行节点标签 |
| .previous_siblings | 迭代类型，返回按照HTML文本顺序的前续所有平行节点标签 |



```
import requests
from bs4 import BeautifulSoup

r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo,"html.parser")

print(soup.a.next_sibling)
print(soup.a.next_sibling.next_sibling)

print(soup.a.previous_sibling)
print(soup.a.previous_sibling.previous_sibling)


for sibling in soup.a.next_siblings:
    print(sibling)

for sibling in soup.a.previous_siblings:
    print(sibling)

```



#### 基于bs4库的HTML格式输出

.prettify

```python
import requests
from bs4 import BeautifulSoup

r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo,"html.parser")

print(soup.prettify) 
print("-----------------------------------------------")
print(soup.a.prettify)

```



#### 单元小结



### 单元5:信息组织与提取方法



#### 信息标记的三种形式



​	HTML  超文本标记语言



**XML  扩展标记语言	  extensible Markup Language**

​		  基于HTMl发展而来；



**JSON	JavaScript Object Notation**

​			有类型的键值对。key：value

​			键、值 都需要双引号。

​		移动应用云端和节点的信息通信，无注释。



**YAML	YAML  Ain‘t Markup  Language**   

​			无类型的键值对 key：value



#### 三种信息标记形式的比较



XML ：		  Internet上的信息交互与传递

JSON：		移动应用云端和节点的信息通信，无注释。

YAML：	   各类系统的配置文件，有注释易读。



#### 信息提取的一般方法



方法一：完整解析信息的标记形式，再提取关键信息。

方法二：无视标记形式，直接搜索关键信息。

```python
import requests
from bs4 import BeautifulSoup

r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

soup = BeautifulSoup(demo,"html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))

```



```python
D:\develop_study\python\Python38-32\python.exe D:/code_file/first_web/爬虫/慕课/慕课01.py
http://www.icourse163.org/course/BIT-268001
http://www.icourse163.org/course/BIT-1001870001

Process finished with exit code 0

```



#### 基于bs4库的HTML内容查找方法



##### <>.find_all (name,attrs,recursive,string,**kwargs)

##### name:对标签名称的检索字符串。



```python
import requests
r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(demo,"html.parser")

print(soup.find_all('a'))

print(soup.find_all(['a','b']))   # 同时查询a和b标签。



```





```python
for tag in soup.find_all(True):
    print(tag.name)

```





```python
import re

for tag in soup.find_all(re.compile('b')):  # b  开头的标签
    print(tag.name)

---------------------------------


D:\develop_study\python\Python38-32\python.exe D:/code_file/first_web/爬虫/慕课/慕课01.py
body
b

Process finished with exit code 0

```



##### attrs:对标签属性值的检索字符串，可标注属性检索



```python
import requests
r = requests.get('https://python123.io/ws/demo.html')
demo = r.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(demo,"html.parser")

print(soup.find_all('p','course'))


--------------------------------------------------------------------
D:\develop_study\python\Python38-32\python.exe D:/code_file/first_web/爬虫/慕课/慕课01.py
[<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>]

Process finished with exit code 0

```





```python
print(soup.find_all(id='link1'))


[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>]

```



```python
import re

print(soup.find_all(id = re.compile('link')))  # 正则表达式 id以link开头的值


-------------------------------------------
[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]


```



##### recursive:是否对子孙全部检索，默认True



```python
print(soup.find_all('a'))

print(soup.find_all('a',recursive=False))   # 判断直接子节点有a标签。

------------------------------------

[<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>, <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>]

[]
```



##### string:<>...</>中字符串区域的检索字符串

 

```python
print(soup)

print(soup.find_all(string = "Basic Python"))   #必须全部匹配 否则需要正则表达式

import re

print(soup.find_all(string = re.compile("python")))   #包含python的全部检索出来，区分大小写


-------------------------------------------

<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
</body></html>

['Basic Python']


['This is a python demo page', 'The demo python introduces several python courses.']

```



##### soup()  等价于 soup.find_all()



##### BeautlSoup扩展方法



| 方法                        | 说明                                                         |
| --------------------------- | ------------------------------------------------------------ |
| <>.find()                   | 搜索且只返回一个参数，字符串类型，同 .find_all()参数         |
| <>.find_parents()           | 在先辈节点中搜索，返回列表类型，同 .find_all()参数           |
| <>.find_parent()            | 在先辈节点中返回一个结果，字符串类型，同 .find_all()参数     |
| <>.find_next_siblings()     | 在后续平行节点中搜索，返回列表类型，同 .find_all()参数       |
| <>.find_next_sibling()      | 在后续平行节点中返回一个结果，字符串类型，同 .find_all()参数 |
| <>.find_previous_siblings() | 在前续平行节点中搜索，返回类别类型，同 .find_all()参数       |
| <>.find_previous_sibling()  | 在前续平行节点中返回一个结果，字符串类型，同 .find_all()参数 |



#### 单元小结



### 单元6:中国大学实例排名

#### 中国大学排名定向爬虫 实例介绍

http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html

程序的结构设计

步骤1：从网络上获取大学排名网页内容  getHTMLText()

步骤2：提取网页内容中信息到合适的数据结构 fillUnivList()

步骤3：利用数据结构展示并输出结果 printUnivList()



#### 中国大学排名定向爬虫 实例编写



```python
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout =30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivList(ulist,num):
    print("{:^10}\t{:^15}\t{:^10}".format("排名","学校","得分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^15}\t{:^10}".format(u[0],u[1],u[2]))



def main():
    uinfo =[]
    url = 'http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)  # 20个大学

main()


-------------------------------------------------------------

D:\develop_study\python\Python38-32\python.exe D:/code_file/first_web/爬虫/慕课/慕课01.py
    排名    	      学校       	    得分    
    1     	   清华大学（北京）    	    大陆    
    2     	     北京大学      	    大陆    
    3     	    香港中文大学     	    香港    
    4     	     浙江大学      	    大陆    
    5     	     香港大学      	    香港    
    6     	   中国科学技术大学    	    大陆    
    7     	    上海交通大学     	    大陆    
    8     	     复旦大学      	    大陆    
    9     	   清华大学（新竹）    	    台湾    
    10    	     台湾大学      	    台湾    
    11    	    北京师范大学     	    大陆    
    12    	    香港城市大学     	    香港    
    13    	    香港科技大学     	    香港    
    14    	     南京大学      	    大陆    
    15    	    华中科技大学     	    大陆    
    16    	   中山大学（广州）    	    大陆    
    17    	    香港理工大学     	    香港    
    18    	   交通大学（新竹）    	    台湾    
    19    	    哈尔滨工业大学    	    大陆    
    20    	    澳门科技大学     	    澳门    

Process finished with exit code 0

```



### 单元7：实例2：淘宝商品比价定向爬虫（失败）



#### 实例介绍



#### 实例编写

 淘宝更新太快，课程中方法与实际不一致。



### 单元8：实例3 股票数据定向爬虫



#### 实例介绍

候选网站：新浪股票https://finance.sina.com.cn/stock/、

​					百度股票，好像已经打不开了。



#### 实例编写

​	案例太老，主要学习方法。

#### 实例优化





## 第四周：网络爬虫之框架



### 单元10:Sracpy 爬虫框架



#### 介绍

https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted

https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted

```python
import pip._internal.pep425tags

print(pip._internal.pep425tags.get_supported())

-----------------------------------------------------
[<cp38-cp38-win32 @ 53656392>, <cp38-abi3-win32 @ 53657000>, <cp38-none-win32 @ 53797960>, <cp37-abi3-win32 @ 53444008>, <cp36-abi3-win32 @ 53798088>, <cp35-abi3-win32 @ 53798216>, <cp34-abi3-win32 @ 53798344>, <cp33-abi3-win32 @ 53798472>, <cp32-abi3-win32 @ 53798600>, <py38-none-win32 @ 53798856>, <py3-none-win32 @ 53798888>, <py37-none-win32 @ 53798984>, <py36-none-win32 @ 53799112>, <py35-none-win32 @ 53799240>, <py34-none-win32 @ 53799368>, <py33-none-win32 @ 53799496>, <py32-none-win32 @ 53799624>, <py31-none-win32 @ 53799752>, <py30-none-win32 @ 53799880>, <cp38-none-any @ 53800136>, <py38-none-any @ 53800008>, <py3-none-any @ 53800264>, <py37-none-any @ 53800392>, <py36-none-any @ 53800520>, <py35-none-any @ 53800648>, <py34-none-any @ 53800776>, <py33-none-any @ 53800904>, <py32-none-any @ 53809256>, <py31-none-any @ 53809384>, <py30-none-any @ 53809512>]
```







scrapy依赖安装



