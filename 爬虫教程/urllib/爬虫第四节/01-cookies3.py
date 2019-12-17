"""
    获取 个人中心的页面
    
    1. 代码登录  登录成功 cookie(有效)
    2. 自动带着cookie 去请求个人中心
    
    
    cookiejar 自动保存这个cookie

"""
import urllib.request
from http import cookiejar
from urllib import parse

# 登录之前的 登录页的网址https://www.yaozh.com/login/
# 找登录 参数

# 后台 根据你发送的请求方式来判断的 如果你是get(登录页面),如果POST(登录结果)

# 1. 代码登录
# 1.1 登录的网址
login_url = 'https://www.yaozh.com/login'
# 1.2 登录的参数
login_form_data = {
    "username": "xiaomaoera12",
    "pwd": "lina081012",
    "formhash": "CE3ADF28C5",
    "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"

}
# 1.3 发送登录请求POST
cook_jar = cookiejar.CookieJar()
# 定义有添加  cook 功能的 处理器
cook_hanlder = urllib.request.HTTPCookieProcessor(cook_jar)
# 根据处理器 生成 opener
opener = urllib.request.build_opener(cook_hanlder)

# 带着参数 发送post请求
# 添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
# 1.参数 将来 需要转译 转码; 2. post请求的 data要求是bytes
login_str = parse.urlencode(login_form_data).encode('utf-8')

login_request = urllib.request.Request(login_url, headers=headers, data=login_str)
# 如果登录成功, cookjar自动保存cookie
opener.open(login_request)

# 2. 代码带着cooke去访问 个人中心
center_url = 'https://www.yaozh.com/member/'
center_request = urllib.request.Request(center_url, headers=headers)
response = opener.open(center_url)
# bytes -->str
data = response.read().decode()

with open('02cook.html', 'w') as f:
    f.write(data)


# 一个用户 在不同的地点(IP(福建,上海, 杭州, 河南)) 不同浏览器 上面 不停的登录  非人为操作
# 封你的账号
# N 个 账号
