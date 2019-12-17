# pip install beautifulsoup4

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story"><!--...--></p>
<p class="title"><b>The Dormouse's story</b></p>


<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>


"""

# 1.转类型 bs4.BeautifulSoup'
soup = BeautifulSoup(html_doc, 'lxml')
# print(type(soup))

# 2. 解析数据

# Tag 标签对象 bs4.element.Tag'
result = soup.head

# 注释的内容  类型 'bs4.element.Comment'
result = soup.p.string
print(type(result))

result = soup.a


# 内容 Navigablestring  'bs4.element.NavigableString
result = soup.a.string

# 属性
result = soup.a['href']






