import random

funciones = ""

'''
Alejamiento, 0
Prohibicion, 1
Transgresion,2
Conocimiento,3
Informacion,4
Engano,5
Trickery,6
Complicidad,7
Fechoria,8
Mediacion,9
Recompensa,10
Aceptacion,11
Partida,12
Prueba,13
Reaccion,14
Regalo,15
Viaje,16
Lucha,17
Marca,18
Victoria,19
Enmienda,20
Regreso,21
Persecucion,22
Socorro,23
Fingimiento,24
Tareadificil,25
Cumplimiento,26
Reconocimiento,27
Desenmascaramiento,28
Transfiguracion,29
Castigo,30
Boda,31
'''
#                            0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1                                           
RelacionesEntreFunciones = [[0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],#0
                            [1,0,1,0,0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0],#1
                            [1,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,0,0,0,0,0,1,0],#2
                            [1,1,0,0,0,1,1,0,0,0,1,1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0],#3
                            [1,0,0,1,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,0,1,0,0,0,0],#4
                            [1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1],#5
                            [0,0,1,0,1,1,0,1,1,0,0,1,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,1,0,1,0],#6
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#7
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#8
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#9
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#10
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#11
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#12
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#13
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#14
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#15
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#16
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#17
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#18
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#19
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#20
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#21
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#22
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#23
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#24
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#25
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#26
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#27
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#28
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#29
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#30
                            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]#31

#                            0 1 2 3 4 5 6                                           
RelacionesEntreActores =   [[0,0,0,0,0,0,0],#0
                            [0,0,0,0,0,0,0],#1
                            [0,0,0,0,0,0,0],#2
                            [0,0,0,0,0,0,0],#3
                            [0,0,0,0,0,0,0],#4
                            [0,0,0,0,0,0,0],#5
                            [0,0,0,0,0,0,0],#6
                            [0,0,0,0,0,0,0],#7
                            [0,0,0,0,0,0,0],#8
                            [0,0,0,0,0,0,0],#9
                            [0,0,0,0,0,0,0],#10
                            [0,0,0,0,0,0,0],#11
                            [0,0,0,0,0,0,0],#12
                            [0,0,0,0,0,0,0],#13
                            [0,0,0,0,0,0,0],#14
                            [0,0,0,0,0,0,0],#15
                            [0,0,0,0,0,0,0],#16
                            [0,0,0,0,0,0,0],#17
                            [0,0,0,0,0,0,0],#18
                            [0,0,0,0,0,0,0],#19
                            [0,0,0,0,0,0,0],#20
                            [0,0,0,0,0,0,0],#21
                            [0,0,0,0,0,0,0],#22
                            [0,0,0,0,0,0,0],#23
                            [0,0,0,0,0,0,0],#24
                            [0,0,0,0,0,0,0],#25
                            [0,0,0,0,0,0,0],#26
                            [0,0,0,0,0,0,0],#27
                            [0,0,0,0,0,0,0],#28
                            [0,0,0,0,0,0,0],#29
                            [0,0,0,0,0,0,0],#30
                            [0,0,0,0,0,0,0]]#31

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
    print(a1.nombre + " Alejamiento " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Prohibicion(a1,a2):
    print(a1.nombre + " Prohibicion " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Transgresion(a1,a2):
    print(a1.nombre + " Transgresion " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Conocimiento(a1,a2):
    print(a1.nombre + " Conocimiento " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Informacion(a1,a2):
    print(a1.nombre + " Informacion " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Engano(a1,a2):
    print(a1.nombre + " Engano " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])

def Trickery(a1,a2):
    print(a1.nombre + " Trickery " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])

def Complicidad(a1,a2):
    print(a1.nombre + " Complicidad " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
     
def Fechoria(a1,a2):
    print(a1.nombre + " Fechoria " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])

def Mediacion(a1,a2):
    print(a1.nombre + " Mediacion " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Recompensa(a1,a2):
    print(a1.nombre + " Recompensa " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Aceptacion(a1,a2):
    print(a1.nombre + " Aceptacion " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Partida(a1,a2):
    print(a1.nombre + " Partida " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Prueba(a1,a2):
    print(a1.nombre + " Prueba " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Reaccion(a1,a2):
    print(a1.nombre + " Reaccionheroe " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Regalo(a1,a2):
    print(a1.nombre + " Regalo " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Viaje(a1,a2):
    print(a1.nombre + " Viaje " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Lucha(a1,a2):
    print(a1.nombre + " Lucha " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Marca(a1,a2):
    print(a1.nombre + " Marca " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Victoria(a1,a2):
    print(a1.nombre + " Victoria " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Enmienda(a1,a2):
    print(a1.nombre + " Enmienda " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Regreso(a1,a2):
    print(a1.nombre + " Regreso " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Persecucion(a1,a2):
    print(a1.nombre + " Persecucion " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Socorro(a1,a2):
    print(a1.nombre + " Socorro " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
            
def Fingimiento(a1,a2):
    print(a1.nombre + " Fingimiento " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Tareadificil(a1,a2):
    print(a1.nombre + " Tareadificil " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Cumplimiento(a1,a2):
    print(a1.nombre + " Cumplimiento " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Reconocimiento(a1,a2):
    print(a1.nombre + " Reconocimiento " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Desenmascaramiento(a1,a2):
    print(a1.nombre + " Desenmascaramiento " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Transfiguracion(a1,a2):
    print(a1.nombre + " Transfiguracion " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Castigo(a1,a2):
    print(a1.nombre + " Castigo " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])
        
def Boda(a1,a2):
    print(a1.nombre + " Boda " + a2.nombre)
    if(random.randrange(10) > 1):
        funciones[random.randrange(32)](a2,actores[random.randrange(7)])

def Inicio():
    num = random.randrange(4)
    if(num == 0):
        funciones[0](actores[0],actores[random.randrange(7)])
    elif(num == 1):
        funciones[2](actores[0],actores[random.randrange(7)])
    elif(num == 2):
        funciones[5](actores[0],actores[random.randrange(7)])
    else:
        funciones[14](actores[0],actores[random.randrange(7)])
        
funciones = [Alejamiento,Prohibicion,Transgresion,Conocimiento,Informacion,Engano,Trickery,Complicidad,Fechoria,Mediacion,Recompensa,Aceptacion,Partida,Prueba,Reaccion,Regalo,Viaje,Lucha,Marca,Victoria,Enmienda,Regreso,Persecucion,Socorro,Fingimiento,Tareadificil,Cumplimiento,Reconocimiento,Desenmascaramiento,Transfiguracion,Castigo,Boda]
actores = [0,0,0,0,0,0,0]

actores[0] = actor(0,0,0,"Heroe",[1,1,1,1,1,1,1])
actores[1] = actor(0,0,0,"Villano",[1,1,1,1,1,1,1])
actores[2] = actor(0,0,0,"Princesa",[1,1,1,1,1,1,1])
actores[3] = actor(0,0,0,"Donante",[1,1,1,1,1,1,1])
actores[4] = actor(0,0,0,"Auxiliar",[1,1,1,1,1,1,1])
actores[5] = actor(0,0,0,"Agresor",[1,1,1,1,1,1,1])
actores[6] = actor(0,0,0,"Ordenante",[1,1,1,1,1,1,1])

Inicio()



