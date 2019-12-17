import requests
from bs4 import BeautifulSoup
from lxml import etree
import json

class BtcSpider(object):
    def __init__(self):
        self.url = 'http://8btc.com/forum-61-{}.html'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

        # 保存列表页的数据
        self.data_list = []

        self.data_detail = []

    # 1.发请求
    def get_response(self, url):
        response = requests.get(url, headers=self.headers)
        data = response.content
        return data

    # 2.解析数据list
    def parse_list_data(self, data):

        # 1.转类型
        soup = BeautifulSoup(data, 'lxml')
        # 2.解析内容 取出 所有的类选择器的 A
        title_list = soup.select('.xst')
        for title in title_list:
            list_dict_data = {}
            list_dict_data['title'] = title.get_text()
            list_dict_data['detail_url'] = title.get('href')
            self.data_list.append(list_dict_data)

    # 3.解析数据详情页
    def parse_detail_data(self, data):
        html_data = BeautifulSoup(data, 'lxml')

        # 取出问题--list[1][0]
        question = html_data.select('#thread_subject')[0].get_text()
        print(question)
        answer_list = html_data.select('.t_f')
        for answer in answer_list:
            answer_list = []
            answer_list.append(answer.get_text())

        detail_data = {
            "question": question,
            "answer": answer_list
        }

        self.data_detail.append(detail_data)

    # 3.保存数据
    def save_data(self, data, file_path):
        data_str = json.dumps(data)
        with open(file_path, 'w') as f:
            f.write(data_str)

    def start(self):
        # 列表页的请求
        for i in range(1, 2):
            url = self.url.format(1)
            data = self.get_response(url)
            self.parse_list_data(data)
        self.save_data(self.data_list, "04list.json")

        # 发送详情页的请求
        for data in self.data_list:
            detail_url = data['detail_url']
            detail_data = self.get_response(detail_url)

            # 解析详情页的数据
            self.parse_detail_data(detail_data)

        self.save_data(self.data_detail, 'detail.json')


BtcSpider().start()

"""
html_data = etree.HTML(data)

        result_list = html_data.xpath('//div[contains(@id,"stickthread")]')
        result_list = html_data.xpath('//head/following-sibling::*[1]')
        print(len(result_list))
        print(result_list)
"""
