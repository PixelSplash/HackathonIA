import random

funciones = ""
actores = [0,0,0,0,0,0,0]

#                            0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1                                           
RelacionesEntreFunciones = [[0,0,0,5,0,0,0,3,0,0,0,3,0,6,5,0,0,0,0,0,3,6,0,0,0,0,0,0,0,0,0,0],#0 Alejamiento
                            [8,0,6,0,0,0,2,7,5,5,0,6,0,0,7,0,0,3,0,0,0,0,0,0,3,0,6,0,0,0,0,0],#1 Prohibicion
                            [5,4,6,0,0,0,0,7,5,0,1,0,6,0,3,0,0,6,4,0,5,0,3,2,2,0,0,0,0,0,3,0],#2 Transgresion
                            [1,1,0,0,0,1,1,0,0,0,1,1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0],#3 Conocimiento
                            [1,0,0,1,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,0,1,0,0,0,0],#4 Informacion
                            [1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1],#5 Engano
                            [0,0,1,0,1,1,0,1,1,0,0,1,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,1,0,1,0],#6 Trickery
                            [0,1,1,0,1,1,0,0,1,1,0,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,0,0,0,0,1],#7 Complicidad
                            [1,1,1,0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,1,0],#8 Fechoria
                            [0,0,0,1,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1],#9 Mediacion
                            [0,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1,0,0,1],#10 Recompensa
                            [0,0,0,1,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1,1,0,0,0],#11 Aceptacion
                            [0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],#12 Partida
                            [0,0,0,0,0,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,1,1,0,1,0,0,0],#13 Prueba
                            [1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,1,1,1,0],#14 Reaccion
                            [1,0,0,1,1,0,0,0,1,0,1,1,1,1,0,0,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1,0],#15 Regalo
                            [0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,0,1,1,0,0,0,0,0],#16 Viaje
                            [1,0,1,0,0,0,0,1,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,0,0],#17 Lucha
                            [0,0,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,1,0],#18 Marca
                            [0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1],#19 Victoria
                            [1,0,0,1,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1],#20 Enmienda
                            [0,1,0,1,0,1,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,0,0,1,0,1,1,0,0,0,1,1],#21 Regreso
                            [1,0,1,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,1,0,1,1,0,1,0],#22 Persecucion
                            [0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,1,1,0,0,0,0],#23 Socorro
                            [0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0],#24 Fingimiento
                            [0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0,0,1,0,0,0,0,0],#25 Tareadificil
                            [0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0],#26 Cumplimiento
                            [1,0,1,1,1,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,1,0,0],#27 Reconocimiento
                            [0,1,0,1,1,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0],#28 Desenmascaramiento
                            [0,0,0,1,0,1,0,0,0,0,1,1,0,1,1,0,0,0,1,0,1,1,0,0,0,0,0,1,0,0,1,0],#29 Transfiguracion
                            [1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0],#30 Castigo
                            [1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0]]#31 Boda
#                            0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1                                           



'''
Alejamiento, 0
Prohibicion, 1
Transgresion,2
Conocimiento,3
Informacion,4
Engano,5
Trickery,6
Complicidad,RelacionesEntreFunciones[fid][c]
Fechoria,8
Mediacion,9
Recompensa,10
Aceptacion,11
Partida,12
Prueba,13
Reaccion,14
Regalo,15
Viaje,16
Lucha,1RelacionesEntreFunciones[fid][c]
Marca,18
Victoria,19
Enmienda,20
Regreso,21
Persecucion,22
Socorro,23
Fingimiento,24
Tareadificil,25
Cumplimiento,26
Reconocimiento,2RelacionesEntreFunciones[fid][c]
Desenmascaramiento,28
Transfiguracion,29
Castigo,30
Boda,31
'''

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
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Aleja de Lugar")
    fid = 0
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] != 0):
            if(random.randrange(11) < RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Prohibicion(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Prohibicion de X a " + a2.nombre)
    fid = 1
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Transgresion(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Transgrede a " + a2.nombre)
    fid = 2
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Conocimiento(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " adquiere Conocimiento")
    fid = 3
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a1,a2)
        
def Informacion(a1,a2):
    if(random.randrange(10) > 8):
                return
    print("Informacion sobre X")
    fid = 4
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a1,a2)
        
def Engano(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Engana a " + a2.nombre)
    fid = 5
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)

def Trickery(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Trick a " + a2.nombre)
    fid = 6
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)

def Complicidad(a1,a2):
    if(random.randrange(10) > 8):
                return

    num = random.randrange(7)
    while(num == a1.pid):
        num = random.randrange(7)
    print(actores[num].nombre + " tiene Complicidad con " + a1.nombre)
    fid = 7
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,actores[num])
     
def Fechoria(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Fechoria a " + a2.nombre)
    fid = 8
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)

def Mediacion(a1,a2):
    if(random.randrange(10) > 8):
                return
    num = random.randrange(7)
    while(num == a2.pid):
        num = random.randrange(7)
    print(actores[num].nombre + " Mediacion con " + a2.nombre)
    fid = 9
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,actores[num])
        
def Recompensa(a1,a2):
    if(random.randrange(10) > 8):
                return
    fid = 10
    num = random.randrange(7)
    while(num == a2.pid):
        num = random.randrange(7)
    print(actores[num].nombre + " Recompensa a " + a2.nombre)
    
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Aceptacion(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Acepta")
    fid = 11
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Partida(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Parte hacia Lugar")
    fid = 12
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Prueba(a1,a2):
    if(random.randrange(10) > 8):
                return
    fid = 13
    num = random.randrange(7)
    while(num == a2.pid):
        num = random.randrange(7)
    print(actores[num].nombre + " Prueba a " + a2.nombre)
    
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,actores[num])
        
def Reaccion(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Reacciona")
    fid = 14
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Regalo(a1,a2):
    if(random.randrange(10) > 8):
                return
    fid = 15
    num = random.randrange(7)
    while(num == a2.pid):
        num = random.randrange(7)
    print(actores[num].nombre + " Regala Objeto a " + a2.nombre)
    
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Viaje(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Viaja a Lugar")
    fid = 16
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Lucha(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Lucha contra " + a2.nombre)
    fid = 17
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Marca(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a2.nombre + " afecta mentalmente a " + a1.nombre)
    fid = 18
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a1,a2)
        
def Victoria(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a2.nombre + " tiene la Victoria")
    fid = 19
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Enmienda(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " se arregla con " + a2.nombre)
    fid = 20
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a1,a2)
        
def Regreso(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Regresa a Lugar")
    fid = 21
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Persecucion(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Persigue a " + a2.nombre)
    fid = 22
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Socorro(a1,a2):
    if(random.randrange(10) > 8):
                return
    fid = 23
    num = random.randrange(7)
    while(num == a2.pid):
        num = random.randrange(7)
    print(a2.nombre + " Ayuda a " + actores[num].nombre)
    
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](actores[num],a2)
            
def Fingimiento(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Finge frente a " + a2.nombre)
    fid = 24
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Tareadificil(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " lleva a cabo Tarea dificil")
    fid = 25
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a1,a2)
        
def Cumplimiento(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Cumple con su acometido")
    fid = 26
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a1,a2)
        
def Reconocimiento(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Reconoce la verdadera forma de " + a2.nombre)
    fid = 27
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Desenmascaramiento(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Desenmascara a " + a2.nombre)
    fid = 28
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Transfiguracion(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " se Transfigura en Algo")
    fid = 29
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a1,a2)
        
def Castigo(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Castiga a " + a2.nombre)
    fid = 30
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)
        
def Boda(a1,a2):
    if(random.randrange(10) > 8):
                return
    print(a1.nombre + " Boda con " + a2.nombre)
    
    fid = 31
    c = random.randrange(32)
    while(1):
        c = c + 1
        c = c % 32
        
        if(RelacionesEntreFunciones[fid][c] == 1):
            if(random.randrange(10) > RelacionesEntreFunciones[fid][c]):
                return funciones[c](a2,a1)

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
actores[3] = actor(0,3,0,"Donante",[1,1,1,1,1,1,1])
actores[4] = actor(0,4,0,"Auxiliar",[1,1,1,1,1,1,1])
actores[5] = actor(0,5,0,"Agresor",[1,1,1,1,1,1,1])
actores[6] = actor(0,6,0,"Ordenante",[1,1,1,1,1,1,1])

Inicio()



