import unittest
from HTMLTestRunner import HTMLTestRunner

#定义测试用例的目录为当前目录下的test_case目录

test_dir = './test_case'
suit = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    #生成HTML格式的报告
    fp = open('./test_report/result20200523.html','wb')
    rnnner = HTMLTestRunner(stream =fp,
                            title='百度搜索测试报告',
                            description='运行环境：Windows10，Chrome浏览器'
                            )

    rnnner.run(suit)
    fp.close()