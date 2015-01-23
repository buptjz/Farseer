# -*- coding: utf-8 -*-

from django.http import HttpResponse
import Farseer
DEBUG = Farseer.settings.DEBUG
# Create your views here.

from scrapy.crawler import Crawler
from scrapy_spider.scrapy_spider.spiders.rumor_baike_spider import RumorBaikeSpider
from scrapy import log, project
from twisted.internet import reactor
from billiard import Process
from scrapy.utils.project import get_project_settings

#http://stackoverflow.com/questions/22116493/run-a-scrapy-spider-in-a-celery-task
#先后试用了多种方法，最终找到上述的方法，看起来可行
class UrlCrawlerScript(Process):
    def __init__(self, spider):
        Process.__init__(self)
        settings = get_project_settings()
        self.crawler = Crawler(settings)

        if not hasattr(project, 'crawler'):
            self.crawler.install()
            self.crawler.configure()
            self.crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        self.spider = spider

    def run(self):
        self.crawler.crawl(self.spider)
        self.crawler.start()
        reactor.run()

def run_spider(request):
    spider = RumorBaikeSpider(domain='liuyanbaike.com')
    crawler = UrlCrawlerScript(spider)
    crawler.start()
    crawler.join()
    return HttpResponse("<html>liuyanbaike runnining over.</html>")