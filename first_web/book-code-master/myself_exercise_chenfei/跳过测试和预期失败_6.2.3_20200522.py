import unittest

class MyTest(unittest.TestCase):

    @unittest.skip('直接跳过测试')
    def test_skip(self):
        print('test aaa')

    @unittest.skipIf(3<2,"当条件为真时跳过测试")
    def test_skip_if(self):
        print('test bbb')

    @unittest.skipUnless(3>2,'当条件为真时执行测试')
    def test_skip_unless(self):
        print('test ccc')

    @unittest.expectedFailure  # 不管执行结果是否失败，都将测试标记为失败，但不会抛出失败信息。
    def test_expected_failure(self):
        self.assertEqual(3,3)


if   __name__ =='__main__':
    unittest.main()