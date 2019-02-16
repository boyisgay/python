
#  一
# tr = soup.find_all('tr',limit=2)[0]
# #limit参数 最多获取多少个元素
# #find_all返回的是列表下表从0开始
# # 所以[1]表示第二个tr标签

#  二
# 获取所有id等于test，class也等于test的a标签
# trs = soup.find_all('a',class_='test',id='test')

#  三
# find 只会返回第一个符合条件的标签
# find_all 会返回所有符合条件的标签

#  四
#获取某个标签的属性（a标签的href属性）
#方法1： 通过下标
# href = a['href']
# print(href)
#方法2： 通过attrs属性
# href = a.attrs['herf']

#  五
# trs = soup.find_all('tr')[1:]
# #[1:]过滤掉第零个tr标签

#  六
# tr.string:获取tr标签下的子非标签字符串, 返回字符串
# tr.strings:获取tr标签下的子孙非标签字符串, 返回生成器
# tr.stripped_strings: 获取tr内的非标签类的非空白内容 , 返回生成器
# tr.get_text:获取tr标签下的子孙非标签字符串, 返回普通字符串
# a = list(tr.stripped_strings) :  加list 返回列表
