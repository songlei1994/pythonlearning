# -*- coding:utf-8 -*-
import re
import urllib
import urllib2
import sys
from lxml import etree
path='http://www.heibanke.com/lesson/crawler_ex00/'
tpath=path
number=urllib.urlopen(tpath).read()
dom=etree.HTML(number)
m=re.findall(r'\d+',dom.xpath('//h3/text()')[0])
while (m):
	print m[0]
	tpath=path+m[0]	
	number=urllib.urlopen(tpath).read()
	dom=etree.HTML(number)
	m=re.findall(r'\d+',dom.xpath('//h3/text()')[0])
print tpath