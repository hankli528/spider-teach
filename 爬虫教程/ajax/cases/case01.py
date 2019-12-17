# 抓取北京市2018年积分落户公示名单
# 'http://www.bjrbj.gov.cn/integralpublic/settlePerson'

import csv
import json
import requests

fw = open('luohu1.csv', 'w')
writer = csv.writer(fw)
writer.writerow(['id','name','birthday','company','score'])

def get_publicity(page_number):
    url = 'http://www.bjrbj.gov.cn/integralpublic/settlePerson/settlePersonJson?sort=pxid&order=asc&limit=100&offset=0&name=&rows=100&page={}'.format(page_number*100)

    header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.get(url,headers=header,timeout=5)

    result = json.loads(response.text)

    for item in result['rows']:
        id = item['pxid']
        name = item['name']
        birthday = item['csrq']
        company = item['unit']
        score = item['score']
        print(id,name,birthday,company,score)
        writer.writerow([id, name, birthday, company, score])

def main():
    for i in range(0,61):
        get_publicity(i)

if __name__ == '__main__':
    main()