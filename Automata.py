import random

funciones = ""
actores = [0,0,0,0,0,0,0]
global count
count = 0
file = open("ntree.txt","w") 

#                            0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1                                           
RelacionesEntreFunciones = [[0,0,0,5,0,0,0,3,0,0,0,3,0,6,5,0,0,0,0,0,3,6,0,0,0,0,0,0,0,0,0,0],#0 Alejamiento
                            [8,0,6,0,0,0,2,7,5,5,0,6,0,0,7,0,0,3,0,0,0,0,0,0,3,0,6,0,0,0,0,0],#1 Prohibicion
                            [5,4,6,0,0,0,0,7,5,0,2,0,6,0,3,0,0,6,4,0,5,0,3,2,2,0,0,0,0,0,3,0],#2 Transgresion
                            [5,5,0,0,0,5,5,0,0,0,5,5,5,0,5,0,0,0,0,0,5,5,0,0,0,5,5,5,0,0,0,0],#3 Conocimiento
                            [5,0,0,5,0,0,0,0,0,5,0,5,5,0,5,5,5,5,0,0,5,5,5,5,5,5,0,5,0,0,0,0],#4 Informacion
                            [2,0,2,0,2,0,2,2,2,0,2,0,2,2,2,2,2,2,0,2,2,2,2,2,2,0,2,2,2,2,2,2],#5 Engano
                            [0,0,2,0,2,2,0,2,2,0,0,2,2,2,2,0,2,0,2,0,2,2,0,0,2,0,2,2,2,0,2,0],#6 Trickery
                            [0,2,2,0,2,2,0,0,2,2,0,2,2,2,2,2,2,2,0,0,0,0,2,2,0,0,2,0,0,0,0,2],#7 Complicidad
                            [2,2,2,0,0,2,0,0,0,0,2,0,2,2,2,2,2,2,0,2,0,0,2,0,0,2,0,0,2,0,2,0],#8 Fechoria
                            [0,0,0,2,2,2,0,2,2,0,2,2,0,2,0,2,0,2,0,2,2,0,0,0,0,0,0,0,0,0,0,2],#9 Mediacion
                            [0,0,0,0,0,2,0,2,0,0,0,2,2,2,2,2,2,0,2,2,2,2,2,0,0,0,2,0,2,0,0,2],#20 Recompensa
                            [0,0,0,2,2,0,0,2,0,0,0,0,2,2,2,0,2,2,2,0,2,2,0,2,0,2,0,2,2,0,0,0],#22 Aceptacion
                            [0,0,2,2,0,0,0,2,0,0,0,0,0,2,0,0,2,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0],#22 Partida
                            [0,0,0,0,0,2,2,0,2,2,2,2,0,0,2,2,0,2,2,2,2,0,2,2,0,2,2,0,2,0,0,0],#23 Prueba
                            [2,2,2,0,0,2,0,0,2,0,0,2,2,0,0,0,0,2,0,0,0,2,2,2,0,0,0,2,2,2,2,0],#24 Reaccion
                            [2,0,0,2,2,0,0,0,2,0,2,2,2,2,0,0,2,2,0,2,0,2,0,0,2,0,2,2,0,0,2,0],#25 Regalo
                            [0,0,0,2,2,0,0,0,0,0,2,0,0,2,0,0,0,2,0,0,2,2,2,2,0,2,2,0,0,0,0,0],#26 Viaje
                            [2,0,2,0,0,0,0,2,2,0,2,0,2,2,2,0,0,0,0,2,0,0,2,2,0,2,0,2,2,2,0,0],#27 Lucha
                            [0,0,0,2,2,0,0,0,2,0,0,2,0,2,2,0,0,0,0,0,0,2,0,2,0,2,0,0,0,2,2,0],#28 Marca
                            [0,0,0,0,0,0,0,0,0,0,2,2,2,0,2,2,2,0,0,0,2,2,0,0,0,0,0,0,0,2,2,2],#29 Victoria
                            [2,0,0,2,0,2,0,0,0,0,2,2,2,0,2,0,0,2,0,2,0,2,0,0,0,0,0,0,0,0,0,2],#20 Enmienda
                            [0,2,0,2,0,2,0,0,0,0,2,0,0,2,0,2,2,0,0,2,2,0,0,2,0,2,2,0,0,0,2,2],#22 Regreso
                            [2,0,2,0,0,0,0,0,2,2,0,0,2,2,0,0,2,2,0,2,2,0,0,0,0,2,0,2,2,0,2,0],#22 Persecucion
                            [0,0,0,0,0,0,0,0,0,0,2,0,2,0,2,2,2,0,2,2,2,2,0,0,0,2,2,2,0,0,0,0],#23 Socorro
                            [0,0,2,0,0,2,0,0,2,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0,2,0,0,0,2,0],#24 Fingimiento
                            [0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,2,2,2,2,0,0,2,0,0,0,2,0,0,0,0,0],#25 Tareadificil
                            [0,0,0,0,0,0,0,0,0,0,2,0,2,0,2,2,0,0,0,2,2,2,0,0,0,0,0,2,0,0,0,0],#26 Cumplimiento
                            [2,0,2,2,2,0,0,0,0,0,2,2,0,0,2,0,0,2,0,0,0,0,2,0,0,2,0,0,2,2,0,0],#27 Reconocimiento
                            [0,2,0,2,2,0,0,0,0,0,0,2,0,2,2,0,0,2,0,0,0,2,2,0,0,0,0,2,0,2,0,0],#28 Desenmascaramiento
                            [0,0,0,2,0,2,0,0,0,0,2,2,0,2,2,0,0,0,2,0,2,2,0,0,0,0,0,2,0,0,2,0],#29 Transfiguracion
                            [2,2,2,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,2,0,0,2,2,0,0,0,0,0,0,0,0,0],#30 Castigo
                            [2,0,0,0,0,2,0,2,0,0,0,0,2,0,2,2,2,0,2,0,0,2,0,0,0,0,2,0,0,2,0,0]]#31 Boda
#                            0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1                                           


#                            0 1 2 3 4 5 6                                           
RelacionesEntreActores =   [[0,0,0,0,0,0,0],#0 Alejamiento
                            [0,0,0,0,0,0,0],#1 Prohibicion
                            [0,0,0,0,0,0,0],#2 Transgresion
                            [0,0,0,0,0,0,0],#3 Conocimiento
                            [0,0,0,0,0,0,0],#4 Informacion
                            [0,0,0,0,0,0,0],#5 Engano
                            [0,0,0,0,0,0,0],#6 Trickery
                            [0,0,0,0,0,0,0],#7 Complicidad
                            [0,0,0,0,0,0,0],#8 Fechoria
                            [0,0,0,0,0,0,0],#9 Mediacion
                            [0,0,0,0,0,0,0],#10 Recompensa
                            [0,0,0,0,0,0,0],#11 Aceptacion
                            [0,0,0,0,0,0,0],#12 Partida
                            [0,0,0,0,0,0,0],#13 Prueba
                            [0,0,0,0,0,0,0],#14 Reaccion
                            [0,0,0,0,0,0,0],#15 Regalo
                            [0,0,0,0,0,0,0],#16 Viaje
                            [0,0,0,0,0,0,0],#17 Lucha
                            [0,0,0,0,0,0,0],#18 Marca
                            [0,0,0,0,0,0,0],#19 Victoria
                            [0,0,0,0,0,0,0],#20 Enmienda
                            [0,0,0,0,0,0,0],#21 Regreso
                            [0,0,0,0,0,0,0],#22 Persecucion
                            [0,0,0,0,0,0,0],#23 Socorro
                            [0,0,0,0,0,0,0],#24 Fingimiento
                            [0,0,0,0,0,0,0],#25 Tareadificil
                            [0,0,0,0,0,0,0],#26 Cumplimiento
                            [0,0,0,0,0,0,0],#27 Reconocimiento
                            [0,0,0,0,0,0,0],#28 Desenmascaramiento
                            [0,0,0,0,0,0,0],#29 Transfiguracion
                            [0,0,0,0,0,0,0],#30 Castigo
                            [6,6,0,0,0,0,0]]#31 Boda

class actor:
    nombre = ""
    pid = 0
    genero = 0
    numero = 0
    relaciones = [0,0,0,0,0,0,0]

    def __init__(self, ppid, pgenero, pnumero,pnombre, prelaciones):
        self.pid = ppid
        self.genero = pgenero
        self.numero = pnumero
        self.nombre = pnombre
        self.relaciones = prelaciones

class objeto:
    nombre = ""

class lugar:
    nombre = ""

def Alejamiento(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    ##file.write(a1.nombre + " Aleja de Lugar")
    #file.write("\n")

    file.write(a1.nombre + " Aleja X")
    file.write("\n")
    fid = 0
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] != 0):
            if(random.randrange(11) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Prohibicion(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Prohibicion de X a " + a2.nombre)
    #file.write("\n")
    file.write(a1.nombre + " Prohib " + a2.nombre)
    file.write("\n")
    fid = 1
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Transgresion(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Transgrede a " + a2.nombre)
    #file.write("\n")

    file.write(a1.nombre + " Transgre " + a2.nombre)
    file.write("\n")
    fid = 2
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Conocimiento(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " adquiere Conocimiento")
    #file.write("\n")

    file.write(a1.nombre + " Conoc X")
    file.write("\n")
    fid = 3
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a1,a2)
        
def Informacion(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write("Informacion sobre X")
    #file.write("\n")
    file.write(" Infor X")
    #file.write("\n")
    fid = 4
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a1,a2)
        
def Engano(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Engana a " + a2.nombre)
    #file.write("\n")

    file.write(a1.nombre + " Engan " + a2.nombre)
    file.write("\n")
    
    fid = 5
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)

def Trickery(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Trick a " + a2.nombre)
    #file.write("\n")

    file.write(a1.nombre + " Trick " + a2.nombre)
    file.write("\n")
    fid = 6
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)

def Complicidad(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return

    num = random.randrange(7)
    while(num == a1.pid):
        num = random.randrange(7)
    #file.write(actores[num].nombre + " tiene Complicidad con " + a1.nombre)
    #file.write("\n")
    file.write(actores[num].nombre + " Complic " + a1.nombre)
    file.write("\n")
    fid = 7
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,actores[num])
     
def Fechoria(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Fechoria a " + a2.nombre)
    #file.write("\n")

    file.write(a1.nombre + " Fechor " + a2.nombre)
    file.write("\n")
    fid = 8
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)

def Mediacion(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    num = random.randrange(7)
    while(num == a2.pid):
        num = random.randrange(7)
    #file.write(actores[num].nombre + " Mediacion con " + a2.nombre)
    #file.write("\n")

    file.write(actores[num].nombre + " Mediac " + a2.nombre)
    file.write("\n")
    fid = 9
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,actores[num])
        
def Recompensa(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    fid = 10
    num = random.randrange(7)
    while(num == a2.pid):
        num = random.randrange(7)
    #file.write(actores[num].nombre + " Recompensa a " + a2.nombre)
    #file.write("\n")
    file.write(actores[num].nombre + " Recomp " + a2.nombre)
    file.write("\n")
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Aceptacion(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Acepta")
    #file.write("\n")
    file.write(a1.nombre + " Acep X")
    file.write("\n")
    fid = 11
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Partida(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Parte hacia Lugar")
    #file.write("\n")
    file.write(a1.nombre + " Parti X")
    file.write("\n")
    fid = 12
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Prueba(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    fid = 13
    num = random.randrange(7)
    while(num == a2.pid):
        num = random.randrange(7)
    #file.write(actores[num].nombre + " Prueba a " + a2.nombre)
    #file.write("\n")
    file.write(actores[num].nombre + " Prueba " + a2.nombre)
    file.write("\n")
    
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,actores[num])
        
def Reaccion(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Reacciona")
    #file.write("\n")

    file.write(a1.nombre + " Reac X")
    file.write("\n")
    fid = 14
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Regalo(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    fid = 15
    num = random.randrange(7)
    while(num == a2.pid):
        num = random.randrange(7)
    #file.write(actores[num].nombre + " Regala Objeto a " + a2.nombre)
    #file.write("\n")
    file.write(actores[num].nombre + " Regal " + a2.nombre)
    file.write("\n")
    
    c = random.randrange(32)
    while(1):
        c = c + 1
        
        if(c > 100):
            break
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Viaje(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Viaja a Lugar")
    #file.write("\n")
    file.write(a1.nombre + " Viaje X")
    file.write("\n")
    fid = 16
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Lucha(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Lucha contra " + a2.nombre)
    #file.write("\n")
    file.write(a1.nombre + " Lucha " + a2.nombre)
    file.write("\n")
    fid = 17
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Marca(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a2.nombre + " afecta mentalmente a " + a1.nombre)
    #file.write("\n")

    file.write(a2.nombre + " Marca " + a1.nombre)
    file.write("\n")
    fid = 18
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a1,a2)
        
def Victoria(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a2.nombre + " tiene la Victoria")
    #file.write("\n")

    file.write(a2.nombre + " Vict X")
    file.write("\n")
    
    fid = 19
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Enmienda(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " se arregla con " + a2.nombre)
    #file.write("\n")

    file.write(a1.nombre + " Enmien " + a2.nombre)
    file.write("\n")
    fid = 20
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a1,a2)
        
def Regreso(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Regresa a Lugar")
    #file.write("\n")

    file.write(a1.nombre + " Regre X")
    file.write("\n")
    
    fid = 21
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Persecucion(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Persigue a " + a2.nombre)
    #file.write("\n")

    file.write(a1.nombre + " Pers " + a2.nombre)
    file.write("\n")
    
    fid = 22
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Socorro(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    fid = 23
    num = random.randrange(7)
    while(num == a2.pid):
        num = random.randrange(7)
    #file.write(a2.nombre + " Ayuda a " + actores[num].nombre)
    #file.write("\n")
    file.write(a2.nombre + " Ayud " + actores[num].nombre)
    file.write("\n")
    
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](actores[num],a2)
            
def Fingimiento(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Finge frente a " + a2.nombre)
    #file.write("\n")

    file.write(a1.nombre + " Finge " + a2.nombre)
    file.write("\n")
    fid = 24
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Tareadificil(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " lleva a cabo Tarea dificil")
    #file.write("\n")

    file.write(a1.nombre + " Tarea X")
    file.write("\n")
    
    fid = 25
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a1,a2)
        
def Cumplimiento(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Cumple con su acometido")
    #file.write("\n")
    file.write(a1.nombre + " Cump X")
    file.write("\n")
    fid = 26
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a1,a2)
        
def Reconocimiento(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Reconoce la verdadera forma de " + a2.nombre)
    #file.write("\n")
    file.write(a1.nombre + " Recon " + a2.nombre)
    file.write("\n")
    fid = 27
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Desenmascaramiento(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Desenmascara a " + a2.nombre)
    #file.write("\n")

    file.write(a1.nombre + " Desen " + a2.nombre)
    file.write("\n")
    fid = 28
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Transfiguracion(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " se Transfigura en Algo")
    #file.write("\n")

    file.write(a1.nombre + " Transfig X")
    file.write("\n")
    fid = 29
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a1,a2)
        
def Castigo(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Castiga a " + a2.nombre)
    #file.write("\n")

    file.write(a1.nombre + " Cast " + a2.nombre)
    file.write("\n")
    fid = 30
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)
        
def Boda(a1,a2):
    global count
    count += 1
    if((random.randrange(10) > 8  and count > 5) or count > 15):
                return
    #file.write(a1.nombre + " Boda con " + a2.nombre)
    file.write(a1.nombre + " Boda " + a2.nombre)
    file.write("\n")
   
    fid = 31
    c = random.randrange(32)
    while(1):
        c = c + 1
        if(c > 100):
            break
        
        if(RelacionesEntreFunciones[fid][c%32] !=0):
            if(random.randrange(10) < RelacionesEntreFunciones[fid][c%32]):
                return funciones[c%32](a2,a1)

def Inicio():
    num = random.randrange(3)
    if(num == 0):
        funciones[0](actores[0],actores[random.randrange(6)+1])
    elif(num == 1):
        funciones[2](actores[0],actores[random.randrange(6)+1])
    else:
        funciones[5](actores[0],actores[random.randrange(6)+1])
        
funciones = [Alejamiento,Prohibicion,Transgresion,Conocimiento,Informacion,Engano,Trickery,Complicidad,Fechoria,Mediacion,Recompensa,Aceptacion,Partida,Prueba,Reaccion,Regalo,Viaje,Lucha,Marca,Victoria,Enmienda,Regreso,Persecucion,Socorro,Fingimiento,Tareadificil,Cumplimiento,Reconocimiento,Desenmascaramiento,Transfiguracion,Castigo,Boda]


actores[0] = actor(0,0,0,"Heroe",[1,1,1,1,1,1,1])
actores[1] = actor(0,1,0,"Villano",[1,1,1,1,1,1,1])
actores[2] = actor(0,2,0,"Princesa",[1,1,1,1,1,1,1])
actores[3] = actor(0,3,0,"Donador",[1,1,1,1,1,1,1])
actores[4] = actor(0,4,0,"Ayudante",[1,1,1,1,1,1,1])
actores[5] = actor(0,5,0,"Agresor",[1,1,1,1,1,1,1])
actores[6] = actor(0,6,0,"Ordenante",[1,1,1,1,1,1,1])

Inicio()
file.close()


