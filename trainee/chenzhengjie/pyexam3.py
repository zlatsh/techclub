'''［pyexam3］：实现用户输入用户名和密码，当用户名为 seven 或 alex 且密码正确时，显示登陆成功，
否则提示“用户名或密码不正确”（登陆失败），失败时允许重复输入三次，3次出错后，提示“已锁定”（不允许再登录）'''
#users=[{"name":"seven","password":123},{"name":"alex","password":321}]
user_dic ={"seven":"123","alex":"321"}
# dic ={v:k for v,k in user_dic.items()}
for i in range(4):
    if i>2:
        print("已锁定")
    else:
        input_name = input("请输入用户名：")
        input_password = input("请输入密码：")
        if input_name in user_dic.keys()and input_password == user_dic[input_name]:
            print("恭喜您，登陆成功！")
            break
        else:
            print("用户名或密码不正确")
            i+=1