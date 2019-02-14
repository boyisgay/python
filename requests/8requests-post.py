# get请求需要传递parmas
# post请求需要传递data

import requests

data = {
    'first': 'true',
    'pn': '1',
    'kd': 'C'
}
headers={
    'Referer': 'https://www.lagou.com/jobs/list_C?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3679.0 Safari/537.36'
}
response = requests.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false',data =data,headers=headers)
print(type(response.text))
print(response.text)
#response.json()可以把返回过来的json数据变成字典或者列表的格式

#