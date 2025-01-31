import pygame
import time
import random
import sys
import csv
import os
import math

vida = 100

inventario = {
    "pan" : 1,
    "chocolate" : 2,
    "golden apple" : 2,
    "espada" : 1,
}

def abrir_inventario():
    
    item = input(f"Tu inventario es {inventario}. ¿Qué te gustaria usar?: ")
    
    if item in inventario:
        
        if inventario[item] <=0:
            print(f"No te queda. Tienes {inventario[item]}")


        elif inventario[item] >=1:
            inventario[item] -= 1
            print(f"Has usado {item}")
            return(item)
    else:
        print("No tienes ese objeto en tu inventario")
           
def curar():

    global vida
    cura = abrir_inventario()
    
    if cura == "pan":
        vida += 3
        print(f"Te has sanado +3. Ahora tienes {vida}")
        return vida
    if cura == "golden apple":
        vida += 50
        print(f"Te has sanado +50. Ahora tienes {vida}")
        return vida
    if cura == "chocolate":
        vida += 15
        print(f"Te has sanado +15. Ahora tienes {vida}")
        return vida

def daño_mob(daño):
    global vida
    if daño >=vida:
        print("Has muerto")
        return 0
    
    vida = vida - daño
    print(f"Tu vida está a {vida}")
    return vida
    
    

daño_mob(50)
print(vida)
vida = curar()
print(vida)
















def poco1(texto):
    for letra in texto:
        sys.stdunt.write(letra)
        sys.stdunt.flush()
        time.sleep(0.1)
    print()
    


def poco2(texto):
    for letra in texto:
        sys.stdunt.write(letra)
        sys.stdunt.flush()
        time.sleep(0.2)
    print()



def poco01(texto):
    for letra in texto:
        sys.stdunt.write(letra)
        sys.stdunt.flush()
        time.sleep(0.08)
    print()



def poco02(texto):
    for letra in texto:
        sys.stdunt.write(letra)
        sys.stdunt.flush()
        time.sleep(0.06)
    print()




def poco03(texto):
    for letra in texto:
        sys.stdunt.write(letra)
        sys.stdunt.flush()
        time.sleep(0.04)
    print()




def poco3(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.4)
    print()



nombres = random.choice(["Misco Jones","Gilito Mcpato","n+i+g+g+a"])





# poco3("Bienvenido")
# poco2("me llamo", nombres)