# -*- coding: utf-8 -*-

from django.http import HttpResponse
import json
import Farseer
DEBUG = Farseer.settings.DEBUG
# Create your views here.

# from scrapy.crawler import Crawler
# from scrapy import log, project
# from twisted.internet import reactor
# from billiard import Process
# from scrapy.utils.project import get_project_settings
#
# #http://stackoverflow.com/questions/22116493/run-a-scrapy-spider-in-a-celery-task
# #先后试用了多种方法，最终找到上述的方法，看起来可行
# class UrlCrawlerScript(Process):
#     def __init__(self, spider):
#         Process.__init__(self)
#         settings = get_project_settings()
#         self.crawler = Crawler(settings)
#
#         if not hasattr(project, 'crawler'):
#             self.crawler.install()
#             self.crawler.configure()
#             self.crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
#         self.spider = spider
#
#     def run(self):
#         self.crawler.crawl(self.spider)
#         self.crawler.start()
#         reactor.run()
#
import urllib2
import json
from django.core import serializers
from models import RumorBaike
def post_dict(url, dict):
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(dict))
    return response

def receive_post(request):
    # return HttpResponse("<html>liuyanbaike runnining over.</html>")
    if request.method == 'POST':
        # print request.body
        json_data = json.loads(request.body)
        dic_list = json.loads(json_data)

        for liuyan_dic in dic_list:
            fields_dic = liuyan_dic[u'fields']
            print fields_dic
            rumor = RumorBaike(**fields_dic)
            rumor.save()
        return HttpResponse("OK")


def send_post(request):
    data = serializers.serialize("json", RumorBaike.objects.all()[:2])
    post_dict('http://127.0.0.1:8000/spider/receive', data)
    return HttpResponse("<html>Send success.</html>")

def update_item(request):
    response_data = {}
    response_data['result'] = 'failed'
    response_data['message'] = 'You messed up'

def run_spider(request):
    pass
    # spider = RumorBaikeSpider(domain='liuyanbaike.com')
    # crawler = UrlCrawlerScript(spider)
    # crawler.start()
    # crawler.join()
    # return HttpResponse("<html>liuyanbaike runnining over.</html>")