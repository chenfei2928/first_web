# #
# # #装饰器   不改变原有代码函数的基础上，给函数增加功能
# #
# # flag = False
# # def login():
# #     global flag
# #     flag = True
# #
# # def add():
# #     pass
# #
# # def upd():
# #     pass
# #
# # def remove():
# #     pass
# #
# # def search():
# #     pass
#
# def wrapper(fn): #把被装饰的函数传递进来
#     def inner():
#         print('被装饰函数之前')
#         fn()  # 执行被装饰的函数
#         print('被装饰之后')
#     return inner #把内层函数返回
#
#
# def add():
#     print('我是新增函数')
#
# # a = wrapper(add)
# #
# # a()
# #
# # add()
#
# add = wrapper(add)   # 装饰器的灵魂
#
#
# add()


# 语法糖

def wrapper(fn):
    def inner():
        print('执行装饰器前')
        fn()
        print('执行之后')
    return inner


@wrapper
def add():
    print('我叫add')


add()

print(add)


# 装饰器不改变原来函数的基础上，给函数添加新的功能
