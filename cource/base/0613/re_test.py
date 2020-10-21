# Python里面match()和search()的区别？
#
# 答：re模块中match(pattern,string[,flags]),检查string的开头是否与pattern匹配。
#
# re模块中research(pattern,string[,flags]),在string搜索pattern的第一个匹配值。
#


import re
flag = 1
print(re.match('super', 'superstition'))
print(re.match('super', 'superstition').span())
print(re.match('super', 'superstitionsuper').group())
print(re.match('super', 'insuperable'))

print(re.search('super', 'superstition').span())


# 正则匹配
line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
print(line)
print(matchObj.group())
print(matchObj.group(0))
print(matchObj.group(1))
print(matchObj.group(2))