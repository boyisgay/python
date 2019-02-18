#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re

#验证手机号
#一共11位，开头是1 第二位一般是3|4|5|7|8
text = "15249701578"
ret = re.match('1[34578]\d{9}',text)
print(ret.group())

#验证邮箱
#前面是数字|字符|下划线 中间是@ 后面公司域名是 数字字母下划线
# 最后是字母
text = "84590wudi@qq.com"
ret = re.match('\w+@[a-z0-9]+\.[a-z]+',text)
#   \.   用转义符将匹配规则 .  转译成字符  .
print(ret.group())

#验证url‘
#开头是http|https|ftp 中间是  ：\\  后面十多个非空字符
text = "http://www.baidu.com/item/Python/412312?fr=asdf"
ret = re.match('(http|https|ftp)://[^\s]+',text)
print(ret.group())

#验证身份证
# 18位 前17位是数字 后一位是数字|x|X
text = "41072519970810663X"
ret = re.match('\d{17}[\dxX]',text)
print(ret.group())