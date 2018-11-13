import re
import json
import requests
import time
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


def get_one_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print('成功')
            return response.text
        return None
    except RequestException:
        return None


def bs4_parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all(name='dd')
    for i in range(10):
        yield{'index': items[i].i.string,
                'title': items[i].find_all(name='p')[0].string.strip(),
              'actor': items[i].find_all(name='p')[1].string.strip(),
              'time': items[i].find_all(name='p')[2].string.strip()
        }


#  正则表达式匹配效率太低
# def parse_one_page(html):
#     pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>'
#                          '.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer*?>(.*?)</i>.*?'
#                          'fraction>(.*/)</i>.*?</dd>', re.S)
#
#     items = re.findall(pattern, html)
#     for item in items:
#         yield {
#             'index': item[0],
#             'image': item[1],
#             'title': item[2],
#             'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
#             'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
#             'score': item[5].strip() + item[6].strip()
#         }


def write_to_json(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False,) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in bs4_parse_one_page(html):
        write_to_json(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
