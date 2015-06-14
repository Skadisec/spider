import random

#from scrapy.contrib.downloadermiddleware import DownloaderMiddleware

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        #fd = open('/home/skadisec/ip.txt','r')
        #data = fd.readlines()
        #fd.close()
        #length = len(data)
        #index  = random.randint(0, length -1)
        #item   = data[index]
        #arr    = item.split(',')
        request.meta['proxy'] = 'http://211.138.60.24:80' 
        #% (arr[0],arr[1])