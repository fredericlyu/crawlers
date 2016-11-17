#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import traceback
import requests
import re

from argparse import ArgumentParser
from bs4 import BeautifulSoup

def _read(args):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,ja;q=0.2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }

    s = requests.Session()
    s.headers.update(headers)

    url = 'http://wufazhuce.com'

    if args.id == 0:
        soup = BeautifulSoup(s.get(url).text, 'lxml')
        link = soup.select('p.one-articulo-titulo a')[0]['href']
    elif -7 < args.id < 0:
        args.id = abs(args.id) - 1
        soup = BeautifulSoup(s.get(url).text, 'lxml')
        link = soup.select('div.fp-one-articulo ul li a')[args.id]['href']
    elif id > 0:
        link = 'http://wufazhuce.com/article/' + str(args.id)
    else:
        print('404 NOT FOUND.')
        return None

    if link:
        r = s.get(link)

        if r.status_code == 404:
            print('404 NOT FOUND.')
            return None

        soup = BeautifulSoup(r.text, 'lxml')
    else:
        return None

    title = soup.select('h2.articulo-titulo')[0].get_text(strip=True)
    author = soup.select('p.articulo-autor')[0].get_text(strip=True)
    article = soup.select('div.articulo-contenido')[0].get_text()

    print(link)
    print(title.encode('utf-8'))
    print(author.encode('utf-8'))
    print('')
    print(str.lstrip(article.encode('utf-8')))

def main():
    usage = '%(prog)s [<args>]'
    description = 'Extract articles from wufazhuce.com.'
    parser = ArgumentParser(usage = usage, description = description)

    parser.add_argument('id', type = int, nargs = '?', default = 0,
                        help = 'extract latest article if unspecified')

    _read(parser.parse_args())

if __name__ == '__main__':
    main()
