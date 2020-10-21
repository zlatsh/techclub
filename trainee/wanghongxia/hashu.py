
#dictN ={"country":"china","chairman":"xidada","toy":"hellokitty","provience":"shanxi"}
#print(dictN.get('to1y'))
#dictN.get(toy,default=None)??
   # print("True")
#exit()
dict ={"country":"china","chairman":"xidada","toy":"hellokitty","provience":"shanxi"}  # type: Dict[str, str]

if  'toy' in dict:
    print("hellokitty")
else :
    print(False)

if "toy" in dict:
    print("hellokitty")