# class Myclass(object):
#     def say_hello(self,name):
#         return "hello"+ name
#
# mc = Myclass()
#
# print(mc.say_hello('Jim'))
#


class A:
    def __init__(self,a,b):
        print('Hello world')
        self.a = int(a)
        self.b = int(b)
    def add(self):
        return self.a +self.b

count = A('4',6)
print(count.add())


class B(A):

    def sub(self,a,b):
        return a - b

print(B(2,3).add())

