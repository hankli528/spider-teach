import re
import requests

# 安装支持 解析html和XML的解析库 lxml
# pip install lxml
from lxml import etree

url = 'http://news.baidu.com/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

# response.text 不太准确 转码 是靠推测
data = requests.get(url, headers=headers).content.decode()


# 1.转解析类型
xpath_data = etree.HTML(data)


# xpath 语法 1. 节点 /
#            2. 跨节点: //
#            3. 精确的标签: //a[@属性="属性值"]
#            4. 标签包裹的内容 text()
#            5. 属性:@href
#              xpath--s数据类型---list
# 2调用 xpath的方法
result = xpath_data.xpath('/html/head/title//text()')
result = xpath_data.xpath('//a/text()')
result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=18"]/text()')
result = xpath_data.xpath('//a[@mon="ct=1&a=2&c=top&pn=18"]/@href')
result = xpath_data.xpath('//li/a/text()')

print(result)

# with open('02news.html', 'w') as f:
#     f.write(data)
