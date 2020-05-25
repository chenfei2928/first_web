# # 装饰器雏形
# def wrapper(fn):
#     def inner():
#         print('开挂')
#         fn()
#         print('关闭外挂')
#     return inner
#
# @wrapper
# def dnf():
#     print('我要玩DNF')
#
# dnf()

# 被装饰函数带参数情况

# def wrapper(fn):
#     def inner(*args,**kwargs):
#         print('开挂')
#         fn(*args,**kwargs)
#         print('关闭外挂')
#     return inner
#
# @wrapper
# def dnf(username,password):
#     print(f"登陆账号为{username},密码为{password}我要玩DNF")
#
# @wrapper
# def wz(wx):
#     print(f"使用账号{wx}登陆王者荣耀")
#
#
# @wrapper
# def qq():
#     print('我是快乐的qq')
#

#
# dnf('admin','123456')
# print('------------------我是分割线----------------------')
# wz('大佬')
#
# print('------------------我是分割线----------------------')
#
# qq()
#
# print('------------------我是分割线----------------------')
#
# def wrapper(fn):
#     def inner(*args,**kwargs):
#         print('开挂')
#         ret =fn(*args,**kwargs)
#         print('关闭外挂')
#         return ret
#     return inner
#
# @wrapper
# def dnf2():
#     print('我要玩DNF')
#     return "屠龙刀"
#
# ret = dnf2()
#
# print('我得到了一把:',ret)


# 通用装饰器
#
# def wrapper(fn):
#     def inner(*args,**kwargs):
#         """"在执行目标函数之前"""
#         ret = fn(*args,**kwargs)
#         """在执行目标函数后"""
#         return ret
#     return inner()
#
# @wrapper
# def target():
#     pass
#
# target()


# 装饰器的应用


# 在执行目标函数的时候，判断是否登陆，若没有登陆，请登陆，登陆成功后，才能执行目标。
flag = False

def login_verify(fn):
    """
    这里是登陆验证的装饰器：
    ：:param fn  被装饰的函数
     :return

    """

    def inner(*args,**kwargs):
        while 1:  # 反复判断登陆状态
            if flag:
                ret = fn(*args,**kwargs)
                return ret # 返回结果
            else:
                login()
    return inner

def login():
    global flag
    username = input('请输入用户名：')
    password = input('请输入密码:')
    if username =='admin' and password =='123456':
        flag = True
        print('登陆成功')
    else:
        print('登陆失败')



@login_verify
def add():
    print('我要执行新增操作')


@login_verify
def upd():
    print('我要执行修改操作')


add()

upd()