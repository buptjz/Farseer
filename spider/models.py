# -*- coding: utf-8 -*-


from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.


class Page(models.Model):
    def __str__(self):
        return "url : " + self.url + "\nscrawl date : " + str(self.scrawl_date)

    """Model of a web page"""
    url = models.URLField(max_length=200)
    content = models.TextField()
    scrawl_date = models.DateTimeField('date scrawling')


class Gossip(models.Model):
    """Model of a Gossip"""
    # def __str__(self):
    #     return smart_unicode(self.title)
    def __unicode__(self):
        return smart_unicode(self.title)

    url = models.URLField(max_length=200, null=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    keywords = models.TextField(default="")
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    source_url = models.URLField(max_length=200, null=True)
    source = models.CharField(max_length=300)
    publish_date = models.DateTimeField(null=True)
    scrawl_date = models.DateTimeField(null=True)
    status = models.IntegerField(null=True)


class RumorBaike(models.Model):
    """Model of a www.liuyanbaike.com"""
    def __unicode__(self):
        return "[" + smart_unicode(self.tf_type) + "]" + smart_unicode(self.title)

    url = models.URLField(max_length=200, null=True)#url
    page_id = models.PositiveIntegerField(default=0)#page id
    title = models.CharField(max_length=300)#标题
    rumor_desc = models.TextField()#流言内容
    rumor_truth = models.TextField()#流言真相
    rumor_content = models.TextField()#论证
    tf_type = models.CharField(max_length=30)#真?假?新?论?

    tags = models.CharField(max_length=300)#标签
    category = models.CharField(max_length=100)#分类

    source_url = models.URLField(max_length=200, null=True)#来源url
    update_date = models.DateTimeField(null=True)#更新日期
    scrawl_date = models.DateTimeField(null=True)#抓去日期
    status = models.IntegerField(null=True)#抓去的状态