# -*- coding: utf-8 -*-
__author__ = 'wangjz'

import scrapy
from django.utils import timezone
from django.utils.dateparse import parse_datetime

# from scrapy_spider.scrapy_spider.items import RumorBaikeSpiderItem
from scrapy_spider.items import RumorBaikeSpiderItem
import pytz

from spider.models import RumorBaike

class RumorBaikeSpider(scrapy.Spider):

    name = "rumorbaike"
    allowed_domains = ["liuyanbaike.com"]

    #http://www.liuyanbaike.com/article/29/
    base_url = "http://www.liuyanbaike.com/article/"
    rbi = RumorBaike.objects.order_by('-page_id')[0]
    start_no = rbi.page_id + 1
    print 'starting crawl page from %d' % start_no
    end_no = rbi.page_id + 31
    start_urls = [base_url + str(i) for i in range(start_no, end_no)]
    # start_urls = []

    def parse(self, response):
        if response.url.endswith(".com"):
            return

        rbsi = RumorBaikeSpiderItem()
        rbsi['url'] = response.url

        try:
            rbsi['page_id'] = int(response.url.split('/')[-2])
        except:
            print "No pid ,return"
            return

        try:
            rbsi['title'] = response.xpath('//h2[@class="rumor-title"]/text()').extract()[0]
        except:
            print "No title"

        try:
            rbsi['rumor_desc'] = response.xpath('//div[@class="rumor-desc"]/text()').extract()[0]
        except:
            print "No rumor_desc"

        try:
            rbsi['rumor_truth'] = response.xpath('//p[@class="rumor-truth"]/text()').extract()[1]
        except:
            print "No rumor_truth"

        try:
            rbsi['rumor_content'] = response.xpath('//div[@class="rumor-content"]').extract()[0]#带html标签的内容
        except:
            print "rumor_content"

        try:
            rbsi['tf_type'] = response.xpath('//div[@class="rumor-sum"]//strong[contains(@class,"icon")]/text()').extract()[0]
        except:
            print "tf_type"


        side_editor = response.xpath('//div[@class="side-editor"]')
        try:
            #<meta name="publishdate" content="2014-12-16 09:44:32">
            for p in side_editor.xpath('//p/text()').extract():
                if p.startswith(u'最后更新'):
                    t_str = p[5:]
                    naive = parse_datetime(t_str)
                    rbsi['update_date'] = pytz.timezone('Asia/Shanghai').localize(naive, is_dst=None)
                    break
        except:
            print "No publish date info"

        try:
            category_list = side_editor.xpath('//a[contains(@href,"category")]/text()').extract()
            rbsi['category'] = '\t'.join(category_list)
        except:
            print "No categories found"

        try:
            tag_list = side_editor.xpath('//a[contains(@href,"tag")]/text()').extract()
            rbsi['tag'] = '\t'.join(tag_list)
        except:
            print "No tags found"

        rbsi["scrawl_date"] = timezone.now()
        rbsi["status"] = int(response.status)
        rbsi.save()