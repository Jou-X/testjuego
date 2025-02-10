import pygame
import time
import random
import sys
import csv
import os
import math



daño = 5
vida = 100
armadura = 0
defensa = 0



# la d significa duravilidad

dbotascuero = 4
dpetocuero = 4
dpantaloneracuero = 4
dcasco = 4


def equipar_arma():

    global daño
    equipar = inventario_armas()

    if equipar == "cuchillo":

        cuchillo = 5
        daño = daño + cuchillo
        print("+5 daño")
        return daño
    
    if equipar == "espada":

        espada = 20
        daño = daño + espada
        print("+20 daño")
        return daño
    
def equipar_armadura():
    global defensa
    equipar = inventario_armaduras()

    if equipar == "botas_cuero":

        botas_cuero = 3
        defensa = defensa + botas_cuero
        print("+3 defensa")
        return defensa
    
    if equipar == "guantes_cuero":
        guantes_cuero = 2
        defensa = defensa + guantes_cuero
        print("+2 defensa")
        return defensa

inventario = {
    
    "inventario_comida" : {
        "pan" : 1,
        "chocolate" : 2,
        "golden apple" : 2,
    },

    "inventario_armas" : {
        "cuchillo" : 1,
        "espada" : 0,
    },

    "inventario_armaduras" : {
        "botas_cuero" : 0,
        "guantes_cuero" : 0,
    }
}


def abrir_inventario():
    print()

    while True:

        tipo_inventario = input("¿Qúe buscas?. 1- Comida 2- Armas 3- Armaduras 4- Cerrar Inventario: ").lower()

        if tipo_inventario == '1':
            curar()
            break
        if tipo_inventario == '2':
            equipar_arma()
            break
        if tipo_inventario == '3':
            equipar_armadura()
            break
        if tipo_inventario == '4':
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

def inventario_armaduras():
    while True:
        print("Pulsa 'e' cuando quieras salir.")
        item = input(f"Tu inventario es {inventario['inventario_armaduras']}. ¿Qué te gustaría equipar?: ")

        if item == 'e':
            print("Saliendo del inventario...")
            break

        print()
        if item in inventario['inventario_armaduras']:
                
            if inventario['inventario_armaduras'][item] ==0:
                print(f"Aún no has encontrado eso.")
                return 0

            elif inventario['inventario_armaduras'][item] ==1:  
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

vida_m_1 = 50
vida_m_2 = 60

def mob_1():
    global vida, vida_m_1
    daño_m_1 = 4

    if vida <= 0:
        print("Has muerto")
        quit()

    vida -= daño_m_1
    print(f"Has recibido {daño_m_1} DPS. Tu vida es {vida}")

def mob_2():
    global vida, vida_m_2
    daño_m_2 = 6 

    if vida <= 0:
        print("Has muerto")
        quit()
    

    vida -= daño_m_2
    print(f"Has recibido {daño_m_2} DPS. Tu vida es {vida}")

def personaje(mob):
    global daño

    if mob == mob_1:
        global vida_m_1
        vida_m_1 -= daño
        print(f"Daño hecho: {daño}. Vida de M1: {vida_m_1}")
        if vida_m_1 <= 0:
            print("Mataste a M1.")

    elif mob == mob_2:
        global vida_m_2
        vida_m_2 -= daño
        print(f"Daño hecho: {daño}. Vida de M2: {vida_m_2}")
        if vida_m_2 <= 0:
            print("Mataste a M2.")

def pelea(mob):
    global vida, vida_m_1, vida_m_2

    while True:
        if vida <= 0 or (mob == mob_1 and vida_m_1 <= 0) or (mob == mob_2 and vida_m_2 <= 0):
            break

        mob() 
        personaje(mob) 


mobs = {
    'mob1': mob_1,
    'mob2': mob_2
}






def habitacion_1():
    global inventario
    while True:
        inventario = inventario['inventario_armaduras']
        print(f"Encontraste {inventario[inventario_armaduras][item]}")
        pelea(mobs['mob1'])
        




# hacer defensa en ataques
def defensa(enemigo):
    global defensa
    if enemigo == mob_1 or mob_2:
        daño = daño - defensa
        poco02(f"tu armadura te ha defendido {defensa} puntos de daño")

    dcasco -= 1
    dpetocuero -= 1
    dpantaloneracuero -= 1

    dbotascuero -= 1

    if dcasco == 0:
        poco03("Tu casco se ha roto")
        casco = 0
            
    elif dbotascuero == 0:
        poco03("Tus botas se ha roto")
        botas_cuero = 0
            
    elif dpetocuero == 0:
        poco03("Tu peto se ha roto")
        peto_cuero = 0
            
    elif dpantaloneracuero == 0:
        poco03("Tus pantalones se ha roto")
        pantalonera_cuero = 0


    
            





def poco1(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.1)
    print()
    


def poco2(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.2)
    print()



def poco3(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.4)
    print()


def poco01(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.08)
    print()



def poco02(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.06)
    print()
    return input()




def poco03(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.04)
    print()







nombres = random.choice(["Misco Jones","Gilito Mcpato","n+i+g+g+a"])





def intro():
    poco2("Hola,")
    poco01(f"me llamo {nombres}")
    poco03(f"tu inventario es: {inventario['inventario_comida']} {inventario['inventario_armas']} {inventario['inventario_armaduras']}")
    respuesta = poco02(f"¿Quieres abrir tu inventario?").lower()
    if respuesta == "si":
        abrir_inventario()
    else:
        poco02("Vale, entendido.")
        exit()

intro()

