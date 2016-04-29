# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AppItem(scrapy.Item):
    # define the fields for your item here like:
    app_name = scrapy.Field()
    down_link = scrapy.Field()
    app_rank = scrapy.Field()
    pass
