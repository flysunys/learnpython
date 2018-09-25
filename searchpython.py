from urllib2 import urlopen
from bs4 import BeautifulSoup
import pymysql

#connectioninfo={host='127.0.0.1',user='root',passwd='1234',port='3306',db='wikipedia',charset='utf-8'}
conn=pymysql.connect(host='127.0.0.1',user='root',passwd='1234',port=3306,db='wikipedia',charset='utf8')
#print('1234567890')
cur=conn.cursor()
cur.execute('use wikipedia')

class SolutionFound(RuntimeError):
  def __init__(self,message):
    self.message=message

def getLinks(fromPageId):
  cur.execute("select topageid from links where frompageid=%s",(fromPageId))
  if cur.rowcount==0:
    return None
  else:
    return [x[0] for x in cur.fetchall()]

def constructDict(currentPageId):
  links=getLinks(currentPageId)
  if links:
    return dict(zip(links,[{}]*len(links)))
  return {}

def searchDepth(targetPageId,currentPageId,linkTree,depth):
  if depth==0:
    return linkTree
  if not linkTree:
    linkTree=constructDict(currentPageId)
    if not linkTree:
      return {}
  if targetPageId in linkTree.keys():
    print("TARGET"+str(targetPageId)+"FOUND!")
    raise SolutionFound("PAGE:"+str(currentPageId))
  for branchKey,branchValue in linkTree.items():
    try:
      linkTree[branchKey]=searchDepth(targetPageId,branchKey,branchValue,depth-1)
    except SolutionFound as e:
      print(e.message)
      raise SolutionFound("PAGE"+str(currentPageId))
  return linkTree

try:
  searchDepth(134951,1,{},4)
  print("No solution found")
except SolutionFound as e:
  print(e.message)

conn.close()