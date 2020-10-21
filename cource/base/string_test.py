#import datetime_test

import re

# 字符串的切片

var1 = 'Hello World!'
var2 = "Robot"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
print ("var2[1:-1]: ", var2[1:-1])

# 字符串的拼接

a = "Hello"
b = "Python"

print("a: ", a)
print("b: ", b)
print("a + b 输出结果：", a +' '+ b)
print("a * 2 输出结果：", a * 2)

print ("我叫{},今年{}岁!".format('小明', 10))

s1 = "-"
s2 = ""
seq = ["r", "u", "n", "o", "o", "b"] # 字符串序列
# 对list拼接
print(seq, type(seq))
print(s1.join(seq))
print(s2.join(seq))

# 对tople拼接,效果是一样的, 回顾一下 列表和元组的区别
seq1 = ("r", "u", "n", "o", "o", "b") # 字符串序列
print(seq1, type(seq1))
print(s1.join(seq1))
print(s2.join(seq1))


# 字符串的内容判断

if ("He" in a):
    print("He 在变量 a 中")
else:
    print("He 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

# 特殊字符转义:回车
print('\r')
print('\n')
print(r'\n')
print(R'\n')


# 字符串的拆分
str = "12.23.232.28"
print("str=",str, type(str))
str_list = str.split('.')
print(len(str_list), type(str_list))
print(str_list[0])
print(str_list[1])
print(str_list[-1])
print(str_list, type(str_list))

print(str)
print(str.rjust(15))

str = " I like noah "
print(str)
print(str.lstrip())
print(str.rstrip())
print(str.strip())



print('理解切片的最好方式是把索引视为两个字符之间的点，第一个字符的左边是0，字符串中第n个字符的右边是索引n')
print(' +---+---+---+---+---+ ')
print(' | H | e | l | p | A |')
print(' +---+---+---+---+---+ ')
print(' 0  1  2  3  4  5 ')
print('-5 -4 -3 -2 -1 -0')
print('第一行是字符串中给定的0到5各个索引的位置，第二行是对应的负索引。从i 到j 的切片由这两个标志之间的字符组成')
print('对于非负索引，切片长度就是两索引的差。例如，word[1:3] 的长度是2')