
# for n in range(2, 10):
#     print("n=",n)
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '等于', x, '*', n//x)
#             break
#     else:
#         # 循环中没有找到元素
#         print(n, ' 是质数')

n =4
for x in range(2, n):
    print("x=",x)
    if n % x == 0:
        print(n, '等于', x, '*', n // x)
        break
else:
    # 循环中没有找到元素
    print(n, ' 是质数')