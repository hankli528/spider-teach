# 抓取金色财经快讯接口
# https://www.jinse.com/lives

import requests
import json

header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

url = 'https://api.jinse.com/v4/live/list?limit=20&reading=false&flag=up'
response = requests.get(url,headers=header,timeout=5)
result = json.loads(response.text)

# print(result)

# json格式分析工具：http://www.bejson.com/

for item in result['list'][0]['lives']:
    print(item)
    timestamp = item['created_at']
    content = item['content']
    print(timestamp)
    print(content)