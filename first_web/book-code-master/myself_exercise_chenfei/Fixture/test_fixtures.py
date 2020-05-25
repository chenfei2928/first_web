
"""
Fixture 通常用来对测试方法、测试函数、测试类和整个测试文件进行初始化或还原测试环境。
"""
#
# import  pytest

def multiply(a,b):
    return a * b

# ---------Fixture---------------

def setup_module(module):
    print('setup_module=========================>')

def teardown_module(module):
    print('teardown_module======================>')

def setup_function(function):
    print('setup_function---------------->')

def teardown_function(function):
    print('teardown_function------------->')

def setup():
    print('setup------->')

def teardown():
    print('teardown----->')

#=============测试用例+++++

def test_multiply_3_4():
    print('test_numbers_3_4')
    assert multiply(3,4) == 12

def test_multiply_a():
    print('test_strings_a_3')
    assert multiply('a',3)=='aaa'

# if __name__ == '__main__':
#     pytest.main()


git测试

#商城100%完成


