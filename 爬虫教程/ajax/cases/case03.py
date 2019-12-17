# 抓取非小号的图表接口
# https://www.feixiaohao.com/currencies/raiden-network-token/

import requests
import json

header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

# url = 'https://api.feixiaohao.com/coinhisdata/raiden-network-token/1540252714000/1540339114000/'
url = 'https://dncapi.feixiaohao.com/api/coin/charts?code=raiden-network-token&type=d&webp=0'
response = requests.get(url,headers=header,timeout=5)

result = json.loads(response.text)

print(result)

print(result.keys())