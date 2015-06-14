# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html
import scrapy
from scrapy.item import Item, Field

class SitemapItem(Item):
    # define the fields for your item here like:
    # name = Field()
    url = Field()
    #status = Field()
    #keywords = Field()
    #description = Field()