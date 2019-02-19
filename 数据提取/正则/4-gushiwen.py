#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import re,requests

def parse_page(url):
    headers = {
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 73.0.3679.0 Safari/537.36'
    }
    reponse = requests.get(url,headers=headers)
    text = reponse.text
#—————————————————————————注意贪婪非贪婪模式!!——————————————————————#
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    #re.DOTALL代表  .   匹配所有的字符 包括换行符 因为html中有换行符干扰
    # print(titles)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text)
    # authors = re.findall(r'<p class="source">.*?<a.*>(.*?)</a>',text)
    authors = re.findall(r'<p class="source">.*?<a.*?>.*<a.*>(.*)</a>',text)
    content_tags =re.findall(r'<div class="contson" .*?>(.*?)</div>',text,re.DOTALL)
    contents = []
    for content in content_tags:
        # print(contents)
        x = re.sub(r'.*?',"",content)
        x = re.sub(r'<br />',"",x)
        contents.append(x.strip())

#zip()函数的用法
# a= [1,2]
# b= [3,4]
# c = zip(a,b)
# c=[
#     (1,3),
#     (2,4)
# ]


# 有a=(1,2,3,4)
# 若A,B,C,D=a
# 则A=1;B=2;C=3;D=4
    pomes = []
    for value in zip(titles,dynasties,authors,contents):
        title,dynastie,author,content = value
        # print(value)
        pome = {
            'title':title,
            'dynasty':dynastie,
            'author':author,
            'concent':content
        }
        pomes.append(pome)

    # # return pomes
    for pome in pomes:
        print(pome)
        print('*'*30)
    # print(pomes[-1])

def main():
    pomes=[]
    for x in range(1,11):
        # 一共有7页
        url = 'https://www.gushiwen.org/default_%s.aspx' % x
        parse_page(url)
        # pomes = parse_page(url)
        # print(pomes)


if __name__ == '__main__':
    main()