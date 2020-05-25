"""
pytest使用测试了， 类必须以Test开头，首字母大写
"""

def multiply(a,b):
    return a*b

class TestMultiply:
    @classmethod
    def setup_class(cls):
        print('setup class==================>')

    @classmethod
    def teardown_class(cls):
        print('teardown class===============>')

    def setup_method(self,method):
        print('setup_method-------->')

    def teardown_method(self,method):
        print('teardown_method------>')

    def setup(self):
        print('setup----->')
    def teardown(self):
        print('teardown-->')

    #测试用例

    def test_numbers_5_6(self):
        print('test_numbers_5_6')
        assert multiply(5,6) == 30

    def test_strings_b_2(self):
        print('test_strings_b_2')
        assert multiply('b',2) == 'bb'