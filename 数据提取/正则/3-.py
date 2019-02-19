#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re


#  \  转义符
# text = 'apple price is $299'
# ret = re.search('\$\d+',text)
# print(ret.group())
#
# print("\\n")
#
# text = r'\n'   # raw  原生
# # r后面的东西是什么就是什么 没有特殊含义
# print(text)
#
# text = '\n'
# ret = re.match('\\n',text)#   \  两个对一个
# print(ret.group())
#
# text = '\c'
# ret = re.match(r'\\c',text)#   用原生字符串r
# print(ret.group())

#____________分组_________________#
#加上（）用来分组
#group(n)  可以获取第n个分组 n从1开始
#group(n,m)获取第n个 第m个分组
#groups把所有分组都拿出来
# text = "apple's price is $99,orange's price is $10"
# ret = re.search('.*(\$\d+).*(\$\d+)',text)
# print(ret.group())

#——————————正则表达式中的函数————————————————————————#
# match  从第一位开始检索 不满足则失败

#search  从整体查找

#findall 返回list 找到所有满足条件的值
# text = "apple's price is $99,orange's price is $10"
# ret = re.findall('\$\d+',text)    # 返回list
# print(ret)
# print(ret[1])

#sub 替换字符串
# text = "apple's price is $99,orange's price is $10"
# ret = re.sub('\$\d+','\$0',text,1)
# # re.sub('正则表达式','要替换的值',替换的文本,替换的第几个（不写默认全部）)
# print(ret)

# 目标：把文字信息提取出来
# 方法：把标签替换为空
# html = """
#         <dd class="job_bt">
#         <h3 class="description">职位描述：</h3>
#         <div class="job-detail">
#         <p>职位描述：</p>
# <p>你要面对的工作内容：</p>
# <p>1、 负责开发、维护公司KA客户，分析客户需求，制订招聘解决方案，并按期完成业务指标；&nbsp;</p>
# <p>2、负责与客户签订服务合同及合同的实施执行；&nbsp;</p>
# <p>3、定期通过电话、面谈拜访客户，维护新老客户关系；&nbsp;</p>
# <p>4、收集有效行业信息，分析市场需求；&nbsp;</p>
# <p>&nbsp;</p>
# <p>我们对你的期望：&nbsp;&nbsp;</p>
# <p>1、3年以上销售工作经验，至少1年以上KA客户开发、维护经验，有招聘行业经验的优先；&nbsp;</p>
# <p>2、良好的人际交往、商务谈判和内部协调能力，注重团队协作；&nbsp;</p>
# <p>3、工作主动性强，有较强的执行能力及抗压能力；</p>
# <p>4、适应外出拜访工作，较强的沟通协调能力和应变能力，善于快速处理问题；</p>
# <p>5、特别热爱销售工作，富有激情，对互联网有强烈的兴趣；</p>
#         </div>
#     </dd>
# """
#
# ret = re.sub('<.+?>|&nbsp;','',html)
# print(ret)

#split  分割字符串   返回list
# text = 'hello%world ni hao'
# ret = re.split('[^a-zA-Z]',text)
# print(ret)
#
# text = 'hello world ni hao'
# ret = re.split('',text)
# print(ret)


#complie作用有两点：
# 1 可以先将正则编译进内存 减少系统重复开销
text = "hello world ni 20.50111asd"
r = re.compile('\d+\.?\d*')
ret = re.search(r,text)
print(ret.group())

#2  可以加注释
text = "hello world ni 20.50"
r = re.compile(r"""
    \d+ #小数点前面（+1或更多个）
    \.? #小数点（？0或1个）
    \d* #小数点后面（*0或更多个）
""",re.VERBOSE)
ret = re.search(r,text)
print(ret.group())

