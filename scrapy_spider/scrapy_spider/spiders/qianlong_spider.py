# -*- coding: utf-8 -*-

__author__ = 'wangjz'

import scrapy
from django.utils import timezone
from scrapy_spider.items import ScrapySpiderItem
from spider.models import Gossip

from datetime import date, datetime, timedelta

#http://www.mengyaoren.com/tag/python-%E5%BE%AA%E7%8E%AF%E6%97%A5%E6%9C%9F-%E9%81%8D%E5%8E%86%E6%97%A5%E6%9C%9F-date-loop
def datespan(startDate, endDate, delta=timedelta(days=1)):
    currentDate = startDate
    while currentDate < endDate:
        yield currentDate
        currentDate += delta


class QianlongSpider(scrapy.Spider):
    name = "qianlong"
    allowed_domains = ["qianlong.com"]

    # root = "http://beijing.qianlong.com/3825/more/54777/more54777@"#权威辟谣
    chosen = 7

    seeds = [54777, 54771, 54768, 54766, 54772, 54780, 54778, 54779, 54790]
    types = [u"权威辟谣", u"工作动态", u"新闻聚焦", u"谣言公示", u"警方行动", u"照谣镜", u"求证", u"央广求证",u"专家视角"]

    root = "http://beijing.qianlong.com/3825/more/" + str(seeds[chosen]) + "/more" + str(seeds[chosen]) + "@"
    start_urls = [root + str(day) + ".htm" for day in datespan(date(2013, 8, 1), date(2015, 1, 16), delta=timedelta(days=1))]
    visited = [gos.url for gos in Gossip.objects.all()]

    def parse(self, response):
        if not response.url.endswith("htm"):
            return

        links = response.xpath('//div[@id="more"]//a')
        for index, link in enumerate(links):
            urls = link.xpath('@href').extract()
            titles = link.xpath('text()').extract()
            if len(urls) > 0 and len(titles) > 0:
                if urls[0] in self.visited:
                    print "[visited]", titles[0]
                    continue
                item = ScrapySpiderItem()
                item['url'] = urls[0]
                item['title'] = titles[0]
                item['category'] = self.types[self.chosen]
                item.save()
                self.visited.append(urls[0])

    """Model of a Gossip
    url = models.URLField(max_length=200, null=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    source = models.CharField(max_length=300)
    publish_date = models.DateTimeField('publishing date')
    scrawl_date = models.DateTimeField('scrawling date')
    status = models.IntegerField()
    """

