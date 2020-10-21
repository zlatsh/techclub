user_assets=100
goods = [
{"name":"电脑","price":1999},
{"name":"鼠标","price":10},
{"name":"游艇","price":20},
{"name":"喜茶","price":98},
]

def  pyexam4(money):
    str = input("欢迎来到小型交易系统~请输入您想买的产品：电脑，鼠标，游艇，喜茶：")
    print(str)
    if str == '退出':
        return
    else:
        store(str,money)


def store(ctx,money):

    for i in range(len(goods)):
        if ctx==goods[i]["name"]:
            empty = input("您是否要购买(Y/N)："+ctx)
            now = money
            if empty=="Y":
                a = money-goods[i]["price"]
                if a > 0:
                    print("购买成功，剩余余额："+str(a))
                    pyexam4(a)
                else:
                    print("余额不足，为："+str(now)+"！请充值")
                    pyexam4(now)
            elif empty == 'N':
                pyexam4( money)

pyexam4(user_assets)