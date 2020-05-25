import unittest

class TestBdd(unittest.TestCase):

    def setUp(self) -> None:
        print('test TestBdd:')

    def test_ccc(self):
        print('test ccc')

    def test_aaa(self):
        print('test aaa')

class TestAdd(unittest.TestCase):
    def setUp(self) -> None:
        print('test TestAdd')

    def test_bbb(self):
        print('test bbb')

# if __name__ == '__main__':
#     unittest.main()

if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestBdd('test_aaa'))
    suite.addTest(TestAdd('test_bbb'))
    suite.addTest(TestBdd('test_ccc'))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)


unittest.skip(reason)
unittest.skipIf(condition,rason)
unittest.skipUnless(condition,reason)
unittest.expectedFailure()
