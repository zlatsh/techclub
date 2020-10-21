#有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中
import os

def test(filePath):
    if not os.path.isfile(filePath):
        raise ValueError('错误：', filePath, '文件格式有误')
    content = ''
    with open(filePath) as fA:
        for line in fA.readlines():
            # content.replace('\n', '')
            # content.replace('\t', '')
            # content.replace('\f', '')
            # content.replace('\r', '')
            # content.replace('\v', '')
            # content.replace(' ', '')
            content += line
        if content == '':
            raise NameError("文件无内容")
        print('文件', filePath, '中的内容是：', content)
    return content


if __name__ == '__main__':
    fileA = './temp/a.txt'
    fileB = './temp/b.txt'
    fileC = './temp/c.txt'
    strC = ''.join(sorted(test(fileA) + test(fileB)))
    strLast = strC.replace(' ','')
    print("合并后的新内容：",strLast)
    #内容合并写入新文件中
    file=open(fileC,'w+')
    file.write(strLast)
    file.close()
