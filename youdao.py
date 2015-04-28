#encoding:utf-8

import urllib,urllib2
import json
def fanyi(name):
    url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

    data={}
    data["type"]="AUTO"

    data["doctype"]="json"
    data["xmlVersion"]="1.6"
    data["keyfrom"]="fanyi.web"
    data["ue"]="UTF-8"
    data["typoResult"]="true"
    data["i"] = name

    data=urllib.urlencode(data).encode("utf-8")

    openurl= urllib2.urlopen(url,data)
    text=openurl.read().decode('utf-8')

    text=json.loads(text)

    a=text['translateResult'][0][0]['tgt']

    print a
danci=raw_input("输入单词：")
while danci!='q':
	fanyi(danci)
	danci=raw_input("输入单词：")



