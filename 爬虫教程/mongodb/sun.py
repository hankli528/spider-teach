import requests
from bs4 import BeautifulSoup

url = 'http://wz.sun0769.com/index.php/question/reply?page=0'
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
data = requests.get(url, headers=headers).content

# with open('sun.html', 'wb') as f:
#     f.write(data)

soup = BeautifulSoup(data,'lxml')

result = soup.select('a[class=news14]')

print(len(result))