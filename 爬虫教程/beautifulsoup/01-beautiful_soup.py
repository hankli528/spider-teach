# pip install beautifulsoup4

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 1.转类型
# 默认bs4会 调用你系统中lxml的解析库 警告提示
# 主动设置 bs4的解析库
soup = BeautifulSoup(html_doc, 'lxml')

# 2.格式化输出 补全
result = soup.prettify()

print(result)
