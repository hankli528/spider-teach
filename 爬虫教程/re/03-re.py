import re


# 纯数字的正则 \d 0-9之间的一个数
pattern = re.compile('^\d+$')
one = '234'

# 匹配判断的方法
# match 方法 是否匹配成功 从头开始 匹配一次
result = pattern.match(one)


print(result.group())
