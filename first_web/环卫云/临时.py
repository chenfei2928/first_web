
import requests
import datetime
url = "https://static.hdslb.com/phoenix/dist/css/comment.min.css" \

# 视频的url地址
html = requests.get(url)

# content返回的的数据（注意，是二进制类型哦！）
html = html.content
start_down_time = datetime.datetime.now()
print('开始下载叶问,时间：{}'.format(start_down_time))
# 因为是二进制数据，所以必须要要采用wb的形式来写入
with open(r'e:\临时停靠\叶问4.mp4', 'wb') as f:
    f.write(html)
end_time = datetime.datetime.now()
print('电影下载结束,时间：{}'.format(end_time))