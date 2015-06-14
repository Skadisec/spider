# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import re
from twisted.enterprise import adbapi
import datetime
import MySQLdb.cursors
import hashlib
 
class MySQLStorePipeline(object):
    """docstring for MySQLstor"""
    def __init__(self):
 
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            db = 'shiep3',
            user = 'root',
            passwd = 'toor',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = False
        )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        #query.addErrback(self.handle_error)

        return item
    def _conditional_insert(self, tx, item):
        #cur = conn,cursor()
        #if item.get('url'):
            hashurl =  re.sub (r'\d+', 'd+',item['url'])
            print hashurl
            a = hashurl 
            #print 'sha1 = %s' % (hashlib.sha1(a).hexdigest(),)
            sha1 =  hashlib.sha1(a).hexdigest()
            print sha1
            print item ['url']
            tx.execute('select hash_value from test where hash_value ="'+sha1+'" limit 1')
            #cursor = conn.cursor() 

            result = tx.fetchone()
            print result

            if not result :
                #raise DropItem['url']
                #print ("http_url already stored in db ")
                tx.execute("insert into test(http_url,time,hash_value) values ('%s','%s','%s')"%(item['url'],datetime.datetime.now(),sha1))
            else:
                #tx.execute("insert into test(http_url,time,hash_value) values ('%s','%s','%s')"%(item['url'],datetime.datetime.now(),sha1))
                raise DropItem['url']
                print ("http_url already stored in db ")
               # '"+sha1+', limit 1)
