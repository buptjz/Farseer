# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
import xml.etree.ElementTree as ET
from django.http import HttpResponse
import hashlib
import time


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
reply wechat users' messages.
request:POST query
"""        
def reply_msg(request):
 
    query_xml = ET.fromstring(request.body)
        
    wechat_user = query_xml.find('FromUserName').text   
    dev_user = query_xml.find('ToUserName').text
    msg_type = query_xml.find('MsgType').text    
    msg = query_xml.find('Content').text
    msg_ID = query_xml.find('MsgId')
        
    #msg = msg.decode("utf-8")
    ret_msg = []
    if msg.find(u'向兆威') != -1:
        ret_msg.append("向大脸！")
    elif msg.find(u"王继哲") != -1:
        ret_msg.append("小短腿！")
    else:
        ret_msg.append("猫王大好人！")
    ret_dic = dict()
    ret_dic['ToUserName'] = wechat_user
    ret_dic['FromUserName'] = dev_user
    ret_dic['CreateTime'] = int(time.time())
    ret_dic['MsgType'] = 'text'
    ret_dic['Content'] = "".join(ret_msg)
        
    return render_to_response('reply_msg.xml', ret_dic, mimetype="application/xml")