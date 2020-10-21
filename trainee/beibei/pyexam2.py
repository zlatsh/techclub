#用户输入一个数字n，打印出n个数字相加之后的结果（4+44+444+4444+.....+=？），例如用户输入3，则打印出4+44+444的计算结果。
n = input("请输入一个数字：")
i = int(n)
m = 4
sum1 = 0
sum2 = 0
for j in range(i):
    sum1 = sum1 + m
    m = m*10
    #print(sum1)
    sum2 = sum2 + sum1
print(sum2)
