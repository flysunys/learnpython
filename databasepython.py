from urllib2 import urlopen
from urllib2 import Request
from urllib2 import ProxyHandler
from urllib2 import build_opener
from urllib2 import install_opener
import urllib
from bs4 import BeautifulSoup 
import re 
import pymysql 
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='1234',db='wikipedia',charset='utf8') 
cur=conn.cursor() 
cur.execute("USE wikipedia") 
def insertPageIfNotExists(url): 
  cur.execute("SELECT*FROM pages WHERE url=%s",(url)) 
  if cur.rowcount==0: 
    cur.execute("INSERT INTO pages (url) VALUES (%s)",(url)) 
    conn.commit() 
    return cur.lastrowid 
  else: 
    return cur.fetchone()[0] 
def insertLink(fromPageId,toPageId): 
  cur.execute("SELECT * FROM links WHERE frompageid = %s AND topageid = %s", (int(fromPageId),int(toPageId))) 
  if cur.rowcount==0: 
    cur.execute("INSERT INTO links (frompageid,topageid) VALUES (%s,%s)", (int(fromPageId),int(toPageId)))
    conn.commit() 
pages=set() 
def getLinks(pageUrl,recursionLevel):
  global pages
  if recursionLevel>4: 
    return; 
  pageId=insertPageIfNotExists(pageUrl)
  url="http://en.wikipedia.org"+pageUrl
  proxy_handler = ProxyHandler({'http':'114.113.126.86:80'})
  opener = build_opener(proxy_handler)  
  install_opener(opener) 
  user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'
  values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
  headers = { 'User-Agent' : user_agent }
  data = urllib.urlencode(values)
  request = Request(url,data,headers)  
  html=urlopen(request) 
  bsObj=BeautifulSoup(html) 
  for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    insertLink(pageId,insertPageIfNotExists(link.attrs['href'])) 
    if link.attrs['href'] not in pages: 
      newPage=link.attrs['href'] 
      pages.add(newPage) 
      getLinks(newPage,recursionLevel+1) 
getLinks("/wiki/Kevin_Bacon",0) 
cur.close() 
conn.close()
