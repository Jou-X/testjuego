import pygame
import time
import random
import sys
import csv
import os
import math


vida = 100
daño = 5

inventario = {
    
    "inventario_comida" : {
        "pan" : 1,
        "chocolate" : 2,
        "golden apple" : 2,
    },

    "inventario_armas" : {
        "cuchillo" : 1,
        "espada" : 0,
    }
}


def abrir_inventario():
    print()

    while True:

        tipo_inventario = input("¿Qúe buscas?. A- Comida B- Armas E- Cerrar Inventario: ").lower()

        if tipo_inventario == 'a':
            curar()
            break
        if tipo_inventario == 'b':
            inventario_armas()
            break
        if tipo_inventario == 'e':
            break
        else:
            print("Respuesta no válida.")
            continue

def inventario_comida():
    while True:
            print("Pulsa 'e' cuando quieras salir.")
            item = input(f"Tu inventario es {inventario['inventario_comida']}. ¿Qué te gustaría usar?: ")

            if item == 'e':
                print("Saliendo del inventario...")
                break

            print()
            if item in inventario['inventario_comida']:
                
                if inventario['inventario_comida'][item] <=0:
                    print(f"No te queda. Tienes {inventario['inventario_comida'][item]}")
                    return 0

                elif inventario['inventario_comida'][item] >=1:
                    inventario['inventario_comida'][item] -= 1
                    print(f"Has usado {item}")
                    return(item)
            else:
                print("No tienes ese objeto en tu inventario")
                continue
            break

def inventario_armas():
    while True:
        print("Pulsa 'e' cuando quieras salir.")
        item = input(f"Tu inventario es {inventario['inventario_armas']}. ¿Qué te gustaría equipar?: ")

        if item == 'e':
            print("Saliendo del inventario...")
            break

        print()
        if item in inventario['inventario_armas']:
                
            if inventario['inventario_armas'][item] ==0:
                print(f"Aún no has encontrado eso.")
                return 0

            elif inventario['inventario_armas'][item] ==1:  
                print(f"Has equipado {item}")
                return(item)
        else:
            print(f"{item} no existe.")
            continue
        
        if item == "e":
            print("Saliendo del inventario...")
            break


def curar():

    global vida

    cura = inventario_comida()
    
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

def vida_p(vida):
    vida = daño_mob()
    return vida
    


def daño_mob(daño_m):

    global vida

    if daño_m >=vida:
        print("Has muerto")
        quit()
    
    vida = vida - daño_m
    print(f"Has recibido {daño_m} de daño. Tu vida está a {vida}")
    return vida


daño_mob(2)


abrir_inventario()










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