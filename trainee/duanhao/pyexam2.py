def get_number(n):
    int_str = ''
    i = 0
    while i < n:
        int_str = '4{}'.format(int_str)
        i += 1
    return int(int_str)


def add(n):
    int_sum = get_number(n)
    if n > 1:
        int_sum += add(n-1)
    return int_sum


print("此程序将算出4+44+444+...(n)个4相加之后的结果，请输入n值：")

def get_input():
    input_val = input("n:")
    try:
        n = int(input_val)
        print(add(n))
    except:
        print('输入内容格式不正确')

while(True):
    get_input()
