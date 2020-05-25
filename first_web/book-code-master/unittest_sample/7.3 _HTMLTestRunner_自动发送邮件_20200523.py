import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import yagmail

# 把测试报告作为附件发送到指定邮箱

def send_mail(report):
    yag = yagmail.SMTP(user='chenfei@tus-est.com',
                       password='6dc27E1710EF21EE',
                       host ='smtp.tus-est.com')
    subject ='主题，自动化测试报告'
    contents = '正文，请查看附件。'
    yag.send('cf2928@163.com',subject,contents,report)
    print('email has send out!')


if __name__ == '__main__':
    # 定义测试用例的目录为当前目录下的test_case目录

    test_dir = './web_case'
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

    #生成HTML格式的报告
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")  # 取当前日期时间
    html_report = './'+now_time+'result.html'
    fp = open(now_time+'result.html','wb')

    rnnner = HTMLTestRunner(stream =fp,
                            title='百度搜索测试报告',
                            description='运行环境：Windows10，Chrome浏览器'
                            )

    rnnner.run(suit)
    fp.close()
    send_mail(html_report)



