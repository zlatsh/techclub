
def foo():
    return 1
foo()

# 作用域
a_str = "hello world"
print(globals())


a_string = "This is a global variable"
def foo_string():
     a_string = "test" # 1
     print(locals())
foo_string()

print(a_string) # 2


# 函数参数
def foo_para(x):
    print(locals())


foo_para(1)


def foo_paras(x, y=0):  # 1
    return x - y


print(foo_paras(3, 1) )

print(foo_paras(3)) # 3


# 嵌套函数
# Python允许创建嵌套函数。这意味着我们可以在函数里面定义函数而且现有的作用域和变量生存周期依旧适用
def outer():
    x = 1

    def inner():
        print(x)  # 1

    inner()  # 2

outer()


# 一级类对象
print("一级类对象")
# 在python里，函数只是一些普通的值而已和其他的值一毛一样。
# 这就是说你可以把函数想参数一样传递给其他的函数或者说从函数了里面返回函数！

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def apply(func, x, y):  # 1
    return func(x, y)  # 2


print(apply(add, 2, 1) ) # 3
print(apply(sub, 2, 1))


# 必包
print("必包")
# 嵌套定义在非全局作用域里面的函数能够记住它在被定义的时候它所处的封闭命名空间
def outer_clo():
    x = 1

    def inner_clo():
        print(x)  # 1

    return inner_clo


foo1 = outer_clo()
print("foo1==",foo1)
foo1()


def outer_clo2(x):
     def inner():
         print(x) # 1
     return inner
print1 = outer_clo2(1)
print2 = outer_clo2(2)
print1()
print2()


# 装饰器
print("装饰器")

#

def outer1(some_func):
    def inner():
        print("before some_func11")
        ret = some_func()  # 1
        return ret + 2

    return inner

def outer(some_func):
     def inner():
         print("before some_func")
         ret = some_func() # 1
         return ret + 1
     return inner

def foo_deco():
     return 1
decorated = outer(foo_deco) # 2
print(decorated())



print("@@@@")

@outer1
@outer
def foo_deco2():
    return 9

print(foo_deco2())

