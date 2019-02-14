#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
# responese = requests.get('https://www.baidu.com')
#获取cookie
# print(responese.cookies.get_dict)
# print(responese.cookies)
#get_dict ：以字典的方式放回cookie信息

#保存cookies  session共享cookie
#比如我先登录人人网，可以得到一个coookie，然后这个cookie保存在我创建的session中 ，在我访问大鹏的人人网主页时，我就可以调用我保存在session中的cookie。
url = 'http://www.renren.com'
data = {"email":"9701380749@qq.com",'password':"pythonspider"}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3679.0 Safari/537.36'
}
session = requests.session()

session.post(url,data=data,headers=headers)
response = session.get('http://www.renren.com/880151247/profile')
with open('renren.html','w',encoding='utf-8') as fp:
    fp.write(response.text)

#爬去SSL证书不被CA认证的网站的时候
# resp = requests.get('http://www.asdasdasd.com',verify=False)
#只需要在读取网页的时候添加verify=False参数即可