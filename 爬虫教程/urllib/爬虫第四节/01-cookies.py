import urllib.request

# 1.数据url
url = 'https://www.yaozh.com/member/'
# 2.添加请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}

# 3.构建请求对象
request = urllib.request.Request(url,headers=headers)

# 4.发送请求对象
response = urllib.request.urlopen(request)

# 5.读取数据
data = response.read()
print(type(data))

# 保存到文件中 验证数据
with open('01cook.html', 'wb') as f:
    f.write(data)