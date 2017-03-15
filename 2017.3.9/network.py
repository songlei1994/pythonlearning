import urllib
import urllib2
from lxml import etree
class network(object):
	def request(self,url):
		result = urllib2.urlopen(url).read()
	return result
	def urltoxpath(self,url):
		result = urllib2.urlopen(url).read()
		dom=etree.HTML(result)
		return dom