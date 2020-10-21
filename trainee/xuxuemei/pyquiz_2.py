#有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

def test(n):
    try:
        num = int(n)
        listvalue = list(range(1,num+1))
        print(listvalue)

        va = xun(listvalue)
        print("最后留下来的是原来的号数为：",va)
    except:
        print("请输入正确的人数")

def xun(list):
    index = -1
    sum = 0
    flog = True
    while flog:
        # yield i
        # print(i)
        index+=1
        sum+=1
        if sum == 3:
            print("移除：",list.pop(index))
            sum=0#重置计数器
            index-=1#相应的下标也要等于向前移动一位
        if index==len(list)-1:
            index=-1
            print(list)
        if len(list)==1:
            flog=False
    return list[0]


if __name__=='__main__':
    n = input("有n个人围成一圈，顺序排号！n:")
    test(n)





















