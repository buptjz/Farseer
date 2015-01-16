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
