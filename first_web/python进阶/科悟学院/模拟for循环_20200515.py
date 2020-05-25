lst = ['张无忌','谢逊','金毛狮王','鲁迅']

# for 循环内部大致工作机制

it = lst.__iter__()  # 拿到迭代器
while True:
    try:  # 尝试执行
        obj = it.__next__()  # 拿到数据
        print(obj)
    except StopIteration:  # 如何上方代码出现了stopiteration 错误，下面代码开始执行
        break # 结束循环

for itm in lst:
    print(itm)


# Iterable  可迭代对象
# Iterator   迭代器
#         迭代器： 节省内存
#                 惰性机制 （必须访问next的）
#                 不能反复，只能向下执行
#





