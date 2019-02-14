from urllib import request
#request是网络请求相关
from urllib import parse
#parse是关于解码编码的库


# resp = request.urlopen('http://www.baidu.com')
# print(resp.read())

# url = 'http://www.baidu.com/s?'
params = {"wd":"杨幂"}#这是个字典类型
qs = parse.urlencode(params)
# url = url + qs
# resp = request.urlopen(url)
# #print(resp.read())

print(qs)
result = parse.parse_qs(qs)
print(result)

