# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:00:02 2020

@author: moussa
"""
"""
print("\t#Algo:  ")

fonction hasard(nombreEntre, nombreMystere: entier): bool
  cpt = 0// pour compter le nombre d'essai
  Tant que cpt < 10
     entrez un nombre()
     si nombreEntrez  < nombreMystere alors afficher (entrer un nombre plus grand)
     sinon si nombreEntrez > nombreMystere alors afficher (entrer un nombre plus petit)
     sinon afficher (bravo! vous avez gagné)
  FinTant que
  Si cpt > 9
     afficher (vous n'avez pas gagné en 10 essais)
 """               
 

print("\n\t#code de l'algo: ")

import random
def mystere():
    nombre_mystere = random.randint(0,100) #  pour generer le nombre aleatoire entre 0 et 100 
    cpt=0 # variable qui compte le nombre d'essai
    
    while(cpt<10): 
        nombre_entre=int(input('Saisir un nombre entre 0 et 100 : ')) 
        cpt=1 
        if( nombre_entre < nombre_mystere):  
            print('{} est inferieur a la valeur proposee'.format( nombre_entre))  
        elif( nombre_entre > nombre_mystere):  
            print('{} est superieur à la valeur proposee'.format( nombre_entre)) #On affiche un message
        else:  
            print('Bravo ! le nombre mystere est {} '.format( nombre_entre))
            break
    else:
        print("\nVous avez depasser le nombre d'essai!") # quand l'utilisateur depasse le nombre d'essai
           
mystere()
