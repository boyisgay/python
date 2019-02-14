#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from urllib import request

#没有使用代理
# url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())

#使用代理
url = 'http://httpbin.org/ip'
#1 使用proxyheadler传入代理都建一个hander
hander = request.ProxyHandler({"http":"115.151.4.201:9999"})
#2 使用上面的header构建一个opener
opener = request.build_opener(hander)
#3 使用opener去发送一个请求
resp = opener.open(url)
print(resp.read())