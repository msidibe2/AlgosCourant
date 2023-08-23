# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:25:34 2020
 
@author: moussa
"""
"""
#algo
Fonction nombreDeChiffre(L:liste de chiffres(nombre)): entier
  //i = 1
  //precondition: nombre positif et  liste non vide 
  
 Si est_vide(Queue(L)) alors 
     renvoyer i
 Sinon
    i+= 1
    L:= Queue(L)
   renvoyer i
"""

# code de l'algo
def nombreDeChiffre():
    print("Entrez un nombre positif :")
    nombre = input("nombre = ")
    i = len(str(nombre))
    print("ce nombre comprend", i ,"chiffres")
nombreDeChiffre()
