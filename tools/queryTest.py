# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 00:13:18 2015

@author: catking
"""
import urllib,urllib2

def post_data(url,app_para_dct):
    content = ""
    if app_para_dct:
        para_data = urllib.urlencode(app_para_dct)
        f = urllib2.urlopen(url, para_data)
        content = f.read()
    return content
    
    
if __name__ == "__main__":
    post_dict = dict()
    post_dict['FromUserName'] = '123'
    post_dict['ToUserName'] = '123'
    post_dict['MsgType'] = '123'
    post_dict['Content'] = '123'
    post_dict['MsgId'] = '123'
    post_dict['text'] = '123'
    
    print post_data("http://127.0.0.1:8000/entrance/",post_dict)
