import nltk
from nltk.collocations import *
import random

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

tags = nltk.pos_tag(tokens)

#Create your bigrams
tgs = nltk.trigrams(tokens)
tagstgs = nltk.trigrams(tags)
#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(tgs)
tdist = nltk.FreqDist(tagstgs)

'''
for k,v in tdist.items():
    print (k)
    print (v)
'''

with open('ntree.txt', "r", encoding="utf8") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

def buscarTag(a):
    print(a)
    
    for k,v in tags:
        print(k)
        if(k == a):
            return v
    return ''

def buscarTagsProbables(a,b):
    trigs = []
    a = buscarTag(a)
    b = buscarTag(b)
    print(a)
    print(b)
    for k,v in tdist.items():
        #print(k)
        if(k[0][1] == a and k[1][1] == b):
            trigs.append((k,v))
    print(trigs)
    maxx = trigs[0][1]
    k = trigs[0][0]
    
    for x in trigs:
        if maxx < x[1]:
            maxx = x[1]
            k = x[0]
    return k[2][1]

def formarOrac(i):
    j = 2
    oracion = []
    aux = []
    c = 0
    z = 0
    while(aux == [] and z<len(categorias[i])):
        for k,v in fdist.items():
                    if categorias[i][z] in k[0] and categorias[i][z][0] == k[0][0]:
                        c+=1
                        aux.append(k)    
                        if(c > 20):
                            break
        z+=1
    
    n = random.randrange(len(aux))
    oracion.append(aux[n][0])
    oracion.append(aux[n][1])
    oracion.append(aux[n][2])

    print(buscarTagsProbables(aux[n][1],aux[n][2]))
    while(oracion[j] != '.' and oracion[j] != ',' and oracion[j] != ';'):
        c = 0
        aux = []
        for k,v in fdist.items():
                    if (oracion[j] in k[1] and oracion[j][0] == k[1][0]) and (oracion[j-1] in k[0] and oracion[j-1][0] == k[0][0]):
                        c+=1
                        aux.append((k,v))
                        if(c > 20):
                            break
        maxx = aux[0][1]
        k = aux[0][0]
        for x in aux:
            if x[1] > maxx:
                maxx = x[1]
                k = x[0]
        
        oracion.append(k[2])               
        j += 1
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
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Prohib"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Transgre"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Conoc"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Infor"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Engan"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Trick"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Complic"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Fechor"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Mediac"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Recomp"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Acep"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Parti"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Prueba"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Reac"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Regal"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Viaje"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Lucha"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Marca"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Vict"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Enmien"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Regre"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Pers"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Ayud"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Finge"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Tarea"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Cump"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Recon"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Desen"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Transfig"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Cast"):
        print(s)
        formarOrac(i)
    i+=1
    if(c == "Boda"):
        print(s)
        formarOrac(i)


