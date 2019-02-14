#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
#
# 使用代理只需添加参数pr     111.177.175.153	9999oxies
proxy = {
    'http':'113.121.153.18:9999'
}
response = requests.get("http://www.httpbin.org/ip",proxies=proxy)

print(response.text)