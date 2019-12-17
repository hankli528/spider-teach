import re

# 1.拆分字符串
one = 'asdsfsgsh'

# 标准 是 s 为拆分

pattern = re.compile('s')
result = pattern.split(one)
# print(result)

# 2.匹配中文
two = '<a href="https://www.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://www.baidu.com/s?ie=utf-8&amp;fr=bks0000&amp;wd=">网页是最新版本的,适配移动端</a>'

# python中 匹配中问 [a-z] unicode的范围 * + ?
pattern = re.compile('[\u4e00-\u9fa5]+')

result = pattern.findall(two)
print(result)