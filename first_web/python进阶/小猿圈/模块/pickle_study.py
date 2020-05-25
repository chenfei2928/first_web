import pickle


d = {
    "name":"chen",
    "role":"police",
    "blood": 76,
    "weapon":"ak47"
}

alive_palyers = ['alex','jack','rain']


print(pickle.dumps(d))  #序列号
d_dump = pickle.dumps(d)
print(pickle.loads(d_dump))  # 反序列号 加载


f = open("game.pkl", 'wb')  # 写入二进制数据
pickle.dump(d,f)
pickle.dump(alive_palyers,f)


# dump		写入文件

# dumps	  生成序列化的字符串


import datetime
pickle