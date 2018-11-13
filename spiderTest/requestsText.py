import requests
import re

data = {'name': 'germey', 'age': '22'}
r = requests.get('http://httpbin.org/get', params=data)
# print(type(r))
# print(r.status_code)
print(r.text)
# print(r.cookies)

# 网页的返回类型实际上是str类型，但是它很特殊，是JSON格式的。所以，如果想直接解析返回结果，
# 得到一个字典格式的话，可以直接调用json()方法
print(r.json())

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

r = requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
title = re.findall(pattern, r.text)
print(title)

