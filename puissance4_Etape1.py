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


from outilsp4_Etape1 import*

Caract=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("\nBienvenue au Puissance 4 ! (de la mort qui tue) \n")
taille = choix_taille()
N = choix_N(taille)
joueur = 1
grille = newG(taille)
vict = False
while vict == False:
    affiche(grille,taille)
    print("\njoueur {} à vous de jouer !".format(joueur),end="")
    colonne = quelleCol(N,joueur,grille,taille)
    joue(joueur,colonne,grille,taille)
    vict,gagnant = victoire(N,grille,taille)
    if vict == True:
        if gagnant != 0:
            print("Le joueur {} a gagné, félicitations !".format(gagnant))
        else:
            affiche(grille,taille)
            print("\nMatch nul")
    if joueur == 1 :
        joueur = 2
    else:
       joueur = 1
    
    
    
        
        
    
        