


count = -1
while (count < 9):
    count += 1
    #count = count + 1
    if count == 2:
        continue

    print('The count is:', count)

    if count == 7:
        break

print("Good bye!")

for letter in 'Python':  # 第一个实例
    print('当前字母 :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前水果 :', fruit)

print("Good bye!")

dict_test = {"k1":"value1","k2":"value2","zl":"ttt"}
print(len(dict_test))

phone = 123
print("phone len ==",len(str(phone)))


for k,v in dict_test.items():
    print("k=", k)
    print("v=", v)
    if v == "ttt":
        print("warning")


