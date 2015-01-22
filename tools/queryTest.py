# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 00:13:18 2015

@author: catking
"""
import urllib,urllib2

def text_from_wechat(data_dict):
    data = ["<xml>\n"]
    data.append("<ToUserName><![CDATA[")
    data.append(data_dict['ToUserName'])
    data.append("]]></ToUserName>\n")
    data.append("<FromUserName><![CDATA[")
    data.append(data_dict['FromUserName'])
    data.append("]]></FromUserName>\n")
    data.append("<CreateTime>")
    data.append(data_dict['CreateTime'])
    data.append("</CreateTime>\n")
    data.append("<MsgType><![CDATA[")
    data.append("text")
    data.append("]]></MsgType>\n")
    data.append("<Content><![CDATA[")
    data.append(data_dict['Content'])
    data.append("]]></Content>\n")
    data.append("<MsgId>")
    data.append(data_dict['MsgId'])
    data.append("</MsgId>\n")
    data.append("</xml>")
    return "".join(data)
"""
def post_data(url,app_para_dct):
    content = ""
    if app_para_dct:
        para_data = urllib.urlencode(app_para_dct)
        f = urllib2.urlopen(url, para_data)
        content = f.read()
    return content
"""
def post_data(url,app_para_dict):
    cookies = urllib2.HTTPCookieProcessor()
    opener = urllib2.build_opener(cookies)
 
    request = urllib2.Request(
        url = url,
        data = app_para_dict)
 
    return opener.open(request).read()
    
    
if __name__ == "__main__":
    post_dict = dict()
    post_dict['FromUserName'] = '123'
    post_dict['ToUserName'] = '123'
    post_dict['MsgType'] = 'text'
    post_dict['Content'] = '123'
    post_dict['MsgId'] = '123'
    post_dict['CreateTime'] = '123'
    
    print post_data("http://127.0.0.1:8000/entrance/",text_from_wechat(post_dict))
    #print post_data("http://rumordetector.sinaapp.com/entrance",text_from_wechat(post_dict))

