import requests
from bs4 import BeautifulSoup
from pyecharts import Bar
#Bar柱状图

ALL_DATA = []

def parse_page(url):
    headers={
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 73.0.3679.0Safari / 537.36'
    }
    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text,'lxml')

    if   url == 'http://www.weather.com.cn/textFC/gat.shtml':
        soup = BeautifulSoup(text, 'html5lib')

    conMidtab = soup.find('div',class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        #     print(table)
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all('td')
            if index ==0:
                city_td = tds[1]
            else:
                city_td = tds[0]
            city = list(city_td.stripped_strings)[0]
            #不加[0]打印的是list(因为前面有个list（）强制转换)
            # 加了之后是str
            temp_td = tds[-2]
            min_temp = int(list(temp_td.stripped_strings)[0])
            ALL_DATA.append({'city':city,'min_temp':min_temp})
            # print({'城市: '+city+'  '+'最低温: '+min_temp})

def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml',
    ]
    for url in urls:
        parse_page(url)


    #根据最低气温排序
    ALL_DATA.sort(key=lambda data:data['min_temp'])
    #sort()指定排序方法
    # print(ALL_DATA)
    data =ALL_DATA[:10]
    #绘图

    cities = list(map(lambda x:x['city'],data))
    temps =  list(map(lambda x:x['min_temp'],data))
    #map(func,iter1)
    #iter1中的一个或多个数依次经过func函数计算
    #并返回一个迭代器/map对象

    chart = Bar('中国天气')
    chart.add('',cities,temps)
    chart.render('temperature.html')

if __name__ == '__main__':
    main()
    # ALL_DATA = [
    #     {'city':'高雄' ,'min_temp':20},
    #     {'city':'台中' ,'min_temp':17}
    # ]
    # #根据最低气温排序
    #
    # ALL_DATA.sort(key=lambda data:data['min_temp'])
    # #sort()指定排序方法
    # print(ALL_DATA)
