# 通过搜索接口抓取etherscan上的合约地址
# https://etherscan.io/

import requests
import re

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

url = 'https://etherscan.io/searchHandler?term=eos'
response = requests.get(url,
                        headers=header,
                        timeout=5
                        )

# print(response.text)

print(type(response.text))

for item in eval(response.text):
    # print(item)
    result = re.findall(r'0x.*\t?', item)[0][:43]
    print(result)
