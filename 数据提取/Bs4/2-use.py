
from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
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
		    		<td colspan="5"></title>
</head>
<body>

</body>
</html>


"""

soup = BeautifulSoup(html,'lxml')

# 1. 获取所有tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)
#     print('='*30)
#     print(type(tr))
#     break

# 2. 获取第二个tr标签
# tr = soup.find_all('tr',limit=2)[0]
# #limit参数 最多获取多少个元素
# #find_all返回的是列表下表从0开始
# # 所以[1]表示第二个tr标签
# print(tr)


# 3. 获取所有class等于even的tr标签
# trs = soup.find_all('tr',class_='even')
# #python中class是一个关键字
# #所以bs4中的标签class用class_表示
# #在soup中搜索所有的  tr标签且class等于even
# for tr in trs:
#     print(tr)
#     print('+'*30)
# #第二种过滤方法
# # trs = soup.find_all('tr',attrs={'class':even})

# 4. 获取所有id等于test，class也等于test的a标签
# trs = soup.find_all('a',class_='test',id='test')
# # 或者
# # trs = soup.find_all('a',attrs={'class':'test','id':'test'})
# for a in trs:
#     print(a)

# 5. 获取所有a标签的href属性的值（职位详细信息的url）
# alist = soup.find_all('a')
# for a in alist:
#     #获取属性
#     #通过下标
#     href = a['href']
#     print(href)
#     #或者attrs属性
#     # href = a.attrs['herf']
#     # print(href)
# 6. 获取所有职位信息（纯文本）

trs = soup.find_all('tr')[1:]
#[1:]过滤掉第零个tr标签
movies=[]
for tr in trs:
    # try:
    #     tds = tr.find_all("td")
    #     title = tds[0].string
    #     #加上  .string表示只要tds[0]里面的字符串
    #     # print(title)
    #     sort = tds[1].string
    #     # print(sort)
    #     nums = tds[2].string
    #     adder = tds[3].string
    #     data = tds[4].string
    #     info = {
    #         '职位':title,
    #         '类别':sort,
    #         '所需人数':nums,
    #         '地点':adder,
    #         '发布时间':data,
    #     }
    # except IndexError:
    #     pass
    # print(info)

    #第二种方法
    movie={}
    try:
        infos = list(tr.stripped_strings)
        #tr.stripped_strings 获取tr内的非标签类的非空白内容
        #tr.strings 获取tr内的非标签内容
        movie['title']= infos[0]
        movie['categoy']= infos[1]
        movie['nums']= infos[2]
        movie['city']= infos[3]
        movie['pubtim']= infos[4]
        movies.append(movie)
    except IndexError:
        pass
print(movies)



