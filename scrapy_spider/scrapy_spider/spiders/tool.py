__author__ = 'wangjz'

import urllib2
import json


def post_dict(url, dict):
    req = urllib2.Request('http://abc.com/api/posts/create')
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(dict))
    return response