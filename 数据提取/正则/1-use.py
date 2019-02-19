#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import re
#-------------------单字符匹配-----------------------#
# text = "asdfghjkl"
# ret = re.match('asdf',text)
# # match只会匹配前面的字符
# # asd可以  sd就不可以
# # 只能从开始的地方匹配

# # ret = re.search('sdf',text)
# # #search会从整个字符串查找
# print(ret.group())

#   .  可以匹配任意字符（除了换行符）
# text = "sdfghjkl"
# ret = re.match('.',text)
# print(ret.group())

# \d  匹配任意的数字
# text = "11222"
# ret = re.match('\d',text)
# print(ret.group())


# \D匹配任意非数字
# text = "*sdfghjkl"
# ret = re.match('\D',text)
# print(ret.group())

# \s 匹配空白字符（\n换行 \t制表 \r 空格）
# text = "a b"
# ret = re.match('\s',text)
# print(ret.group())

# \w 匹配a-z A-Z 数字 下划线

# \W 匹配的和\w相反 ~ ! @ # $ % ^ & * ( ) - + :等

# [] 组合方式 只要满足[] 内的字符就可以
# text = "0737-743aaa3169"
# ret = re.match('[\d\-]+',text)
#   +   匹配多个字符
# print(ret.group())


#这几种方式等效
# \d [0-9]
# \D ^0-9
# \w [0-9a-zA-Z_]
# \W [^0-9a-zA-Z_]

# ——————————————————————匹配多个字符————————————————————————————#
#

#    *  ：匹配任意多个字符（包括0个）
# text = "11222"
# ret = re.match('\d*',text)
# print(ret.group())

#   +  ：  匹配一个或多个字符
# text = "1Ad+f"
# ret = re.match('\w+',text)
# print(ret.group())

#   ?  :   匹配一个或者0个(英文问号)
# text = "a1222"
# ret = re.match('\d?',text)
# print(ret.group())

#  {m}   匹配m个字符
# text = "11222"
# ret = re.match('\d{2}',text)
# print(ret.group())
#  {m,n}   匹配m到n个字符


#--------------------第二节---------------------#
#  ^  脱字号 以什么开始
# 如果在中括号中 代表取反操作
text = 'asdf'
ret = re.search('^as',text)
print(ret.group())
#

#  $   以什么结尾
text = 'x12asx_x@163.com'
ret = re.match('\w+@163\.com$',text)
print(ret.group())

#  |    匹配多个字符串或者表达式 或
text = 'http://www.baidu.com'
ret = re.match('(http|https|ftp)',text)
print(ret.group())
#
# 贪婪模式（默认）
# 非贪婪模式(一般在  +  后面加个问号)
text = '12344'
ret = re.match('\d+?',text)
print(ret.group())

#贪婪模式
text = '<h1>标题<h1>'
ret = re.match('<.+>',text)
print(ret.group())

#——————————————案例——————————————————#
#匹配0-100之间的数字
text = '100'
ret = re.match('[1-9]\d?$|100$',text)
print(ret.group())