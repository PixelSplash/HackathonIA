import random

funciones = ""

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
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Prohibicion(a1,a2):
    print(a1.nombre + " Prohibicion " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Transgresion(a1,a2):
    print(a1.nombre + " Transgresion " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Conocimiento(a1,a2):
    print(a1.nombre + " Conocimiento " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Informacion(a1,a2):
    print(a1.nombre + " Informacion " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Engano(a1,a2):
    print(a1.nombre + " Engano " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Complicidad(a1,a2):
    print(a1.nombre + " Complicidad " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Fechoria(a1,a2):
    print(a1.nombre + " Fechoria " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Mediacion(a1,a2):
    print(a1.nombre + " Mediacion " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Aceptacion(a1,a2):
    print(a1.nombre + " Aceptacion " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Partida(a1,a2):
    print(a1.nombre + " Partida " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Prueba(a1,a2):
    print(a1.nombre + " Prueba " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Reaccionheroe(a1,a2):
    print(a1.nombre + " Reaccionheroe " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Regalo(a1,a2):
    print(a1.nombre + " Regalo " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Viaje(a1,a2):
    print(a1.nombre + " Viaje " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Lucha(a1,a2):
    print(a1.nombre + " Lucha " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Marca(a1,a2):
    print(a1.nombre + " Marca " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Victoria(a1,a2):
    print(a1.nombre + " Victoria " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Enmienda(a1,a2):
    print(a1.nombre + " Enmienda " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Regreso(a1,a2):
    print(a1.nombre + " Regreso " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Persecucion(a1,a2):
    print(a1.nombre + " Persecucion " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Socorro(a1,a2):
    print(a1.nombre + " Socorro " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Regresoincognito(a1,a2):
    print(a1.nombre + " Regresoincognito " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Fingimiento(a1,a2):
    print(a1.nombre + " Fingimiento " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Tareadificil(a1,a2):
    print(a1.nombre + " Tareadificil " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Cumplimiento(a1,a2):
    print(a1.nombre + " Cumplimiento " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Reconocimiento(a1,a2):
    print(a1.nombre + " Reconocimiento " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Desenmascaramiento(a1,a2):
    print(a1.nombre + " Desenmascaramiento " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Transfiguracion(a1,a2):
    print(a1.nombre + " Transfiguracion " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Castigo(a1,a2):
    print(a1.nombre + " Castigo " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])
        
def Boda(a1,a2):
    print(a1.nombre + " Boda " + a2.nombre)
    if(random.randrange(10) > 3):
        funciones[random.randrange(31)](a2,actores[random.randrange(7)])

funciones = [Alejamiento,Prohibicion,Transgresion,Conocimiento,Informacion,Engano,Complicidad,Fechoria,Mediacion,Aceptacion,Partida,Prueba,Reaccionheroe,Regalo,Viaje,Lucha,Marca,Victoria,Enmienda,Regreso,Persecucion,Socorro,Regresoincognito,Fingimiento,Tareadificil,Cumplimiento,Reconocimiento,Desenmascaramiento,Transfiguracion,Castigo,Boda]

actores = [0,0,0,0,0,0,0]

actores[0] = actor(0,0,0,"Heroe",[0,0,0,0,0,0,0])
actores[1] = actor(0,0,0,"Villano",[0,0,0,0,0,0,0])
actores[2] = actor(0,0,0,"Princesa",[0,0,0,0,0,0,0])
actores[3] = actor(0,0,0,"Donante",[0,0,0,0,0,0,0])
actores[4] = actor(0,0,0,"Auxiliar",[0,0,0,0,0,0,0])
actores[5] = actor(0,0,0,"Agresor",[0,0,0,0,0,0,0])
actores[6] = actor(0,0,0,"Ordenante",[0,0,0,0,0,0,0])

funciones[random.randrange(31)](actores[0],actores[1])



