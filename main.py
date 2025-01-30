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
    
    item = input(f"Tu inventario es {inventario}. ¿Qué te gustaria usar?")
    
    for item in inventario:
        
        if inventario[item] <=0:
            print(f"No te queda. Tienes {item}")

        elif inventario[item] >=1:
            inventario[item] -= 1
            print(inventario)
           
        elif item not in inventario:
            print("No tienes ese item")
            break
        
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





poco3("Bienvenido")
poco2("me llamo", nombres)