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
    #print(a)
    
    for k,v in tags:
        #print(k)
        if(k == a):
            return v
    return ''

def buscarTagsProbables(a,b):
    trigs = []
    a = buscarTag(a)
    b = buscarTag(b)
    #print(a)
    #print(b)
    
    for k,v in tdist.items():
        #print(k)
        
        if(k[0][1] == a and k[1][1] == b):
            return k[2][1]
        
    
    return ""
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

    cat = buscarTagsProbables(aux[n][1],aux[n][2])
    #print("primer tag.........")
    #print(cat)
    while(oracion[j] != '.' and oracion[j] != ',' and oracion[j] != ';'):
        c = 0
        aux = []
        for k,v in fdist.items():
                    if (oracion[j] in k[1] and oracion[j][0] == k[1][0]) and (oracion[j-1] in k[0] and oracion[j-1][0] == k[0][0]):
                        cataux = buscarTag(k[2])
                        #print(cataux)
                        if(cat == cataux):
                            c+=1
                            aux.append((k,v))
                            if(c > 20):
                                break
        if(aux == []):
            break
        maxx = aux[0][1]
        k = aux[0][0]
        for x in aux:
            if x[1] > maxx:
                maxx = x[1]
                k = x[0]
        
        oracion.append(k[2])
        
        j += 1
        #print("otro tag.........")
        cat = buscarTagsProbables(oracion[j-1],oracion[j])
        #print(cat)
    sta = ""
    for x in oracion:
        sta = sta + x + " "
    print(sta + " ")

for x in content:
    #print(x)
    arr = x.split()

    s = arr[0]
    c = arr[1]
    z = arr[2]
    i = 0
    if(c == "Aleja"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Prohib"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Transgre"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Conoc"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Infor"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Engan"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Trick"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Complic"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Fechor"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Mediac"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Recomp"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Acep"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Parti"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Prueba"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Reac"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Regal"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Viaje"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Lucha"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Marca"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Vict"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Enmien"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Regre"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Pers"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Ayud"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Finge"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Tarea"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Cump"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Recon"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Desen"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Transfig"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Cast"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")
    i+=1
    if(c == "Boda"):
        print(s,end=" ")
        formarOrac(i)
        print( "( " + z + " )")


