# #urlparse和urlsplit没有params

# from urllib import parse
#
# url = 'https://baike.baidu.com/item/%E6%9D%A8%E5%B9%82/149851?fr=aladdin#2'
#
# result = parse.urlparse(url)
# print(result)
#
# print('scheme:',result.scheme)
# print('netloc:',result.netloc)
# print('path=',result.path)
# print('params:',result.params)#urlsplit没有
# print('query:',result.query)
# print('fragment:',result.fragment)

from  urllib import request
from  urllib import parse

# url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
# aa = request.urlopen(url)
# print(aa.read().decode('utf-8'))
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
                  'x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3679.0 Safari/537.36',

    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
}
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}
req = request.Request(url,headers=headers,
                      data=parse.urlencode(data).encode('utf-8'),method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))