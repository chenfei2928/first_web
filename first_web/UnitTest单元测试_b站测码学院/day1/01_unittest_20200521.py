"""

https://www.bilibili.com/video/BV1xJ411v7Eb?from=search&seid=379593409790369798
测码软件测试官方

UnitTest  >>> PyTest

鄙视链
Pytest ——UnitTest ——— RobotFrameWork

"""
import unittest

class fortext(unittest.TestCase):

    # 类的初始化
    @classmethod
    def setUpClass(cls) -> None:
        print('class start')

    @classmethod
    def tearDownClass(cls) -> None: # 类的释放
        print('class end')

    #初始化
    def setUp(self) -> None:
        print('setup')
    def tearDown(self) -> None:
        print('teardown')

    def plus(self,a,b):
        c = a+b
        print(c)
        return c

    def test_a(self):
        print('aaa')

    def test_b(self):
        print('bbb')

    def test_c(self):
        self.plus(1,2)
        print('c')
#
# # 四大组件
#     text Fixture    setUp(前置条件)     setDown(后置条件)
#
#     test case 测试用例
        #     集成 unittest.TestCase ,

      # test suite 测试套件
      #
      # test runner  运行器  一般通过runner来调用suite去执行测试

if __name__ == '__main__':
    unittest.main()

# unittest运行机制
    #   通过在main函数中，调用unittest.main()运行所有内容






#




