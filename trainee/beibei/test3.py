'''

# 读文件readme.txt,把其中出现的 changes和行号 输出到一个新的目录newdir中,新文件名:changs.txt
最后打印一共出现了几次changes
'''
import os
import sys
fo = open("readme.txt","r",encoding="utf-8")
print(os.system("mkdir newdir"))
file = open("newdir/changes.txt","w",encoding="utf-8")
list = fo.readlines()
line = 1
sum = 0
for a in list:
    if a.find("changes") >= 0:
        print(a)
        file.write(a)
        print(line)
        file.write(str(line)+"\n")
        b = a.count("changes")
        #print(b)
        sum = sum + b
    line +=1
print(sum)
file.write(str(sum))
file.close()







