import urllib2
import cookielib
#����һ��CookieJar����ʵ��������cookie
cookie = cookielib.CookieJar()
#����urllib2���HTTPCookieProcessor����������cookie������
handler=urllib2.HTTPCookieProcessor(cookie)
#ͨ��handler������opener
opener = urllib2.build_opener(handler)
#�˴���open����ͬurllib2��urlopen������Ҳ���Դ���request
response = opener.open('http://manhua.dmzj.com/yiquanchaoren/19954.shtml')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value