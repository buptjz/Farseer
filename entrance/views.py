# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
import xml.etree.ElementTree as ET
from django.http import HttpResponse
import hashlib
import time
import Farseer
DEBUG = Farseer.settings.DEBUG

import method

        
def index(request):
    if not DEBUG and not method.check(request):
        return HttpResponse("not valid")
    else:
        if request.method == 'GET':
            return HttpResponse(request.GET['echostr'])
        else:
            return method.reply_news(request)
