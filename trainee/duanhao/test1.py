'''

＃ 写一个python函数，入参是一个整型数组，返回一个从大到小排好序的数组，
例如入参［3,2,5,7,1,2,6,9］，返回［9,7,6,5,3,2,2,1］

'''

def sort_desc(list_param):
    list_param.sort(reverse=True)
    return list_param

print(sort_desc([3,2,5,7,1,2,6,9]))
