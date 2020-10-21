
# MRO（Method Resolution Order）：方法解析顺序。



# C3算法解决了单调性问题和只能继承无法重写问题
# 都只有那个merge list的公式法，想看的话网上很多，自己可以查。但是从公式很难理解到解决这个问题的本质。
# 如下例子可以看出C3算法的本质



class D(object):
    pass

class E(object):
    pass

class F(object):
    pass

class C(D, F):
    pass

class B(E, D):
    pass

class A(B, C):
    pass

if __name__ == '__main__':
    print(A.__mro__)