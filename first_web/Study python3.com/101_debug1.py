import requests

# 用requests获取销量信息
res = requests.get('http://cdn1.python3.vip/files/py/0016_price')
content = res.text

# 下面两个变量记录当前找到的销量最多的手机和卖出数量
# 初始值都是None
mostsoldphone = None
mostsoldcount = None

for info in content.splitlines():
    info = info.strip()
    # 去掉空行
    if not info:
        continue

    items = info.split(',')
    # 销量在倒数第二列，获取销量信息
    soldcount = items[-2]
    # 型号在 第一列，  获取型号信息
    phonetype = items[0]

    # 如果前面已经有销量最多的手机记录，和当前这款手机销量比较
    if mostsoldphone:
        # 如果当前这款手机销量更高，把它置为最热卖手机
        if mostsoldcount < soldcount:
            mostsoldcount = soldcount
            mostsoldphone = phonetype

    # 如果前面没有有销量最多的手机记录，说明这是第一条记录
    # 暂时先把它置为最热卖手机
    else:
        mostsoldcount = soldcount
        mostsoldphone = phonetype

print(f'最热卖手机是 {mostsoldphone}, 销量是 {mostsoldcount}')