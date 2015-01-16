# -*- coding: utf-8 -*-

__author__ = 'wangjz'

import scrapy
from django.utils import timezone
from django.utils.dateparse import parse_datetime

from scrapy_spider.items import ScrapySpiderItem
from spider.models import Gossip
from datetime import date, datetime, timedelta

#http://stackoverflow.com/questions/25939719/django-ver-1-7-appregistrynotready-models-arent-loaded-yet
import django
django.setup()

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
    chosen = 8

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

import pytz
class QianlongItemSpider(scrapy.Spider):
    name = "qianlongitem"
    allowed_domains = ["qianlong.com"]

    start_urls = [gos.url for gos in Gossip.objects.all()]

    def parse(self, response):
        if not response.url.endswith("htm"):
            return

        gos = Gossip.objects.get(url=response.url)

        try:
            gos.keywords = response.xpath('//meta[@name="keywords"]/@content').extract()[0]
        except:
            print "No keywords"

        try:
            #<meta name="publishdate" content="2014-12-16 09:44:32">
            t_str = response.xpath('//meta[@name="publishdate"]/@content').extract()[0]
            naive = parse_datetime(t_str)
            gos.publish_date = pytz.timezone('Asia/Shanghai').localize(naive, is_dst=None)
        except:
            print "No publish date info"

        try:
            gos.source_url = response.xpath('//span[@id="source"]//a/@href').extract()[0]
        except :
            print "No source url"

        try:
            gos.source = response.xpath('//span[@id="source"]//a/text()').extract()[0]
        except:
            print "No source"

        gos.scrawl_date = timezone.now()
        gos.status = int(response.status)

        gos.content = response.xpath('//div[@id="content"]').extract()[0]

        gos.save()