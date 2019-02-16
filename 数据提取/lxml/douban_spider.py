#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#豆瓣可以不用写headers
import requests
from lxml import etree
# 1 将目标网站页面抓取下来
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3679.0 Safari/537.36',
    'Referer': 'https://movie.douban.com/'
}
url = ' https://movie.douban.com/cinema/nowplaying/xinxiang/'
response = requests.get(url,headers=headers)
# print(response.text)
#text 返回的是经过解码后（有可能是乱码，所以用content）的字符串，是str（unicode）类型
#content 返回的是原生的字符串，就是从网页上抓取下来的 是bytes类型（自定解码方式）
text = response.text
# 2 将抓取下的数据根据一定规则提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul,encoding='utf-8').decode("utf-8"))
lis =ul.xpath(".//li")
move = []
for li in lis:
    try:
        # print(etree.tostring(li,encoding='utf-8').decode('utf-8'))
        title = li.xpath("@data-title")[0]
        time_release = li.xpath("@data-release")[0]
        time_duration = li.xpath("@data-duration")[0]
        actors = li.xpath("@data-actors")[0]
        thumbnail = li.xpath(".//img/@src")[0]

        bb={
             '标题':title,
             '上映时间':time_release,
             '时长':time_duration,
             '主演':actors,
             '专辑图片':thumbnail
           }
        move.append(bb)
    except(IndexError):
        pass
print(move)