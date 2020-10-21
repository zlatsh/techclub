# 如何判断一个对象是否是一个类的实例？   isinstance(s, myclass)来判断如果是s是mycalss的实例，返回True，否则返回False
# Python语言包含了很多优秀的特性，其中多重继承就是其中之一，但是多重继承会引发很多问题，
# 比如二义性，Python中一切皆引用，这使得他不会像C++一样使用虚基类处理基类对象重复的问题，但是如果父类存在同名函数的时候还是会产生二义性，
# Python中处理这种问题的方法就是MRO。


class A():
    def __init__(self):
        self.a = 'hello'

    def dump(self):
        print('dump==',self.a)


class B():
    def __init__(self):
        self.b = 'hello b'

class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

if __name__ =='__main__':
    a = A()
    a.dump()
    print(isinstance(a,A))
    print(isinstance(a, B))

    print('========')

    print(Parent.x, Child1.x, Child2.x)
    Child1.x = 2
    print(Parent.x, Child1.x, Child2.x)
    Parent.x = 3
    print(Parent.x, Child1.x, Child2.x)