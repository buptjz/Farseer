__author__ = 'wangjz'

from django.conf.urls import patterns, url

from spider import views

urlpatterns = patterns('',
    # url(r'^$', views.index, name='index'),
    url(r'^run$', views.run_spider, name = 'index')
)