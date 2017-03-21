# -*- coding:utf-8 -*-
import re
import urllib
import urllib2
import sys
import os
#只检查了refer而已,并没有用到cookie
req_header = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
'Accept': '*/*',
'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip',
'Referer': 'http://manhua.dmzj.com'}
url='http://images.dmzj.com/b/%E8%9D%99%E8%9D%A0%E4%BE%A0%20%E9%98%BF%E5%85%8B%E6%B1%89%E5%A7%86%E5%9F%8E-%20End%20Game/%E7%AC%AC02%E5%8D%B7_1366551455/000.jpg'
req = urllib2.Request(url,None,req_header)
resp = urllib2.urlopen(req,None,5)
html = resp.read()
resp.close()
f=file('d:/2.jpg','wb')
f.write(html)
f.close()    