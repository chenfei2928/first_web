def binary_search(list, item):
 low = 0
 high = len(list)-1                         # Tracking list head and tail
 n = 0
 while low <= high:
     mid = int((low + high)/2)              #Take the middle number
     guess = list[mid]
     n += 1
     if list[mid]==item:
         print(n)
         return mid
     if list[mid]<item:                     #Change the head and tail pointers
         low = mid + 1
     else:
         high = (mid-1)
 return None

m=[1,2,3,4,8,9,11,12,14,18,19,20,28]
print(binary_search(m,14))
