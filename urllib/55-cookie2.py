#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 模拟登陆
# 杨幂人人网主页       http://www.renren.com/285104411/profile
# 人人网登陆           http://www.renren.com/PLogin.do
from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3679.0 Safari/537.36'
}

def get_opener() :
    # 1   登陆
    # 1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步创建的headler创建一个opener
    opener = request.build_opener(handler)
    return opener

def login_renren(opener) :
    # 1.4 使用opener发送登录请求
    data = {
        'email': '970138074@qq.com',
        'password': "pythonspider"
    }
    login_url = "  http://www.renren.com/PLogin.do"
    req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
    opener.open(req)

def visit_profile(opener) :
    # 2   访问个人主页
    yangmi_url = "http://www.renren.com/285104411/profile"
    # 获取个人主业的时候不要新建一个opener
    # 而应该是用之前的opener，因为之前那个opener已经包含了
    # 登陆所需要的cookie信息
    req = request.Request(yangmi_url, headers=headers)
    resp = opener.open(req)
    with open('renren.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))

if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)