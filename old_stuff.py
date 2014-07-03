__author__ = 'Paola'

from random import randint as rnd
from time import sleep as sleep
Jardin=[]

def generarNombres():
    silabas = ['pan','chon','je','men','ti','ca','se']
    nombre = ''
    for x in range(0,rnd(2,4)):
        nombre = nombre + silabas[rnd(0,len(silabas)-1)]

    return nombre

def calcularSol():
    sol = False
    so_random = rnd(1,10)
    if so_random % 2 == 0:
        sol = True

    return sol

def calcularLLuvia():
    lluvia = False
    so_random = rnd(1,10)
    if so_random % 2 == 0:
        lluvia = True
    return lluvia

class Planta():
    def __init__(self,nombre):
        self.vida = rnd(1,3)
        self.edad = 0
        self.crecimiento = 0
        self.nombre = nombre
        self.fertil = True
        print 'HA NACIDO', self.nombre

    def reproducirse(self):
        Jardin.append(Planta(self.nombre + 'jr'))
        self.fertil = False

    def darSolecito(self,sol):
        if sol:
            self.crecimiento += 1

    def darLLuvia(self,lluvia):
        if lluvia:
            self.vida += 1
        else:
            self.vida -= 1

    def avanzarEdad(self):
        if self.vida > 0:
            self.edad += 1
            if self.crecimiento > 5 and self.fertil:
                self.reproducirse()
            return True
        else:
            return False


def generarJardin(cantidad):
    for x in range(0,cantidad):
        Jardin.append(Planta(generarNombres()))


generarJardin(4)
def simularDia():
    for x in Jardin:
        x.darLLuvia(calcularLLuvia())
        x.darSolecito(calcularSol())
        if x.avanzarEdad():
            print x.nombre, x.crecimiento, x.vida
        else:
            print 'RIP',x.nombre

            Jardin.remove(x)
    sleep(1)


while True:
    simularDia()