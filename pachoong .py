#! /usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
'''
url=http://weibo.com/whulecture
'''



import urllib2
import cookielib
import urllib2
import re
from json import JSONDecoder
import socket
import re
cookiejar = cookielib.LWPCookieJar()

import gzip
from StringIO import StringIO


def leture():
    le=[]
    li={}
    cookiejar = cookielib.CookieJar()
    cookieSupport= urllib2.HTTPCookieProcessor(cookiejar)
    opener = urllib2.build_opener(cookieSupport)
    urllib2.install_opener(opener)
    url = 'http://weibo.com/whulecture'

    head = {
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0'	,
        'Pragma':'no-cache',
        'Cookie' :'YF-Page-G0=82a2c733169b8fbd551fc09977b0f608; SUB=_2AkMiEU68f8NjqwJRmPoUzmrrbIh3yQHEiebDAHzsJxJjHk8m7HjoWB5hjcErEDOJUnKkkTzqIu73; SUBP=0033WrSXqPxfM72-Ws9jqgMF55z29P9D9WhpyhE-r1IE-CFJzaHvJ0EG; _s_tentry=passport.weibo.com; Apache=6880582037146.517.1431159181449; SINAGLOBAL=6880582037146.517.1431159181449; ULV=1431159181543:1:1:1:6880582037146.517.1431159181449:; YF-Ugrow-G0=57484c7c1ded49566c905773d5d00f82; YF-V5-G0=f59276155f879836eb028d7dcd01d03c',
        'Connection':'keep-alive',
        'Cache-Control':'no-cache',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
    url = urllib2.Request(url,headers=head)
    response = urllib2.urlopen(url)

    buf = StringIO(response.read())
    f = gzip.GzipFile(fileobj=buf)
    data = f.read()
    #print data
    a = re.findall(r'\#讲座信息\#\<\\\/a\>(.+?)\<\\\/div\>',data)
    for i in a:
        b = re.split(r'【.+?】',i)
        li['主题']=b[0]
        li['时间']=b[1]
        li['地点']=b[2]
        li['主讲人']=b[3]
        le.append(li)
    return le
li = leture()
for i in li:
    print i