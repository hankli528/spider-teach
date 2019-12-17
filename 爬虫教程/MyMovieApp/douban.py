# -*- coding: utf-8 -*-
# version 3.7.1
# Author: muyi
# html  css   javascript
# python 基础语法
# 爬虫基本知识

import requests
import re
from bs4 import BeautifulSoup
# 读写excel文件
from openpyxl import Workbook
wb = Workbook()
filename = 'movies.xlsx'
ws1 = wb.active
ws1.title = "电影top250"
DOWNLOAD_URL = 'http://movie.douban.com/top250/'
def download_page(url):
    #获取url地址页面内容
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    # print(data)
    return data

def get_li(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    ol = soup.find('ol', class_='grid_view')
    #电影名称
    name = []
    # 评价人数
    star_con = []
    # 评分
    score = []
    # 短评
    info_list = []
    for i in ol.find_all('li'):
        detail = i.find('div', attrs={'class': 'hd'})
        # 电影名称
        movie_name = detail.find('span', attrs={'class': 'title'}).get_text()
        # 评分
        level_star = i.find('span', attrs={'class': 'rating_num'}).get_text()
        star = i.find('div', attrs={'class': 'star'})
        # 评价人数
        star_num = star.find(text=re.compile('评价'))
        star_num=str(star_num)[:-3]
        # 短评
        info = i.find('span', attrs={'class': 'inq'})
        #判断是否有短评
        if info:
            info_list.append(info.get_text())
        else:
            info_list.append('无')
        score.append(level_star)
        # 追加元素内容
        name.append(movie_name)
        star_con.append(star_num)
    # 获取下一页
    page = soup.find('span', attrs={'class': 'next'}).find('a')
    if page:
        return name, star_con, score, info_list, DOWNLOAD_URL + page['href']
    return name, star_con, score, info_list,None

def main():
    url = DOWNLOAD_URL
    name = []
    star_con = []
    score = []
    info = []

    while url:
        doc = download_page(url)
        movie, star, level_num, info_list, url = get_li(doc)
        name = name + movie
        star_con = star_con + star
        score = score + level_num
        info = info + info_list
    #     名称、评论数、分数、短评
    for (n, count, sc, comment) in zip(name, star_con, score, info):
        col_A = 'A{0}'.format((name.index(n) + 1))
        col_B = 'B{0}'.format((name.index(n) + 1))
        col_C = 'C{0}'.format((name.index(n) + 1))
        col_D = 'D{0}'.format((name.index(n) + 1))
        ws1[col_A] = n
        ws1[col_B] = count
        ws1[col_C] = sc
        ws1[col_D] = comment
    wb.save(filename=filename)
if __name__ == '__main__':
    main()