#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from bs4.element import Tag
from bs4.element import NavigableString
from bs4.element import Comment

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
		    			
		    			
		    			
		    		</td>
		    	</tr>
		    </tbody></table>
<div>
我是div文本
</div>		    
<p><!--我是注释1--></p>    

<p1>
<!--我是多行注释-->
</p1>   		    
		    
"""

soup =BeautifulSoup(html,'lxml')
tbody = soup.find('table')
B = tbody.find
print(type(B))
for A in tbody:
    print(A)
print(type(tbody.children))



#BeautifulSoup将Html解析成树，树内包括四种对象
# 1 Tag是所有标签的对象/类型
# 2  BeautifulSoup是soup的对象
#    BeautifulSoup类继承自Tag
# 3 NavigableString是div的文本（我是div文本）的对象
#  （字符串str）
# 4 Comment是注释字符串的对象 继承自NavigableString
#   一行时如98行  可以直接用p.string获取
#    但是当多行时如100-102行，需要用p.contents
#---------------------------------------------------------------------
# contentsh和children 返回某个标签下的直接子元素。
# 区别是
# div.contents 返回的是一个list
# div.children 返回的是一个iterator（迭代器）
# 都可以进行遍历
#