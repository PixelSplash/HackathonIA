import nltk
from nltk.collocations import *

f = open('textofinal.txt', encoding="utf8")
raw = f.read()

tokens = nltk.word_tokenize(raw)

#Create your bigrams
tgs = nltk.trigrams(tokens)

#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(tgs)


for k,v in fdist.items():
    print (k)
    print (v)
