#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字，例如12345，是5位数，逆序输出为5 4 3 2 1
def test(n):
    try:
        value = int(n)
        if len(n) <= 5 and value > 0:
            print(n, "是%d位数" % len(n))
            print("逆序后：", ''.join(reversed(n)))
        else:
            raise TypeError(n + '不是一个小于5位的正整数')
    except TypeError as error:
        print(error)
    except:
        print("输入格式有误")

if __name__ == "__main__":
    inp = input("请输入您的数值：")
    test(inp)
