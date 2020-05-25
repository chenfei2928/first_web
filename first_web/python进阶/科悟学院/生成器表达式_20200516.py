#
# # q = (i for i in range(5))
# # print(q)
#
# # print(q.__next__())
# # print(q.__next__())
# # print(q.__next__())
# # print(q.__next__())
#
# # for item in q:
# #     print(item)
#
# # print(list(q))
#
# # print(tuple(q))  # 元祖
#
# # print(set(q))  # 集合
# #
# #
#
# def func():
#     print(111)
#     yield 222
#
# g = func()
#
# g1= (i for i in g)
# g2 =(i for i in g1)
#
#
# print(list(g2))
#
# print(list(g))
# print(list(g1))



def func():
    lst1 =['麻花1号','马里一号','222']
    lst2 =['麻花1号2','马里一号2','2222']
    # for item in lst1:
    #     yield item
    # for item in lst2:
    #     yield item
    yield from lst1
    yield from lst2

g = func()

print(list(g))