from email.mime.multipart import MIMEMultipart # 一份邮件
from email.mime.text import MIMEText   #文本
from email.mime.image import MIMEImage   # 图片
from email.mime.application import MIMEApplication  #附件

import smtplib  # 发送邮件

sender = "chenfei@tus-est.com"  # 发送人

to_list = ['luowei@tus-est.com']  # 收件人
cc_list = ['cf2928@163.com','chenfei@tus-est.com']   # 抄送

subject = "工作周报"  # 主题

em = MIMEMultipart()

em['Subject'] = subject
em['From'] = sender
em['To'] = ','.join(to_list)
em['cc'] = ','.join(cc_list)

# ## 发送文本
# content = MIMEText('pip命令默认会连接在国外的python官方服务器下载，速度比较慢，你还可以使用国内的豆瓣源，数据会定期同步国外官网，速度快好多')
# em.attach(content)

### 发送html代码

# content = MIMEText('<h1>我是一只鱼</h1>',_subtype='html')
# em.attach(content)

# content = MIMEText("<a href='http://www.baidu.com'><img src='cid:jay' width='200px'/></a>",_subtype='html')  #调用图片cid值
# em.attach(content)  # 效果，邮件中点击图片，跳转百度
#

# # 发送图片
# img = MIMEImage(open('tu.jpg',mode = 'rb').read())   # 本地图片路径
# img.add_header("Content-ID",'jay') # 给图片设置ID值
# em.attach(img)


# 附件
app = MIMEApplication(open("E:\\新环卫工作\\2020年1~2季度运维日志V1.0.xlsx",mode = 'rb').read())
app.add_header('content-disposition', 'attachment', filename='2020_1-2季度运维日志V1.0.xlsx')
em.attach(app)

app = MIMEApplication(open("E:\\新环卫工作\\实施问题记录表20200518-20200522.xlsx",mode = 'rb').read())
app.add_header('content-disposition', 'attachment', filename='实施问题记录表_2020.05.18-2020.05.22.xlsx')
em.attach(app)

app = MIMEApplication(open("E:\\新环卫工作\\工作周月年报\\陈飞-周报_20200522.xlsx",mode = 'rb').read())
app.add_header('content-disposition', 'attachment', filename='陈飞-周报_20200522.xlsx')
em.attach(app)



# 邮件服务器
auth_pwd ='6dc27E1710EF21EE'
# qq邮箱授权码        nqcoykmsfmefbicj
# tus-est邮箱授权码   6dc27E1710EF21EE



# 链接 qq邮件服务器
smtp = smtplib.SMTP()
smtp.connect('smtp.tus-est.com')

#登陆

smtp.login(sender,auth_pwd)

# 发送邮件

smtp.send_message(em)

# 关闭连接

smtp.close()
