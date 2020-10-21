#采用lambada实现输出任意两个整数的大值
def test(v1,v2):
    try:
        value1 = int(v1)
        value2 = int(v2)
        maxValue = lambda value1, value2: value1 if value1> value2 else value2
        print("最大的数：",maxValue(value1,value2))
    except Exception:
        print("请输入格式正确的整数")

if  __name__=='__main__':
    v1 = input("请输入第一个整数：")
    v2 = input("请输入第二个整数：")
    test(v1,v2)

















