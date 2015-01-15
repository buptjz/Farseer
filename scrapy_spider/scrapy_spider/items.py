# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.djangoitem import DjangoItem
from spider.models import Gossip

class ScrapySpiderItem(DjangoItem):
    django_model = Gossip
    # define the fields for your item here like:
    # name = scrapy.Field()
