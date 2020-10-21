#编写代码, 打印1-1百万之内的偶数。
def  test01(value):
    for i in  range(value):
        if i>0:
            if i%2 == 0:
                print(i)

if __name__ == '__main__':
    test01(1000000)




