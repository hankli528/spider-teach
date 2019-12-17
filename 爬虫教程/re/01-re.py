
import re

# 贪婪模式  从开头匹配到结尾 默认
# 非贪婪
one = 'mdfsdsfffdsn12345656n'
two = "a\d"
pattern = re.compile('a\b')
# pattern = re.compile('m(.*?)n')

result = pattern.findall(two)

print(result)
