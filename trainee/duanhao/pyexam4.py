goods = [
    {"name":"电脑","price":1999},
    {"name":"鼠标","price":10},
    {"name":"游艇","price":20},
    {"name":"喜茶","price":98},
]

user_assets = 100


def buy(name):
    global user_assets
    for thing in goods:
        if thing['name'] == name:
            if thing['price'] <= user_assets:
                user_assets = user_assets - thing['price']
                return 1
            else:
                return 2
    return 0


def get_buy():
    val = input('请输入要购买的商品：')
    flag = buy(val)
    if flag == 1:
        print('购买成功')
    elif flag == 2:
        print('余额不足')
    else:
        print('商品不存在')


while(True):
    get_buy()
