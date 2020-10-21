
'''
hehrelf
'''


# f = open('ifelse.py', "r")
# rl = f.readlines()
#
# print(type(f),type(rl))
#
# print(len(rl))
# print(rl)
# for l in rl:
#     print(l)
# f.close()

# fw = open("zhanglei.txt","w")
# fw.write("i am zhanglei\n")
# fw.close()

fw = open("zhanglei.txt","a", encoding="utf-8")
fw.write("i am zhanglei\n")
fw.close()

fw = open("zhanglei1.txt","a", encoding="gbk")
fw.write("i am zhanglei1\n")
fw.close()
