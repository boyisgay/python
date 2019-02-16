#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from lxml import etree

#打开网页，获取该页的所有视频detaile_url
#打开detaile_url
#标题，观看次数，下载地址，图片、
Bassurl = 'https://jp.pornhub.com'
url = 'https://jp.pornhub.com/video?o=ht'
# page_url = 'https://jp.pornhub.com/video?o=ht&page=2'

Heardes = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3679.0 Safari/537.36',
    'Referer': 'https://jp.pornhub.com/video?o=ht&cc=gb'
}

def get_detail_urls(page_url):

    response = requests.get(page_url,headers=Heardes)
    text = response.text
    html = etree.HTML(text)


    detail_urls = html.xpath("//div[@class='nf-videos']//ul//span[@class='title']/a/@href")
    detail_urls = map(lambda page_url:Bassurl+page_url,detail_urls)

    # imgs = html.xpath("//*[@id='v205237521']/div/div[1]/div[2]/a/img/@src")
    return detail_urls

def parse_detail_page(detail_url):
    # detail_url = 'https://jp.pornhub.com/view_video.php?viewkey=ph59c40fc2ec6a0'
    movie ={}
    response = requests.get(detail_url, headers=Heardes)
    text = response.content.decode('utf-8')
    html = etree.HTML(text)
    home = html.xpath("//div[@class='video-wrapper']")
    playnow = home[0]
    #第一个是当前界面（上半部分）

    title = playnow.xpath(".//h1/span/text()")
    movie['标题']=title
    actors = playnow.xpath(".//div[@class='pronstarsWrapper']/a/text()")
    movie['演员']= actors
    views = playnow.xpath("./div[5]/div[1]/div[1]/div[2]/div[4]/div[1]//text()")
    movie['观看次数']= views
    year = playnow.xpath("./div[5]/div[1]/div[1]/div[2]/div[7]/span/text()")
    movie['发布日期']= year
    # print(year)
    views = playnow.xpath("./div[5]/div[1]/div[1]/div[1]/div/div[1]/span/text()")
    movie['观看次数']= views
    # print(views)
    cent = playnow.xpath("./div[5]/div[1]/div[1]/div[1]/div/div[3]/span[1]/text()")
    # print(cent)
    movie['好评率']= cent

    return movie


def spider():
    base_url = "https://jp.pornhub.com/video?o=ht&page={}"
    movies = []
    for x in range(1,2):
        #一共有7页
        page_url = base_url.format(x)
        detail_urls = get_detail_urls(page_url)
        for detail_url in detail_urls:
            #遍历每一页中的电影详情url
            # movie = parse_detail_page(detail_url)
            movies.append(parse_detail_page(detail_url))
            # print(movies)

if __name__ == '__main__':
    spider()