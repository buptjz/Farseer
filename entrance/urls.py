__author__ = 'wanghh'

from django.conf.urls import patterns, url

from spider import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)