
import urllib.request

def load_baidu():
    url= "https://www.baidu.com"
    header = {
        #浏览器的版本
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        # "haha":"hehe"
    }


    #创建请求对象
    request = urllib.request.Request(url)
    #动态的去添加head的信息
    request.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
    #请求网络数据(不在此处增加请求头信息因为此方法系统没有提供参数)
    response = urllib.request.urlopen(request)
    print(response)
    data = response.read().decode("utf-8")

    #获取到完整的url
    final_url = request.get_full_url()
    print(final_url)

    #响应头
    # print(response.headers)
    #获取请求头的信息(所有的头的信息)
    # request_headers = request.headers
    # print(request_headers)
    #(2)第二种方式打印headers的信息
    #注意点:首字母需要大写,其他字母都小写
    request_headers = request.get_header("User-agent")
    # print(request_headers)
    with open("02header.html","w")as f:
        f.write(data)



load_baidu()