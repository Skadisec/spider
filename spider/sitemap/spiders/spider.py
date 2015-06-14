import scrapy
import sys
import getopt

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from sitemap.items import SitemapItem
from scrapy.contrib.linkextractors import LinkExtractor
from urlparse import urlparse, parse_qsl, urljoin, urlunparse, urlunsplit

import urllib
import simplejson
import exceptions
import pickle
import sys
import requests
import string


class SitemapSpider(CrawlSpider):
#class MySpider(Spider):
    name = 'spider'
    #allowed_domains = ['shiep.edu.cn']
    #start_urls = ['http://www.sina.com.cn/']
    def __init__(self, *args, **kwargs):
        super(SitemapSpider, self).__init__(*args, **kwargs)
        self.start_urls =  [kwargs.get('url')]
        hostname1 = urlparse(self.start_urls[0]).hostname
        hostname2 = hostname1[4:]
        self.allowed_domains = [hostname2]


    rules = (
        Rule(LinkExtractor(deny='bbs', )),
        #Rule(LinkExtractor(allow=(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])',)), callback='parse'),
    )

    def parse(self, response):
        #if response.meta['depth'] > 1000:
            #print 'Loop?'
        item = SitemapItem()
        x         = HtmlXPathSelector(response)
        raw_urls  = x.select("//a/@href").extract()
        urls      = []
        orig_url = response.url
        for url in raw_urls:
            #if 'routes' in url:
                if 'http' not in url:
                    hostname1 = response.url
                    #url =  'http://www.shiep.edu.cn' + url
                    url =  hostname1 + url
                 #   url =  start_urls + url
                urls.append(url)

        for url in urls:
            yield scrapy.Request(url,meta={'depth':10})

        item['url']  = response.url.encode('UTF-8')
        #item['status'] = response.status
        #arr_keywords        = x.select("//meta[@name='keywords']/@content").extract()
        #item['keywords']    = arr_keywords[0].encode('UTF-8')
        #arr_description     = x.select("//meta[@name='description']/@content").extract()
        #item['description'] = arr_description[0].encode('UTF-8')

        yield item
