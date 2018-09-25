from urllib2 import urlopen
from bs4 import BeautifulSoup
from urllib2 import Request
from urllib2 import ProxyHandler
from urllib2 import build_opener
from urllib2 import install_opener
import urllib
#url="http://api.xicidaili.com/free2016.txt"
url="http://www.xicidaili.com/"
proxy_handler = ProxyHandler({'http':'localhost:8081'})
opener = build_opener(proxy_handler)  
install_opener(opener) 
user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'
values = {'name' : 'Michael Foord',
        'location' : 'beijing',
        'language' : 'Python' }
headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
request = Request(url,data,headers)
html=urlopen(request)
print(html.read())
#bsObj=BeautifulSoup(html)
#print(type(bsObj))
#print(any(bsObj))
#print(bsObj.title)
#iplist=bsObj.find("table",{"id":"ip_list"}).tr.children
#iplist=bsObj.r
#ipaddres=iplist[1]
#ipaddres=ipport[2]
#print(ipaddres)
#print(ipport)