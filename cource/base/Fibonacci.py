
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数


a, b = 0, 1

while b < 20:
    print(b)
    a, b = b, a+b

print("======")
# 上面的方法和相面的方法有什么不同? 为什么?
a, b = 0, 1

while b < 20:
    print(b)
    b = a + b
    a = b

    # t = a
    # a = b
    # b = t + b

