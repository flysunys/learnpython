#from nltk.book import *
from nltk import word_tokenize
from nltk import pos_tag
from nltk import sent_tokenize
#text=word_tokenize("Strange women lying in ponds distributing swords is  no basis for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony")
#tags=pos_tag(text)
#print(tags)
sentences=sent_tokenize("Google is one of the best companies in the world. I constantly google myself to see what I'm up to")
nouns=['NN','NNS','NNP','NNPS']

for sentence in sentences:
  if "google" in sentence.lower():
    taggedWords=pos_tag(word_tokenize(sentence))
    for worde in taggedWords:
        if worde[0].lower()=="google" and worde[1] in nouns:
          print(worde[1])
          print(sentence)