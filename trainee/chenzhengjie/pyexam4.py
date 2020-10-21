'''［pyexam4］：利用控制台交互界面，模拟一个小型的交易系统，开启后，提示商品信息，当用户输入要购买的商品后，提示购买成功，或者余额不足，可连续购买。
例如：用户输入“电脑”，提示余额不足；用户输入“喜茶”，提示购买成功，再输入“鼠标”，提示余额不足
系统数据:
user_assets=100
goods = [
{"name":"电脑","price":1999},
{"name":"鼠标","price":10},
{"name":"游艇","price":20},
{"name”:”喜茶”,”price":98},
]'''
goods = {"电脑":"1999","鼠标":"10","游艇":"20","喜茶":"98"}
user_assets = 100
print(goods)
input_goods = input("请输入你要购买的商品：")
while input_goods not in goods.keys():
    input_goods = input("请输入以上存在的商品：")
else:
    while int(goods[input_goods]) <= user_assets:
        print("购买成功")
        user_assets = user_assets - int(goods[input_goods])
        input_goods = input("请输入你要购买的商品：")
        while input_goods not in goods.keys():
            input_goods = input("请输入以上存在的商品：")
        continue
    else:
        print("余额不足")
