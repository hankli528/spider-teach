# 抓取当当网书评
# http://product.dangdang.com/25340451.html

import json
import requests
from lxml import etree


for i in range(1,5):
    # url = 'http://product.dangdang.com/index.php?r=comment/list&productId=25340451&pageIndex=1'
    url = 'http://product.dangdang.com/index.php?r=comment/list&productId=25340451&categoryPath=01.07.07.04.00.00&mainProductId=25340451&mediumId=0&pageIndex={}'.format(i)

    header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
            }

    response = requests.get(url,
                            headers=header,
                            timeout=5
                            )

    # print(response.text)

    result = json.loads(response.text)
    #
    comment_html = result['data']['list']['html']
    #
    tree = etree.HTML(comment_html)
    #
    comments = tree.xpath('//div[@class="items_right"]')
    #
    for item in comments:
        comment_time = item.xpath('./div[contains(@class,"starline")]/span[1]/text()')[0]
        comment_content = item.xpath('./div[contains(@class,"describe_detail")]/span[1]//text()')[0]
        print(comment_time)
        print(comment_content)