from urllib2 import urlopen
from urllib2 import Request
from urllib2 import ProxyHandler
from urllib2 import build_opener
from urllib2 import install_opener
import urllib
from random import randint

def wordListSum(wordList):
  sum=0
  for word,value in wordList.items():
    sum+=value
  return sum

def retrieveRandomWord(wordList):
  randIndex=randint(1,wordListSum(wordList))
  for word,value in wordList.items():
    randIndex-=value
    if randIndex<=0:
      return word
def buildWordDict(text):
  text=text.replace("\n"," ")
  text=text.replace("\"","")
  punctuation=[',','.',';',':']
  for symbol in punctuation:
    text=text.replace(symbol," "+symbol+" ")
  words=text.split(" ")
  words=[word for word in words if word !=""]

  wordDict={}
  for i in range(1,len(words)):
    if words[i-1] not in wordDict:
      wordDict[words[i-1]]={}
    if words[i] not in wordDict[words[i-1]]:
      wordDict[words[i-1]][words[i]]=0
    wordDict[words[i-1]][words[i]]=wordDict[words[i-1]][words[i]]+1
  return wordDict

url="http://pythonscraping.com/files/inaugurationSpeech.txt"
#proxy_handler = ProxyHandler({'http': '127.0.0.1:80'})
proxy_handler = ProxyHandler({'sock5': 'localhost:1080'})
opener = build_opener(proxy_handler)  
install_opener(opener) 
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
request = Request(url,data,headers)
#request = request.add_header('user_agent','Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
textt=str(urlopen(request).read())
wordDictt=buildWordDict(textt)

length=100
chain=""
currentWord="I"
for i in range(0,length):
  chain +=currentWord+" "
  currentWord=retrieveRandomWord(wordDictt[currentWord])

print(chain)