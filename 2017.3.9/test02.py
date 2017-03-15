# -*- coding:utf-8 -*-
import urllib
import urllib2
from lxml import etree
postdata=urllib.urlencode({
'Accept' : '*/*'
})
req = urllib2.Request(url = 'http://www.bilibili.com/list/hot-32-3-2017-02-01~2017-02-28.html',data = postdata)
result = urllib2.urlopen(req).read()
dom=etree.HTML(result)
print result