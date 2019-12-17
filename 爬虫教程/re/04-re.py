import re


# 范围运算 [123] [1-9]
one = '7893452'

pattern = re.compile('[1-9]')

result = pattern.findall(one)


print(result)
