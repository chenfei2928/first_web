# #
# # # 统一了容器类型循环遍历的标准
# #
# # for c in "你好好":
# #     print(c)
# #
# #
# # for i in 124:
# #     print(i)
#
# print(dir(str)) # 数据类型能执行的操作 #__iter__
# print('---------------------------------------------')
# print(dir(list)) # __iter__
#
# print('---------------------------------------------')
#
# print(dir(dict)) # __iter__
# print('---------------------------------------------')
# #
# # print(dir(int))  # 无 __iter__
# # print('---------------------------------------------')
# #
# # print(dir(bool)) # 无 __iter__
# #
# #
# # # iter  迭代  iterable 可迭代的。
# #
# #
# #
#
# lst = ['你好','sss','good']
# it = lst.__iter__()
# print(it)
# print(dir(it))
# ret = it.__next__()
# print(ret)
#
# ret = it.__next__()
# print(ret)
#
# ret = it.__next__()
# print(ret)
#
# ret = it.__next__()
# print(ret)


# 使用步骤

# 1、__iter__ 拿到可迭代对象的迭代器
# 2、用迭代器执行 __next__拿到元素
# 3、重复第二部，反复执行，直到出现StopIteration结束


s = {'合理','嗯嗯','二'}
it = s.__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
