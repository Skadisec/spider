# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import re
from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
from sitemap.items import SitemapItem
import datetime
import MySQLdb
import MySQLdb.cursors
import socket
import select
import sys
import os
import errno
 
class MySQLStorePipeline(object):
    """docstring for MySQLstor"""
    def __init__(self):
 
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            db = 'hello',
            user = 'root',
            passwd = 'Ykswsjjd1!',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = False
        )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item
    def _conditional_insert(self, tx, item):
        #cur = conn,cursor()
        if item.get('url'):
            hashurl =  re.sub (r'\d+', 'd+',item['url'])
            print hashurl
            a = hashurl 
            #print 'sha1 = %s' % (hashlib.sha1(a).hexdigest(),)
            sha1 =  hashlib.sha1(a).hexdigest()
            print sha1
            print item ['url']
            tx.execute("select hash_value from test where hash_value ='sha1'")
            result = tx.fetchone()
            if result:
                #DropItem['url']
                tx.execute("insert into test(http_url,time,hash_value) values ('%s',NOW(),'%s')',(item['url'][i]),time,sha1)")
                #log.msg("http_url already stored in db",level=log.DEBUG)
                #print ("http_url already stored in db ")
            else:
                #tx.execute("insert into test(http_url,time,hash_value) values ('%s',NOW(),'%s')',(item['url'][i]),time,sha1)")
                DropItem['url']
                print ("http_url already stored in db ")

