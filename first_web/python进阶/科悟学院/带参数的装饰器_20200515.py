def gua_outer(name):
    def gua(fn):
        def inner(*args,**kwargs):
            print(f'开启{name}外挂')
            ret = fn(*args,**kwargs)
            print(f'关闭{name}外挂')
            return ret
        return inner
    return gua


@gua_outer('饕餮')
def dnf():
    print('我要dnf')

@gua_outer('lll')
def lol():
    print('我要LOL')


dnf()
lol()
