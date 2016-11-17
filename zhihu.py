#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup

def main():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,ja;q=0.2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }

    s = requests.Session()
    s.headers.update(headers)

    url = 'http://www.zhihu.com/explore'

    soup = BeautifulSoup(s.get(url).text, 'lxml')
    result = soup.select('div.zh-summary.summary.clearfix')
    head = soup.select('div.explore-feed.feed-item h2')
    link = soup.select('div h2 a')
    dontwant = soup.select('div a.toggle-expand')
    for i in range(len(head)):
        print(head[i].get_text(strip=True).encode('utf-8'))
        print("http://www.zhihu.com"+link[i+5].get('href'))
        print('')
        dontwant[i].string = " "
        print(result[i+1].get_text(strip=True).encode('utf-8'))
        print('')

if __name__ == '__main__':
    main()
