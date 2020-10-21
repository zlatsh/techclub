#用户输入一个数字n，打印出n个数字相加之后的结果（4+44+444+4444+.....+=？），例如用户输入3，则打印出4+44+444的计算结果。
class  pyexam2:

    def test(self,n,value):
        try:
            n = int(n)
            val = str(value)
            sumJ = val
            va = int(value)


            #方法二
            s = 0
            sum = 0
            for i in range(int(n)):
                s += pow(10, i)
                sum += s * va
            print(sum)

            #方法一
            # for i in range(n - 1):
            #     sumJ = sumJ + val
            #     va = va + int(sumJ)
            # print(va)
        except:
            print("您输入的数字格式不正确！")


if __name__ == '__main__':
     py = pyexam2()
     py.test(input(" n："),input("请输入您的数字："))














