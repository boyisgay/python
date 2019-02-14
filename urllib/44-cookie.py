#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#杨幂人人网主页http://www.renren.com/285104411/profile
#人人网登陆http://www.renren.com/SysHome.do

from urllib import request


depeng_url = "https://user.qzone.qq.com/845905527/infocenter"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3679.0 Safari/537.36',
    "Cookie": "845905527_todaycount=104; 845905527_totalcount=61611; eas_sid=01v534a9k1e09305d8R31366q6; pgv_pvid=7844478539; tvfe_boss_uuid=d83c9488cc9edbeb; RK=/Y484ivMdV; ptcz=9d51175855d6a02755b4badb4b819b73ddf5d2418d15e21731f61d404cb31ad9; pgv_pvi=2565337088; ptui_loginuin=845905527; Loading=Yes; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=1; uin=o0845905527; skey=@48nw4XJQT; ptisp=cnc; p_uin=o0845905527; pt4_token=m9udlr6JywLH29kSDoSPdZAXl*OzyH6z6s6rCJeVDdA_; p_skey=VNUpnTCWHqVNvn7FIUXihXbKRETogi1sgFgoRLWBYC0_; qzmusicplayer=qzone_player_845905527_1549780133062; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; pgv_info=ssid=s3652329920"
}
req = request.Request(url=depeng_url,headers=headers)
resp = request.urlopen(req)
#print(resp.read().decode('utf-8'))
with open('QQZ.html','w',encoding='utf-8') as fp:
   #write函数必须写入一个str的数据类型
   #resp.read()读出来的是一个byte数据类型
   #bytes -> decode -> str
   #str -> edcode -> bytes
    fp.write(resp.read().decode('utf-8'))
