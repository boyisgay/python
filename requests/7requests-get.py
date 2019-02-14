#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests

#调用第三方库requests可以直接获取网页源码
response = requests.get('https://www.baidu.com')
#get是请求方式 还有post等

#使用text有可能产生乱码（text是按照自己的猜测进行解码的）
# print(type(response.text))
# print(response.text)

#使用content产生bytes是经过编码的字符串，
# bytes可以直接存储在硬盘，也可以在网络上进行传输
# print(type(response.content))
# print(response.content.decode('utf-8'))
#加上decode('utf-8')将bytes按照utf-8的编码方式进行解码。

#将获取到的网页save在本地
# with open('111.html','w',encoding='utf-8') as fp:
#     fp.write(response.content.decode('utf-8'))

# print(response.url)#获取requests的url
# print(response.encoding)#编码方式 可以看出它认为编码方式是ISO-8859-1所以用text时产生了乱码
# print(response.status_code)#相应状态码

#利用第三方库requests传递参数
params = {
    # 'ie': 'utf-8',
    'wd': '中国'
}#这是一个字典类型
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3679.0 Safari/537.36'
}

response1 = requests.get('https://www.baidu.com/s',params=params,headers=headers)
#将获取到的网页save在本地
with open('baidu.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))#write函数必须写入一个str类型，所以要把content解码出来
print(response1.url)