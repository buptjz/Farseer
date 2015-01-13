from django.db import models

# Create your models here.


class Page(models.Model):
    """Model of a web page"""
    url = models.URLField(max_length=200)
    content = models.TextField()
    scrawl_date = models.DateTimeField('date scrawling')