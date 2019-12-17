

import urllib.request

def load_baidu():
    url= "http://www.baidu.com"
    #添加请求头的信息


    #创建请求对象
    request = urllib.request.Request(url)
    #请求网络数据
    response = urllib.request.urlopen(request)
    print(response)
    data = response.read().decode("utf-8")

    #响应头
    # print(response.headers)
    #获取请求头的信息
    request_headers = request.headers
    print(request_headers)
    with open("02header.html","w")as f:
        f.write(data)



load_baidu()