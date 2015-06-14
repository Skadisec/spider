# Scrapy settings for sitemap project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import os
import random

BOT_NAME = 'sitemap hello,world~!'
BOT_VERSION = '2.0'

SPIDER_MODULES = ['sitemap.spiders']
NEWSPIDER_MODULE = 'sitemap.spiders'

#DOWNLOAD_DELAY = 6

ITEM_PIPELINES = [
    #'sitemap.pipelines.SitemapPipeline',
    'sitemap.mysql1.MySQLStorePipeline',
]
WEBKIT_DOWNLOADER=['spider']

DOWNLOADER_MIDDLEWARES={
   'mymiddleware.jswebkit.WebkitDownloader':543,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'mymiddleware.proxy.ProxyMiddleware': 100,
    #'myddleware.js.WebkitDownloader':543,
    #'mymiddleware.jswebkit.WebkitDownloader':1,
    'mymiddleware.useragent.RandomUserAgentMiddleware': 400,
    #'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware':None,
    'mymiddleware.canonicalize_url.Canonicalize':112,
 }

import os
os.environ["DISPLAY"] = ":0"
