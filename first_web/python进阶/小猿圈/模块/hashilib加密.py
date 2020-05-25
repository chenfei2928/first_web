
# 防止被篡改
# 防止直接看到明文
# 防止抵赖


import hashlib
m = hashlib.md5()
m.update(b'hello alex')
print(m.hexdigest()) # 16进制md5值

m.update('欢迎来到小猿圈'.encode(('utf-8')))

print(m.digest())  # 消化
print(m.hexdigest()) # 16进制md5值


m2 = hashlib.md5()
m2.update("hello alex欢迎来到小猿圈".encode('utf-8'))
print(m2.hexdigest())


#撞库
#脱库
#加盐



