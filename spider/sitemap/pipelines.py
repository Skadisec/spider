# Define your item pipelines here
# coding:utf-8
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import  urlparse
import re
import hashlib
#class SitemapPipeline(object):
    #def process_item(self, item, spider):
       # data_path = '/home/skadisec/output/sitemap_sina_data1.txt'
     #   fd = open(data_path, 'a')
       # line = str(item['status'])   +'      '+  str(item['url'])  + '\n'
        #+ '#$#' + str(item['keywords']) + '#$#' + str(item['description']) + '\n'
     #   fd.write(line)
    #    fd.close
     #   return item
class SitemapPipeline(object):
	def process_item(self, item, spider):
		#url = item['url']
		#def format(url):
		#	if urlparse.urlparse(url)[2] == '':
		#		url = url+'/'
		#		url_structure = urlparse.urlparse(url)
		#		netloc = url_structure[1]
		#		path = url_structure[2]
		#		query = url_structure[4]
		#		item = (netloc,tuple([len(i) for i in path.split('/')]),tuple(sorted([i.split('=')[0] for i in query.split('&')])))
		#def url_similar_control(url):
		#	'''
		#	url 相似性控制
		#	True url未重复
		#	False url重复
		#	'''
		#print item['url']
		hashurl =  re.sub (r'\d+', 'd+',item['url'])
		print hashurl
		a= hashurl
		print 'sha1 = %s' % (hashlib.sha1(a).hexdigest(),)
		sha1 =  hashlib.sha1(a).hexdigest()
		print sha1
		print item['url']
		data_path = '/home/skadisec/output/shiep3.txt'
		fd = open(data_path, 'a')
		line =   str(item['url'])  + '\n'
		#line = str(item['status'])   +'      '+  str(item['url'])  + '\n'
		fd.write(line)
		fd.close
		return item
   # '''
    #策略是构建一个三元组
    #第一项为url的netloc
    #第二项为path中每项的拆分长度
    #第三项为query的每个参数名称(参数按照字母顺序排序，避免由于顺序不同而导致的重复问题)
    
    #if urlparse.urlparse(url)[2] == '':
      #  url = url+'/'

    #url_structure = urlparse.urlparse(url)
    #netloc = url_structure[1]
    #path = url_structure[2]
    #query = url_structure[4]
    
    #temp = (netloc,tuple([len(i) for i in path.split('/')]),tuple(sorted([i.split('=')[0] for i in query.split('&')])))
    #print temp
    #return temp
   # '''