import unittest

class TestMethod(unittest.TestCase):
    def setUp(self):
        print('test-->setup')
    def tearDown(self):
        print('test--->tearDown')

    def test_01(self):
        print('这个第一个测试方法')

    def test_02(self):
        print('这个第二个测试方法')

if __name__ == '__main__':
    unittest.main()