def  pressHorn():
    print('嘟嘟~~~~~~')

benzCar = {
    'brand'   : '奔驰',
    'country' : '德国',
    'price'   : 300000,
    'pressHorn' : pressHorn # 字典对象的值可以是一个函数对象
}

# 我可以这样执行它的行为
benzCar['pressHorn']()


