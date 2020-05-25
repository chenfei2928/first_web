
# 类 驼峰体
class Dog:
    d_type = '京巴'  # 类属性，类变量   公共属性
    sss ='sss'

    def __init__(self,name,age):     #初始方法，构造方法，构造函数 ，实例化时进行一些初始化工作
        self.nm = name
        self.ag = age
        print('哈哈哈',name,age)
    def say_hi(this):  #self 代办实例本身,第一个参数必须是self
        print("hello, I am a dog ,my type is ",this.d_type,this.nm,this.ag)


d = Dog("majj",3)  # 实例
d2 =Dog('mansan',5)

d.say_hi()  # 实例.方法 method
d2.say_hi()

Dog.d_type ='藏獒'
print(d.d_type,d.sss,d2.d_type)
print(id(d.d_type),id(d.d_type))

