# 抓取简书博客总阅读量
# https://www.jianshu.com/u/130f76596b02

import requests
import json
import re
from lxml import etree

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}


def get_all_article_links():
    links_list = []
    for i in range(1, 22):
        url = 'https://www.jianshu.com/u/130f76596b02?order_by=shared_at&page={}'.format(
            i)
        response = requests.get(url,
                                headers=header,
                                timeout=5
                                )
        tree = etree.HTML(response.text)
        article_links = tree.xpath(
            '//div[@class="content"]/a[@class="title"]/@href')
        for item in article_links:
            article_link = 'https://www.jianshu.com' + item
            links_list.append(article_link)
    return links_list


def get_read_num():
    num_list = []
    links_list = get_all_article_links()
    for url in set(links_list):
        response = requests.get(url,
                                headers=header,
                                timeout=5
                                )

        content = response.text
        read_num_pattern = re.compile(r'"views_count":\d+')
        read_num = int(read_num_pattern.findall(content)[0].split(':')[-1])
        print(read_num)
        num_list.append(read_num)
    return num_list

# total_read = 0
# for num in get_read_num():
#     total_read += num
# read_num_list = get_read_num()
# print('总阅读量 =', sum(read_num_list))