#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("TX.html",parser =parser)

# 1 获取所有的tr标签  //tr
# trs = html.xpath("//tr")
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 2 获取第二个tr标签
# tr = html.xpath("//tr[2]")[0]
# print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 3 获取所有class等于even的tr标签
# trs = html.xpath("//tr[@class='even']")
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 4 获取所有a标签的href属性的值（职位详细信息的url）
# aslit = html.xpath("//a/@href")
# for a in aslit:
#     print("http://hr.tencent.com/"+a)

# 5 获取所有职位信息（纯文本）
trs = html.xpath("//tr[position()>1]")#获取大于1的tr标签
positions = []#列表数据类型

for tr in trs:
    try:
        href = html.xpath("//tr[position()>1]//td/a/@href")[0]
        # 加[0]是为了把列表变成字符串（雾）
        # 防止出现错误 ：（must be str, not list）
        # 或者这样提取href属性：
        # href = tr.xpath(".//a/@href")[0]
        #在当前（.//）标签（tr）下获取a标签
        fullurl = 'http://hr.tencent.com/' + href
        title = tr.xpath("./td[1]//text()")[0]
        #这里text()用来获取网页代码某个标签下的文本
        #或者这样获取
        #title = tr.xpath(".//a/text()")[0]
        category = tr.xpath("./td[2]/text()")[0]
        nums = tr.xpath("./td[3]/text()")[0]
        address = tr.xpath("./td[4]/text()")[0]
        pubtime = tr.xpath("./td[5]/text()")[0]

        position = {
            '网址':fullurl,
            '标题':title,
            '类型':category,
            '人数':nums,
            '地点':address,
            '时间':pubtime
        }
        positions.append(position)
    except(IndexError):
        pass
print(positions)

