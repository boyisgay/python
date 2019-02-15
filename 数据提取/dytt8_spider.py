
import requests
from lxml import etree

BASS_DOMAIN = 'https://www.dytt8.net'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3679.0 Safari/537.36'
}
def get_detail_urls(url):
    # url = "https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
    response = requests.get(url, headers=HEADERS)
    text = response.text
    # print(response.content.decode('gbk'))
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")#是一个列表

    # def asd(url)
    #     return BASS_DOMAIN+url
    #
    # index = 0
    # for detail_url in detail_urls:
    #     detail_url = asd(detail_url)
    #     detail_urls[index] = detail_url
    #     index += 1
    #18-26行相当于第29行

    #map(一个函数，一个序列)
    # 把列表中的每个值依次经过前面的函数计算，再传出
    #lambda相当于出传入url，传出BASS_DOMAIN+url
    detail_urls = map(lambda url:BASS_DOMAIN+url,detail_urls)
    return detail_urls


def parse_detail_page(url):
    movie = {}
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    # print(html)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['标题']= title
    zoom = html.xpath("//div[@id='Zoom']")[0]
    img = zoom.xpath(".//img/@src")
    # //img[@src="???"]  是给定img下属性src的值
    # //img/@src  是获取img下属性src的值
    # @后加属性
    cover = img[0]#第一个值
    movie['图片']= cover
    screenshot = img[1]#第二个值
    movie['截图']= screenshot
    infos = zoom.xpath(".//text()")
    for index,info in enumerate(infos):
        if info.startswith("◎年　　代"):
            info = info.replace("◎年　　代","").strip()
            movie['年代'] = info
        elif info.startswith("◎类　　别"):
            info = info.replace("◎类　　别", "").strip()
            movie['类别'] = info
        elif info.startswith("◎产　　地"):
            info = info.replace("◎产　　地", "").strip()
            movie['产地'] = info
        elif info.startswith("◎豆瓣评分"):
            info = info.replace("◎豆瓣评分", "").strip()
            movie['豆瓣评分'] = info
        elif info.startswith("◎片　　长"):
            info = info.replace("◎片　　长", "").strip()
            movie['片长'] = info
        elif info.startswith("◎主　　演"):
            info = info.replace("◎主　　演", "").strip()
            actors = [info]
            for x in range(index+1,len(infos)):
                actor = infos[x].strip()
                if actor.startswith("◎"):
                    break
                actors.append(actor)
            movie['主演'] = actors
    download_url =zoom.xpath(".//p/a/@href")
    movie['磁力链接'] = download_url
    # print(movie)
    return movie


def spider():
    base_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    for x in range(1,2):
        #一共有7页
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            #遍历每一页中的电影详情url
            movie = parse_detail_page(detail_url)
            movies.append(movie)
        #     break
        # break
            print(movie)

if __name__ == '__main__':
    spider()



