'''

＃ 写一个python函数，入参是一个字典型(dictionary)，返回是否存在叫"hellokitty"的value，
例如:
入参{"country":"china","chairman":"xidada","toy":"hellokitty","provience":"shanxi"}，返回 True
入参{"key1":"value1","key2":"value2"} , 返回 False

'''

def exist_kity(dict_val):
    return 'hellokitty' in dict_val.values()

print(exist_kity({"country":"china","chairman":"xidada","toy":"hellokitty","provience":"shanxi"}))
print(exist_kity({"key1":"value1","key2":"value2"}))
