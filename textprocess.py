from urllib2 import urlopen
from bs4 import BeautifulSoup
from itertools import product
import re
import string
import operator

def cleanInput(input):
  input=re.sub('\n+'," ",input)
  input=re.sub('\[[0-9]*\]',"",input)
  #input=re.sub('\+*'," ",input)
  cleanInput=[]
  input=input.split(' ')
  for item in input:
    item=item.strip(string.punctuation)
    if len(item)>1 or (item.lower()=='a' or item.lower()=='i'):
      cleanInput.append(item)
  return cleanInput

def ngrams(input,n):
  input=cleanInput(input)
  output={}
  for i in range(len(input)-n+1):
    if isCommon(input[i:i+n])==False:
      ngramTemp=" ".join(input[i:i+n])
      if ngramTemp not in output:
        output[ngramTemp]=0
      output[ngramTemp]+=1
  return output

def isCommon(ngram):
  commonWords=["the","be","and","of","a","in","to","have","it",
    "i","that","for","you","he","with","on","do","say","this", 
    "they","is","an","at","but","we","his","from","that","not","by",
    "she","or","as","what","go","their","can","who","get", "if",
    "would","her","all","my","make","about","know","will", "as",
    "up","one","time","has","been","there","year","so", "think",
    "when","which","them","some","me","people","take", "out","into",
    "just","see","him","your","come","could","now", "than","like",
    "other","how","then","its","our","two","more", "these","want",
    "way","look","first","also","new","because", "day","more","use",
    "no","man","find","here","thing","give", "many","well"]
  for word in ngram: 
    if word.lower() in commonWords:
      return True 
  return False

def isSubstring(s1,s2):
  if s1 in s2:
    return True
  else:
    return False

  
content=str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read())
ngrams=ngrams(content,2)
print(type(ngrams))
#print(ngrams)
#ngramss={}
#for ngram in ngrams.items():
#  print(ngram)
  #if isCommon(ngram):
    #ngramss.append(ngram)

sortedNGrams=sorted(ngrams.items(),key=operator.itemgetter(1),reverse=True)
#print(sortedNGrams)
#print(type(sortedNGrams))
fif5Grams=sortedNGrams[0:2]
#print(type(fif5Grams))
fif5Gramskey=[itemb[0] for itemb in fif5Grams]
#print(fif5Gramskey)
sentences=content.split('.')
#for x,y in product(fif5Gramskey,sentences):
#  if isSubstring(x,y):
#    print(y)
#for paragraph in content.split('\n\n'):
#  print(paragraph)
#  print("---------------")
  #print(len(paragraph.split('.')))

firstsentences=[paragraph.split('.')[0] for paragraph in content.split('\n\n') ]
for itte in firstsentences:
  print(itte)