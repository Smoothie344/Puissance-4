# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 09:39:50 2021

@author: smoot
"""

#Etudiants :
    #Coralie Vernay
    #Chloé Jaunain
    #Ronan Loizeau
    #Paul Croizet


from outilsp4 import*

Caract=["A","B","C","D","E","F","G"]
print("\nBienvenue au Puissance 4 ! (de la mort qui tue) \n")
joueur = 1
grille = newG()
vict = False
while vict == False:
    affiche(grille)
    print("\njoueur {} à vous de jouer !".format(joueur),end="")
    colonne = quelleCol(joueur,grille)
    joue(joueur,colonne,grille)
    vict,gagnant = victoire(grille)
    if vict == True:
        if gagnant != 0:
            print("Le joueur {} a gagné, félicitations !".format(gagnant))
        else:
            affiche(grille)
            print("\nMatch nul")
    if joueur == 1 :
        joueur = 2
    else:
       joueur = 1
    
    
    
        
        
    
        