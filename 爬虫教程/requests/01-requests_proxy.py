import requests

# 1.请求url
url = 'http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}

free_proxy = {'http': '27.17.45.90:43411'}

response = requests.get(url=url, headers=headers, proxies=free_proxy)

print(response.status_code)
