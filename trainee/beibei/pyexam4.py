# [pyexam4］：利用控制台交互界面，模拟一个小型的交易系统，开启后，提示商品信息，当用户输入要购买的商品后，
# 提示购买成功，或者余额不足，可连续购买。例如：
# 用户输入“电脑”，提示余额不足；
# 用户输入“喜茶”，提示购买成功，再输入“鼠标”，提示余额不足
# 系统数据:
# user_assets=100
# goods = [
# {"name": "电脑", "price": 1999},
# {"name": "鼠标", "price": 10},
# {"name": "游艇", "price": 20},
# {"name": "喜茶", "price": 98},
# ]
products = {"电脑": 1999, "鼠标": 10, "游艇": 20, "喜茶": 98}
user_assets = 100
a = 0
while True:
    key = input("请输入要购买的商品名称：")
    if key in products.keys():
        # print(products.get(key))
        price = products.get(key)
        if price <= user_assets:
            user_assets = user_assets - price
            print("购买成功,余额为%d元"%user_assets)
        else:
            a = price - user_assets
            print("余额不足，购买此商品还差%d元"%a)
    else:
        print("商品不存在")
