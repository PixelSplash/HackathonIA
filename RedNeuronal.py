import nltk
from nltk.collocations import *

f = open('textofinal.txt', encoding="utf8")
raw = f.read()

tokens = nltk.word_tokenize(raw)

#Create your bigrams
tgs = nltk.trigrams(tokens)

#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(tgs)

'''
for k,v in fdist.items():
    print (k)
    print (v)
'''

file =  open('ntree.txt', "r", encoding="utf8")
print(file.read())


if(c = "Aleja"):
    pass
if(c = "Prohib"):
    pass
if(c = "Transgre"):
    pass
if(c = "Conoc"):
    pass
if(c = "Infor"):
    pass
if(c = "Engan"):
    pass
if(c = "Trick"):
    pass
if(c = "Complic"):
    pass
if(c = "Fechor"):
    pass
if(c = "Mediac"):
    pass
if(c = "Recomp"):
    pass
if(c = "Acep"):
    pass
if(c = "Parti"):
    pass
if(c = "Prueba"):
    pass
if(c = "Reac"):
    pass
if(c = "Regal"):
    pass
if(c = "Viaje"):
    pass
if(c = "Lucha"):
    pass
if(c = "Marca"):
    pass
if(c = "Vict"):
    pass
if(c = "Enmien"):
    pass
if(c = "Regre"):
    pass
if(c = "Pers"):
    pass
if(c = "Ayud"):
    pass
if(c = "Finge"):
    pass
if(c = "Tarea"):
    pass
if(c = "Cump"):
    pass
if(c = "Recon"):
    pass
if(c = "Desen"):
    pass
if(c = "Transfig"):
    pass
if(c = "Cast"):
    pass
if(c = "Boda"):
    pass


