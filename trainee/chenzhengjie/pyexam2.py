'''［pyexam2］用户输入一个数字n，打印出n个数字相加之后的结果（4+44+444+4444+.....+=？），
例如用户输入3，则打印出4+44+444的计算结果。'''
a = int(input("请输入几个数相加："))
result= []
for i in range (1,a+1):
    result.append(int('4'*i))
    print(result[i-1])
print("以上数字相加和为：",sum(result))