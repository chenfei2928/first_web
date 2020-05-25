#
# # def func():
# #     print('1234')
# #     yield "你好"  # 当函数中有yield时，就是一个生成器函数
# #
# #
# # gen = func()
# # print('得到的返回值是',gen)  #<generator object func at 0x03949680>
# # ret = gen.__next__()
# #
# # print(ret)
#
#
# # 一个生成器函数中，可以有多个yield
#
#
# def func():
#     print(11)
#     yield "你好"
#     print(22)
#     yield "你不好"
#     print(33)
#     yield "你到底好不"
#
# gen = func()
# r = gen.__next__()
# print('接受的数据是：',r)
# r2 = gen.__next__()
# print('接受到的2数据是',r2)
#
# r3 = gen.__next__()
# print('接受的数据3是',r3)
#
# r4 =gen.__next__()
# print("接受的r4是",r4)

'''

生成器函数
    1、里面有yield
    2、执行的时候，实际是创建一个生成器出来；
    3、必须使用__next__()来执行一段代码，会自动的执行到下一个yield结束。
    4、yield也是返回的意思，可以让一个函数分段执行
    5、当后面没有yield之后，再次__next__会报错 StopIteration


'''

# 生成器 最大作用 节省内存

#
