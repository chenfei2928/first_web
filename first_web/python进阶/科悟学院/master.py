def func():
    print('我是master')

name = '大佬'

print('哈哈哈哈哈哈')


print(__name__)  # 内置变量

# 当此模块被直接运行时 值是 __main__
# 程序的入口，运行的入口
if __name__ == '__main__':   # 程序的入口   自己运行被执行，被其他模块导入不执行
    print('以下是我的测试代码')
    print('我想给你唱首歌')

