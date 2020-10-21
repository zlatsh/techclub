users = [{"name":"seven","password":123},{"name":"alex","password":321}]


def get_user():
    username = input("username:")
    password = input("passwprd:")
    flag = verify_user(username, password)
    if flag == 0:
        print('账户已被锁定，请更换账户')
        get_user()
    elif flag == 1:
        print('登陆成功')
    else:
        print('用户名或密码不正确')
        get_user()


def verify_user(username, password):
    for user in users:
        if user['name'] == username:
            if user.get('error_count', 0) >= 3:
                return 0
            else:
                if str(user['password']) == password:
                    return 1
                else:
                    user['error_count'] = user.get('error_count', 0) + 1
                    return 2
    return 2


get_user()
