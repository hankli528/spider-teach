import requests
import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing import Pool


def download_music(songmid, music_name):
    url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=872989112&jsonpCallback=MusicJsonCallback06459212607938936&loginUin=11297258&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8¬ice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback06459212607938936&uin=11297258&songmid={0}&filename=C100{0}.m4a&guid=9136027940'.format(
        songmid)
    html = requests.get(url)
    # 去掉jsonp
    music_json = json.loads(re.findall(r'^\w+\((.*)\)$', html.text)[0])
    filename = music_json['data']['items'][0]['filename']
    vkey = music_json['data']['items'][0]['vkey']
    download_url = 'http://dl.stream.qqmusic.qq.com/{}?vkey={}&fromtag=66'.format(
        filename, vkey)
    print(download_url)
    # 下载到本地
    music = requests.get(download_url)
    # 文件名去除特殊符号
    with open("d:\\music\\{}.m4a".format(re.sub(r'[\s+|@<>:\\"/]', '', music_name)), "wb") as m:
        m.write(music.content)

def view_html():
    # qq音乐页面是js加载的，这里用chrome headless模式访问
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(
        r'D:\Program Files\Python\chromedriver.exe',
        chrome_options=option)

    # 排行榜页面
    driver.get('https://y.qq.com/n/yqq/toplist/26.html')
    print(driver.title)
    try:
        # 等待播放列表加载完毕
        WebDriverWait(
            driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "songlist__songname_txt")))

        lis = driver.find_elements_by_class_name('songlist__songname_txt')
        pattern = re.compile(r'https://y.qq.com/n/yqq/song/(\S+).html')
        for i in range(lis.__len__()):
            li = lis.__getitem__(i)
            a = li.find_element_by_class_name('js_song')
            # 获得songid
            href = a.get_attribute('href')
            music_name = a.get_attribute('title')
            m = pattern.match(href)
            download_music(m.group(1), music_name)

    finally:
        driver.quit()

if __name__ == '__main__':
    view_html()
