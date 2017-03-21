# -*- coding:utf-8 -*-
import re
import urllib
import urllib2
import sys
import os
import threading
import Queue
req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		 'Accept':'text/html;q=0.9,*/*;q=0.8',
		 'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		 'Accept-Encoding':'gzip',
		 'Connection':'close',
		 'Referer':'http://www.migudm.com'
		 }
for i in range(231,232):
    req = urllib2.Request("http://www.migudm.cn/opus/webQueryWatchOpusInfo.html?hwOpusId=000000051390&index="+str(i)+"&opusType=2",None,req_header)
    resp = urllib2.urlopen(req,None,5)
    html = resp.read()
    resp.close()		
    hpath=re.findall(r"\"url\"\:\"(.*?)\"}",html.decode('utf8'))
    # 使用Queue来线程通信，因为队列是线程安全的（就是默认这个队列已经有锁）
    q = Queue.Queue()
    for url in hpath:
        q.put(url)
        
    os.makedirs('d:/migudm/'+str(i),0)

    def fetch_img_func(q):
        while True:
            try:
                # 不阻塞的读取队列数据
                url = q.get_nowait()
            except Exception, e:
                print e
                break
            #print 'handle %s pic... pic url %s ' % (i, url)
            req = urllib2.Request(url,None,req_header)
            resp = urllib2.urlopen(req,None,5)
            html = resp.read()
            resp.close()
            name=re.findall(r"original/(.*?)\?st=",url.decode('utf8'))
            name=re.findall(r"original/(.*?)\?st=",url)
            f=file('d:/migudm/'+str(i)+'/'+name[0],'wb')
            f.write(html)
            f.close()		
            print name[0]		
            print name[0]+'下载完成'.decode('utf-8')		
        
    t1 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_1")
    t2 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_2")
    t3 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_3")
    #t4 = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_4")
    t1.start()
    t2.start()
    t3.start()
    #t4.start()
    t1.join()
    t2.join()
    t3.join()
    #t4.join()