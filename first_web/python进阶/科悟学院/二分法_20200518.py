#
# lst = [11,25,46,78,99,265]
#
# n = int(input(">>>"))
#
# for item in lst:
#     if item == n:
#         print('存在')
#         break
# else:
#     print("不存在")

lst = [11,25,46,78,99,265]

n = int(input(">>>"))
left =0
right = len(lst)-1

while left <= right:
    mid = (right-left)//2  # 整除
    if n > lst[mid]:
        left =mid+1
    elif n < lst[mid]:
        right = mid -1
    else:
        print('找到了数据，位置',mid)
        break
else:
    print('不存在')
