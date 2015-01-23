# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
import xml.etree.ElementTree as ET
from django.http import HttpResponse
import hashlib
import time

logo_url = r'https://mmbiz.qlogo.cn/mmbiz/RCx81AIZk5ETDGd9L5Om0FYOuVEibYcWNlpjcqkjL1aIflIMEHSAyeaGsyQhZcOK7HwwicN1GpPpDnVFxzicslFFw/0'
token = 'catkingisagoodman'

"""
check if the msg comes from wechat
"""
def check(request):
    try:
        query_dic = request.GET
        par = []
        par.append(token)
        par.append(query_dic['timestamp'])
        par.append(query_dic['nonce'])
        par.sort()
        par_sha1 = hashlib.sha1("".join(par)).hexdigest()
        return par_sha1 == query_dic['signature']
    except:
        return False

"""
get messages from wechat
"""
def get_msg(request):
    query_xml = ET.fromstring(request.body)
    msg = dict()
    msg["FromUserName"] = query_xml.find('FromUserName').text   
    msg["ToUserName"] = query_xml.find('ToUserName').text
    msg["MsgType"] = query_xml.find('MsgType').text    
    msg["Content"] = query_xml.find('Content').text
    msg["MsgId"] = query_xml.find('MsgId')
    
    return msg

"""
reply wechat users' messages.
request:POST query
"""        
def reply_msg(request):
 
    msg = get_msg(request)
        
    #msg = msg.decode("utf-8")
    ret_msg = []
    if msg.find(u'向兆威') != -1:
        ret_msg.append("向大脸！")
    elif msg.find(u"王继哲") != -1:
        ret_msg.append("小短腿！")
    else:
        ret_msg.append("猫王大好人！")
    ret_dic = dict()
    ret_dic['ToUserName'] = msg['FromUserName']
    ret_dic['FromUserName'] = msg['ToUserName']
    ret_dic['CreateTime'] = int(time.time())
    ret_dic['MsgType'] = 'text'
    ret_dic['Content'] = "".join(ret_msg)
        
    return render_to_response('reply_msg.xml', ret_dic, mimetype="application/xml")
 
"""
get nearest websites
"""
def get_articles(content):
    ret = []
    cnt = 3
    for i in cnt:
        website = {}
        website['Title'] = '文章' + i
        website['Description'] = '测试图文' + i
        website['PicUrl'] = logo_url
        website['Url'] = 'www.baidu.com'
        ret.append(website)
    return ret
   
"""
reply news
request:POST query
"""        
def reply_news(request):
 
    msg = get_msg(request)
        
    ret_dic = dict()
    ret_dic['ToUserName'] = msg['FromUserName']
    ret_dic['FromUserName'] = msg['ToUserName']
    ret_dic['CreateTime'] = int(time.time())
    ret_dic['MsgType'] = 'news'
    
    articles = get_articles(msg['Content'])        
    ret_dic['ArticleCount'] = len(articles)
    ret_dic['news_list'] = articles
        
    return render_to_response('reply_news.xml', ret_dic, mimetype="application/xml")