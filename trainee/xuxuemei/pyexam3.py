

users  =  [
    {
        'name':'seven',
        'password': '123'
    },
    {
        'name':'alex',
        'password': '123'
    }
]

def pyexam3():
    for i in range(3):
        sumJ = login()
        if sumJ == 1:
            break
        elif i == 2 and sumJ == 0:
            print("已锁定！")

def  login():
    name = input("please input your name: ")
    print(name)
    password = input("please input your password: ")
    print(password)
    value = 0
    for i in  range(len(users)):
        # print(users[i]["name"],users[i]["password"])
        if name==users[i]["name"] and password==users[i]["password"]:
            print("登录成功！")
            value = 1

    if value == 1:
         return value
    else:
        print("用户名或密码不正确！")
        return value

pyexam3()