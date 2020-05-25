
# def func():
#     print('你好')
#     func()
#
# func()


# import sys
# print(sys.getrecursionlimit())
#

def f(x):
    if x>0:
        return x +f(x-1)
    else:
        return 0

print(f(100))