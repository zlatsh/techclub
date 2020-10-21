# lambda 表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数
# lambda表达式：体现原理就是python允许lambda关键字创建匿名函数，
# 所谓匿名就是python不会创建名称空间，lambda表达式返回可调用的函数对象，这些都符合函数式编程的思想。
#
# lambda函数：首要用途是指点短小的回调函数
#
# lambda [arguments]:expression

a=lambda x,y,z:x+y+z

print(a, type(a))
print(a(3,11,2))



# 内建函数：filter()
# filter(func,iter)   只能处理一个参数(iter)，仅仅将满足func方法的数值过滤出来
print(list(filter(lambda x:x%2 == 0, range(0,10))))



# map(func,iter1,iter2,..) 可以处理多个iter，实现通过func方法对iter1,iter2,..进行处理
print(list(map(lambda x:x**2, range(0,10))))
#print(list(filter(lambda x:x**2, range(0,10))))


# reduce(func,iter,init):仅能处理一个iter，init为初始化值，
# 执行顺序为：先将每个iter内部第一个值和init进行func处理，处理的结果再与iter第二个值进行func处理，直到结束。
from functools import reduce
print(reduce(lambda x, z : x - z, [2, 3, 4, 5, 6], 0))
