import nltk
from nltk.collocations import *

categorias = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

f = open('textofinal.txt', encoding="utf8")
raw = f.read()

with open('ListaVerbos.txt', encoding="utf8") as f:
    verbos = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
verbos = [x.strip() for x in verbos]

i = 0
for x in verbos:
    if x == "-":
        i+=1
    else:
        categorias[i].append(x)

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

with open('ntree.txt', "r", encoding="utf8") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]


def formarOrac(i):
    j = 2
    c = ""
    oracion = []
    for k,v in fdist.items():
                if categorias[i][0] in k[2]:
                    oracion.append(k[0])
                    oracion.append(k[1])
                    oracion.append(k[2])
 
                    break
    
    while(oracion[j] != '.' and oracion[j] != ',' and oracion[j] != ';'):
        for k,v in fdist.items():
                    if oracion[j] in k[1] and oracion[j-1] in k[0]:
                        oracion.append(k[2])
                        j += 1
                        break
    print(oracion)
    print("\n")

for x in content:
    print(x)
    arr = x.split()

    s = arr[0]
    c = arr[1]
    z = arr[2]
    i = 0
    if(c == "Aleja"):
        formarOrac(i)
    i+=1
    if(c == "Prohib"):
       formarOrac(i)
    i+=1
    if(c == "Transgre"):
        formarOrac(i)
    i+=1
    if(c == "Conoc"):
        formarOrac(i)
    i+=1
    if(c == "Infor"):
        formarOrac(i)
    i+=1
    if(c == "Engan"):
        formarOrac(i)
    i+=1
    if(c == "Trick"):
        formarOrac(i)
    i+=1
    if(c == "Complic"):
        formarOrac(i)
    i+=1
    if(c == "Fechor"):
        formarOrac(i)
    i+=1
    if(c == "Mediac"):
        formarOrac(i)
    i+=1
    if(c == "Recomp"):
        formarOrac(i)
    i+=1
    if(c == "Acep"):
        formarOrac(i)
    i+=1
    if(c == "Parti"):
        formarOrac(i)
    i+=1
    if(c == "Prueba"):
        formarOrac(i)
    i+=1
    if(c == "Reac"):
        formarOrac(i)
    i+=1
    if(c == "Regal"):
        formarOrac(i)
    i+=1
    if(c == "Viaje"):
        formarOrac(i)
    i+=1
    if(c == "Lucha"):
        formarOrac(i)
    i+=1
    if(c == "Marca"):
        formarOrac(i)
    i+=1
    if(c == "Vict"):
        formarOrac(i)
    i+=1
    if(c == "Enmien"):
        formarOrac(i)
    i+=1
    if(c == "Regre"):
        formarOrac(i)
    i+=1
    if(c == "Pers"):
        formarOrac(i)
    i+=1
    if(c == "Ayud"):
        formarOrac(i)
    i+=1
    if(c == "Finge"):
        formarOrac(i)
    i+=1
    if(c == "Tarea"):
        formarOrac(i)
    i+=1
    if(c == "Cump"):
        formarOrac(i)
    i+=1
    if(c == "Recon"):
        formarOrac(i)
    i+=1
    if(c == "Desen"):
        formarOrac(i)
    i+=1
    if(c == "Transfig"):
        formarOrac(i)
    i+=1
    if(c == "Cast"):
        formarOrac(i)
    i+=1
    if(c == "Boda"):
        formarOrac(i)


