#［pyexam1］：编写代码, 打印1-1百万之内的偶数。
result = []
for i in range(1,1000001):
    if i% 2 == 0:
        result.append(i)
print(result)