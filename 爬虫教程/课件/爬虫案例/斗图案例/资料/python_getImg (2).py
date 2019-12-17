#coding:utf-8
#!/usr/bin/python

# 内容的一个时间模块
import time
import urllib
import urllib2

# Xpath的模块
from lxml import etree

# etree 可以对html格式的字符串构建html结构

# 爬虫第一步：查看我们的要爬取的网站，分析爬虫得地址和头部信息

url = 'https://www.duitang.com/search/?kw=%E6%96%97%E5%9B%BE&type=feed'
# 标识我们请求时候的身份
header = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

# 爬虫第二步：发起请求
request = urllib2.Request(url, data=None, headers=header)

# 爬虫第三步：我们将请求响应的内容返回成为一个文件对象
opener = urllib2.urlopen(request)

# 爬虫第四步：查看返回的内容
content = opener.read()

# print content
# 爬虫第五步：筛选我们需要的数据
	# re
	# xpath
	# beautifulsoup

	#1.构建html结构
html = etree.HTML(content)
	# 进行匹配我们需要的数据
	# 该网页所有的图片的地址 img标签的src属性
		# // 代表递归匹配，匹配该结构当中的所有的指定标签
		# [@class=""] 标签的class属性
img_list = html.xpath("//img")


# 爬虫礼仪
	# 指在数据采集过程中，对请求的网站保持一种和平，非攻击的行为
# print img_list

for img in img_list:
	print(img.attrib["src"])


# 构建下载图片的地址和名称
	img_url = img.attrib["src"]
	name = img_url.rsplit("/", 1)[1]
	print(img_url)
	print(name)
	urllib.urlretrieve(url, name)
	time.sleep(1)	














