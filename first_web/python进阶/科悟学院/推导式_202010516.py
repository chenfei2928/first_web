

# 列表推导式
lst = [i for i in range(1,11)]
print(lst)

# 奇数

lst2 =[i for i in range(1,11) if i%2==1]
print(lst2)

lst2 =[i**2 for i in range(1,11) if i%2==1]
print(lst2)


# 字典推导式

lst = ['你好','哈哈','扣款']

d = {i:lst[i] for i in range(len(lst))}
print(d)


# 集合推导式

lst3 = ['校招','张三丰','金毛狮王']
s = {item for item in lst3}
print(s)