#coding = cp936
import urllib2
import urllib
import re

def gitimg(html):
    
    reg =  r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'0%s.jpg' % x)
        x+=1



headers ={
'User-Agent':'Mozilla/5.0(Windows;U;Windows NT 6.1;en-US;rv:1.9.1.6)Gecko/20091201 Firefox/3.56'}
request = urllib2.Request(url='http://jandan.net/ooxx',headers = headers)
html = urllib2.urlopen(request).read()
print gitimg(html)
