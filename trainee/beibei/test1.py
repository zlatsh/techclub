'''

＃ 写一个python函数，入参是一个整型数组，返回一个从大到小排好序的数组，
例如入参［3,2,5,7,1,2,6,9］，返回［9,7,6,5,3,2,2,1］

'''
listA =[3,2,5,7,1,2,6,9]
i = 0
while  i < 7:
    j = 0
    while j < 7 - i:
        while listA[j] < listA[j + 1]:
            (listA[j] , listA[j + 1]) = (listA[j+1] , listA[j])
        j = j + 1
    i = i + 1
print("listA",listA)





