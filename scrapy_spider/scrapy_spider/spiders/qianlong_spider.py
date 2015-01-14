__author__ = 'wangjz'

import scrapy
from django.utils import timezone
from scrapy_spider.items import ScrapySpiderItem

class QianlongSpider(scrapy.Spider):
    name = "qianlong"
    allowed_domains = ["py.qianlong.com"]
    start_urls = ["http://py.qianlong.com/3825/more/54768/more54768@2014-12-11.htm"]

    def parse(self, response):
        ssitem = ScrapySpiderItem()
        ssitem['url'] = "Charles"
        ssitem['content'] = "http://abc.com"
        ssitem['scrawl_date'] = timezone.now()
        ssitem.save()