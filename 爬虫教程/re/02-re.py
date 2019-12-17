import re

# . 除了 换行符号\n 之外的 匹配
one = """
    msfdsdffdsdfsn
    1234567778888N
"""

pattern = re.compile('m(.*)n', re.S | re.I)
result = pattern.findall(one)
print(result)
