'''

＃ 写一个python函数，入参是一个字典型(dictionary)，返回是否存在叫"hellokitty"的value，
例如:
入参{"country":"china","chairman":"xidada","toy":"hellokitty","provience":"shanxi"}，返回 True
入参{"key1":"value1","key2":"value2"} , 返回 False

'''
dictA = {"country":"china","chairman":"xidada","toy":"hellokitty","provience":"shanxi"}
if  'hellokitty'  in dictA.values():
    print("True")
else:
    print("False")



