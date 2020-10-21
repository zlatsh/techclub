# 请写出一段Python代码实现删除一个list里面的重复元素
#
# 答：
#
# 1,使用set函数，set(list)
#
# 2，使用字典函数，
#

import time
from datetime import *

a=[1,2,4,2,4,5,6,5,7,8,9,0]



# 采用set
dt_now = dt_pre = datetime.now()
print("a==",datetime.now())


b=set(a)
print(a,type(b))
print(b)
dt_now = datetime.now()
print(dt_now - dt_pre)
dt_pre = dt_now


# 采用字典
b={}
b=b.fromkeys(a)
print(b, type(b))
c=list(b.keys())
print(c)
dt_now = datetime.now()
print(dt_now - dt_pre)

exit()

# a.sort(reverse=True)
# print(a)
# a.sort(reverse=False)
# print(a)