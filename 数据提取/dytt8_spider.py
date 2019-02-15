# -*- coding:utf-8 -*-

import requests
from lxml import etree

BASS_DOMAIN = 'https://www.dytt8.net'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3679.0 Safari/537.36'
}
def get_detail_urls(url):
    # url = "https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"

    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk')
    # print(response.content.decode('gbk'))
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")

    # def asd(url)
    #     return BASS_DOMAIN+url
    #
    # index = 0
    # for detail_url in detail_urls:
    #     detail_url = asd(detail_url)
    #     detail_urls[index] = detail_url
    #     index += 1
    #19-16行相当于第29行

    detail_urls = map(lambda url:BASS_DOMAIN+url,detail_urls)
    return detail_urls


def parse_detail_page(url):
    pass


def spiders():
    base_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    for x in range(1,8):
        url = base_url.format(x)
        movie = parse_detail_page(url)

if __name__ == '__main__':
    spiders()