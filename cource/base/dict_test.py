import json

a = {"k1":"value", "k2": "value2", "k3":"value3"}
b = {"k1":0, "k2":1, "k3": 2}

d = json.dumps(a)
print(type(d),d)

print(type(a))
str_a = str(a)
print(str_a, type(str_a))

json_a = json.loads(d)
print("i am here:",type(json_a))



print('a=',a)
print('b=',b)

print('a[k2]=',a['k2'])
print('b[k2]=',b['k2'])

a['k2'] = 'changed'
b['k2'] = 'changed'
print('a[k2]=',a['k2'])
print('b[k2]=',b['k2'])

del a["k2"]
print('a=',a)


a.pop("k3")
print('a=',a)

a.clear()
print('a',a)

del a
print('a',a)