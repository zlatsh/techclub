# super()的作用，以及在什么情况下使用super()？
#
# super()方法的漂亮之处在于，你不需要在定义子类构造器时，明确的指定子类的基类并显式的调用，即不需要明确的提供父类，
# 这样做的好处就是，如果你改变了继承的父类，你只需要修改一行代码（class代码行），而不需要在大量代码中去查找那个要修改的基类
#
# 在super机制里可以保证公共父类仅被执行一次，至于执行的顺序，是按照mro进行的


class yeye():
    def dump(self):
        print("yy")

class baba(yeye):

    def dump1(self):
        print("bb")

class mama():
    def dump(self):
        print("mm")

class child(baba,mama):
    def dump2(self):
        print("yy")

a = child()
a.dump()

exit()

class FooParent:
    def __init__(self):
        print('FooParent init')
    def bar(self, message):
        print('FooParent.bar')
        print(message)

class FooChild(FooParent):
    def __init__(self):
        print('FooChild init')
    def bar(self, message):
        print('FooChild.bar')
        FooParent.bar(self, message)


class A:
    def __init__(self):
        print('A init')
    def bar(self, message):
        print('in A.bar')
        print(message)

class AChild(A):
    def __init__(self):
        print('AChild init')
    def bar(self, message):
        print('in AChild.bar')
        super(AChild, self).bar(message)

class B(A):
    def __init__(self):
        print('B init')
    def bar(self, message):
        print('in B.bar')
        super(B, self).bar(message)

class C(AChild,B):
    def __init__(self):
        print('C init')
    def bar(self, message):
        print('in C.bar')
        super(C, self).bar(message)

class D(AChild,B):
    def __init__(self):
        print('D init')
    def bar(self, message):
        print('in D.bar')
        #super(C, self).bar(message)
        A.bar(self,message)

FooChild().bar("Hello, World.")
print('----')
AChild().bar("Hello, World.")
print('----')
B().bar("Hello, World.")


print('----')
C().bar("Hello, World.")
print('----')
D().bar("Hello, World.")