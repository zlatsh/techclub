# ［pyexam3］：实现用户输入用户名和密码，当用户名为 seven 或 alex 且密码正确时，显示登陆成功，否则提示“用户名或密码不正确”（登陆失败），
# 失败时允许重复输入三次，3次出错后，提示“已锁定”（不允许再登录）
# 系统数据：
# users  =  [{“name”:”seven”,”password”:123},{”name”:”alex”,”password”:321}]
count = 1
while count <= 3:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if (username == 'seven' and password == '123') or (username == 'alex'and password == '321'):
        print("登录成功！")
        break
    else:
        print("用户名或密码不正确")
        count = count + 1
else:
    print("3次输入错误，账号已锁定")
