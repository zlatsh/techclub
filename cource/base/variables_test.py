'''
Python的函数参数传递

所有的变量都可以理解是内存中一个对象的“引用”，或者，也可以看似c中void*的感觉。

这里记住的是类型是属于对象的，而不是变量。
而对象有两种,“可更改”（mutable）与“不可更改”（immutable）对象。在python中，strings, tuples, 和numbers是不可更改的对象，而list,dict等则是可以修改的对象。(这就是这个问题的重点)


'''




def myfun(a):
    a = 2

a = 1
print("调用myfun之前:",a)
myfun(a)
print("调用myfun之后:",a)

# a的值在myfun调用前后一样吗? 为什么



def yourfun(b):
    b[0] += 10

b = [1,2]
print("调用yourfun之前:",b)
yourfun(b)
print("调用yourfun之后:",b)

def yourfun1(b):
    try:
        #b[0] += 10
        print(b)
        a = b
    except Exception as err:
        print("err:",err)
    finally:
        print("over")

    print("last")

b = (1,2)
print("调用yourfun1之前:",b)
yourfun1(b)
print("调用yourfun1之后:",b)


def herfun(c):
    c = '2'

c = '1'
print("调用herfun之前:",c)
myfun(c)
print("调用herfun之后:",c)


exit()