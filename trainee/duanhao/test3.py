'''

# 读文件readme.txt,把其中出现的 changes和行号 输出到一个新的目录newdir中,新文件名:changs.txt
最后打印一共出现了几次changes
'''
import os
import sys

f = open(os.path.join(sys.path[0], 'readme.txt'), 'r')
new_path = os.path.join(sys.path[0], 'newdir')
if not os.path.exists(new_path):
    os.makedirs(new_path)
new_file_path = os.path.join(new_path, 'changes.txt')
try:
    os.remove(new_file_path) # 先删除旧文件
except Exception as error:
    print('没有需要清空的文件')
other_file = open(new_file_path, 'a')

count = 0
for index, line in enumerate(f.readlines()):
    temps = line.split('changes')
    if len(temps) > 1:
        other_file.write('{}\t{}\n'.format(index+1, len(temps)-1))
        count += len(temps)-1
other_file.write('{}\t{}'.format('总计',count))

f.close()
other_file.close()
