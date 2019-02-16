#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from  lxml import etree
text = """ 

		    					    		</div>
		    		<div class="clr"></div>
		    	</div>
		    </form>
		    <table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tbody><tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47428&amp;keywords=python&amp;tid=0&amp;lid=0">30628-腾讯广告算法高级工程师（研发中心-深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47423&amp;keywords=python&amp;tid=0&amp;lid=0">TEG02-网络运维工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47411&amp;keywords=python&amp;tid=0&amp;lid=0">22989-腾讯云资深运营开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47396&amp;keywords=python&amp;tid=0&amp;lid=0">PCG11-后台开发工程师（北京）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47379&amp;keywords=python&amp;tid=0&amp;lid=0">22989-腾讯云serverless运营开发工程师（深圳总部）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47380&amp;keywords=python&amp;tid=0&amp;lid=0">22989-腾讯云serverless运营开发工程师（成都）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>成都</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47374&amp;keywords=python&amp;tid=0&amp;lid=0">18436-NLP算法研究员（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47359&amp;keywords=python&amp;tid=0&amp;lid=0">PCG17-QQ钱包后台开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47353&amp;keywords=python&amp;tid=0&amp;lid=0">23295-互娱游戏数据营销经理（深圳）</a></td>
					<td>市场类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47354&amp;keywords=python&amp;tid=0&amp;lid=0">30359-后台开发高级工程师（北京）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
"""


def parse_text():
    #解析HTML字符串文本时
    #直接使用HTML进行解析
    htmlElement = etree.HTML(text)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

def parse_TXfile():
    parser = etree.HTMLParser(encoding='utf-8')
    htmlElement = etree.parse("TX.html",parser = parser)
    print(etree.tostring(htmlElement,encoding='utf-8').decode('utf-8'))

def parse_lagoufile():
    #parse默认使用XML的解析器
    #使用parse进行解析HTML时，
    # 一般都要指定解析器为HTMLparser
    parser = etree.HTMLParser(encoding='utf-8')
    htmlElement = etree.parse("lagou.html",parser=parser)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
    #parse_text()
    #parse_lagoufile()
    parse_TXfile()

# 这步骤是用来把网页代码格式化，
# 以方便使用xpath进行有用的数据提取