# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:43:48 2020

@author: moussa
"""

print("\n#Question 6\n")
def test_de_primalite(nombre):
    liste_premier = [2] 
    for i in range(3,nombre,2):
        liste_premier.append(i) 
    for i in liste_premier:
        for j in liste_premier:
            if(j%i==0 and i!=j): #le nombre admet un autre diviseur different de lui-meme
                liste_premier.remove(j)
    return liste_premier
nombre = int(input("Saisir la borne supérieure de l'intervalle dont vous sauhaitez lister les nombres premiers : ")) 
print(test_de_primalite(nombre))