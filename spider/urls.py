__author__ = 'wangjz'

from django.conf.urls import patterns, url

from spider import views

urlpatterns = patterns('',
    url(r'^send$', views.send_post, name='index'),
    url(r'^run$', views.run_spider, name = 'index'),
    url(r'^receive$', views.receive_post, name = 'index')
)