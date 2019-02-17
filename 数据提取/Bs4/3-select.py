#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

# 使用css选择器时就用seclet方法，
# 但css能做的事有限，一般只用来选中标签
html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tbody><tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47594&amp;keywords=python&amp;tid=0&amp;lid=0">25927-游戏测试经理（上海）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>上海</td>
					<td>2019-02-17</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47589&amp;keywords=python&amp;tid=0&amp;lid=0">31504-运营开发工程师</a></td>
					<td>技术类</td>
					<td>5</td>
					<td>深圳</td>
					<td>2019-02-17</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47590&amp;keywords=python&amp;tid=0&amp;lid=0">31504-高级数据运维工程师（DBA）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-02-17</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47583&amp;keywords=python&amp;tid=0&amp;lid=0">29912-数据分析-运营开发</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-02-17</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47584&amp;keywords=python&amp;tid=0&amp;lid=0">29912-数据产品经理</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-17</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47585&amp;keywords=python&amp;tid=0&amp;lid=0">29912-增长算法岗</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-17</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47578&amp;keywords=python&amp;tid=0&amp;lid=0">29912-后台架构工程师</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-02-17</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47580&amp;keywords=python&amp;tid=0&amp;lid=0">29912-增长前端开发</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-02-17</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47581&amp;keywords=python&amp;tid=0&amp;lid=0">29912-增长安卓开发工程师</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-02-17</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47582&amp;keywords=python&amp;tid=0&amp;lid=0">29912-增长移动端开发iOS</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-02-17</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">541</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=10#a">2</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=20#a">3</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=30#a">4</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=40#a">5</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=50#a">6</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=60#a">7</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=70#a">...</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=540#a">55</a><a href="position.php?lid=&amp;tid=&amp;keywords=python&amp;start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    		</td>
		    	</tr>
		    </tbody></table>
"""

# 1. 获取所有tr标签
# 2. 获取第二个tr标签
# 3. 获取所有class等于even的tr标签
# 4. 获取所有id等于test，class也等于test的a标签
# 5. 获取所有a标签的href属性的值（职位详细信息的url）
# 6. 获取所有职位信息（纯文本）

soup = BeautifulSoup(html,'lxml')

# 1. 获取所 有tr标签
# trs = soup.select("tr")
# print(type(trs))
# #list类型
# for tr in trs:
#     print(type(tr))
#     #Tag数据类型
#     print('*'*30)

# 2. 获取第二个tr标签
# trs = soup.select("tr")[1]
# print(trs)

# 3. 获取所有class等于even的tr标签
# trs = soup.select("tr[class='even']")
#
# print(trs)

# 4. 获取所有id等于test，class也等于test的a标签
#css无法实现

# 5. 获取所有a标签的href属性的值（职位详细信息的url）
# alist = soup.select('a')
# for a in alist:
#     href = a['href']
#     print(href)
# #先遍历a标签 再在每个a标签下遍历href

# 6. 获取所有职位信息（纯文本）
trs = soup.select('tr')
aa = {}
for tr in trs[1:len(trs)-1]:
    infos = list(tr.stripped_strings)
   # tr.stripped_strings是一个生成器：generator
    aa['职位']=infos[0]
    aa['类别']=infos[1]
    aa['人数']=infos[2]
    aa['地点']=infos[3]
    aa['时间']=infos[4]
    print(aa)
