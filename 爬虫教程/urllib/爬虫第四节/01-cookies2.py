"""
    直接获取 个人中心的页面
    手动粘贴 复制 PC 抓包的 cookies
    放在  request对象的请求头里面 

"""

import urllib.request

# 1.数据url
url = 'https://www.yaozh.com/member/'
# 2.添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    ,
    'Cookie': '_ga=GA1.2.1820447474.1535025127; MEIQIA_EXTRA_TRACK_ID=199Tty9OyANCXtHaSobJs67FU7J; UtzD_f52b_ulastactivity=1511944816%7C0; WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; PHPSESSID=7jsc60esmb6krgthnj99dfq7r3; _gid=GA1.2.358950482.1540209934; _gat=1; MEIQIA_VISIT_ID=1BviNX3zYEKVS7bQVpTRHOTFV8M; yaozh_logintime=1540209949; yaozh_user=381740%09xiaomaoera12; yaozh_userId=381740; db_w_auth=368675%09xiaomaoera12; UtzD_f52b_saltkey=CfYyYFY2; UtzD_f52b_lastvisit=1540206351; UtzD_f52b_lastact=1540209951%09uc.php%09; UtzD_f52b_auth=2e13RFf%2F3R%2BNjohcx%2BuoLcVRx%2FhF0NvwUbslgSZX%2FOUMkCRRcgh5Ayg6RGnklcG3d2DkUFAXJxjhlIS8fPvr9rrwa%2FY; yaozh_uidhas=1; yaozh_mylogin=1540209953; MEIQIA_EXTRA_TRACK_ID=199Tty9OyANCXtHaSobJs67FU7J; WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1535025126%2C1535283389%2C1535283401%2C1539351081%2C1539512967%2C1540209934; MEIQIA_VISIT_ID=1BviNX3zYEKVS7bQVpTRHOTFV8M; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1540209958'
}

# 3.构建请求对象
request = urllib.request.Request(url, headers=headers)

# 4.发送请求对象
response = urllib.request.urlopen(request)

# 5.读取数据
data = response.read()
print(type(data))

# 保存到文件中 验证数据
with open('01cook.html', 'wb') as f:
    f.write(data)
