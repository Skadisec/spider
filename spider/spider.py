#!/usr/bin/env python
#-*-coding:utf-8-*-

import argparse
from scrapy.cmdline import execute
from sitemap.spiders.spider import SitemapSpider
import sys

__author__ = 'Skadisec'
__license__ = 'BSD'
__version__ = '2.0'
__email__ = 'skadisec@qq.com'

def get_args():
    parser = argparse.ArgumentParser(description=__doc__,
                                    formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-u', '--url', help="设置起始url如; -u http://www.shiep.edu.cn")
    #parser.add_argument('-l', '--login', help="用户名; -l admin")
    #parser.add_argument('-p', '--password', help="密码; -p password")
    parser.add_argument('-c', '--connections', default='30', help="并发请求数控制, default=30")
    parser.add_argument('-r', '--ratelimit', default='0', help="请求速率控制, default=0")
    #parser.add_argument('--basic', help="Use HTTP Basic Auth to login", action="store_true")
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    rate = args.ratelimit
    if rate not in [None, '0']:
        rate = str(60 / float(rate))
    try:
        execute(['scrapy', 'crawl', 'spider', 
                 '-a', 'url=%s' % args.url, 
                 '-s', 'CONCURRENT_REQUESTS=%s' % args.connections,
                 '-s', 'DOWNLOAD_DELAY=%s' % rate])
    except KeyboardInterrupt:
        sys.exit()

main()