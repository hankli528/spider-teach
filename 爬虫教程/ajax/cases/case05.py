# 抓取36氪快讯
# https://36kr.com/newsflashes

import requests
import json

header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

url = 'https://36kr.com/api/newsflash?&per_page=20'
response = requests.get(url,headers=header,timeout=5)

# print(json.loads(response.text))
data = json.loads(response.text)['data']

items = data['items']

# print(items)

for item in items:
    # print(item)
    item_info = {}
    title = item['title']
    item_info['title'] = title
    description = item['description']
    item_info['content'] = description
    published_time = item['published_at']
    item_info['published_time'] = published_time
    print(item_info)