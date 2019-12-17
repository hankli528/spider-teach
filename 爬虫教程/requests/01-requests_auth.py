import requests

# 发送post请求
data = {

}
response = requests.post(url, data=data)


# 内网 需要 认证
auth = (user,pwd)
response = requests.get(url,auth=auth)