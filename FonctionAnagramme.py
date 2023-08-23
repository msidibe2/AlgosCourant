# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:00:01 2020

@author: moussa
"""

def anagramme(m1,m2):
    flag = False  
    for i in mot1: 
        if i in mot2: #si la lettre i est dans m2
            flag=True  
        else:
           flag=False  
    if(flag==True):     
        print("Ce sont des anagrammes")
    else:
        print("Ce ne sont pas des anagrammes")
mot1 = str(input("Saisir le premier mot : ")) 
mot2 = str(input("Saisir le second mot : ")) 

#mot1='anas'        
#mot2='sana' #sont des exemples d'anagrammes

anagramme(mot1,mot2)  
