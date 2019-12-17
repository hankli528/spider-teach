# 抓取华尔街见闻实时快讯
# https://wallstreetcn.com/live/global?from=navbar

import requests
import json

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

url = 'https://api-prod.wallstreetcn.com/apiv1/content/lives?channel=global-channel&client=pc&limit=20'
response = requests.get(url,
                        headers=header,
                        timeout=5
                        )

# print(json.loads(response.text))

data = json.loads(response.text)['data']

for item in data['items']:
    print(item['content_text'].strip())
