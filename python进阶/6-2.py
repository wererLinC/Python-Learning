'''
    读写json文件来进行数据的操作的
'''

import requests

r = requests.get('http://httpbin.org/headers')
print(r.text)

# 读json 的数据

import json

json.load()   # 从文件进行解析
json.loads()  # 从字符串中进行解析

json.dumps()  # 把python 对象转化成json

# 我们把python 对象用json的格式写进去文件中
json.dump(data, f)  # 把data写进去f文件中去，这就很有意思的呀

# 相对应的读的时候参数也是一样的



