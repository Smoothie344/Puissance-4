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


from outilsp4_Etape2 import*

Caract=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("\nBienvenue au Puissance 4 ! (de la mort qui tue) \n")

#Création des différents paramètres du jeu
taille = choix_taille()
N = choix_N(taille)
ordi = nbr_ordi()
players = repartition(ordi)
grille = newG(taille)

n = 0
vict = False
while vict == False:
    affiche(grille,taille)
    if players[n][1] == "joueur":
        print("\njoueur {} à vous de jouer !".format(players[n][0]),end="")
        colonne = quelleCol(N,players[n],grille,taille)
        joue(players[n],colonne,grille,taille)
    else:
        colonne = quelleCol_IA(N,grille,taille,players[n])
        joue(players[n],colonne,grille,taille)
        print("\nL'ordinateur {} a joué sur la colonne {}\n".format(players[n][0],colonne))
        
    vict,gagnant = victoire(N,grille,taille)
    if vict == True:
        if gagnant != 0:
            print("\nLe {} {} a gagné, félicitations !\n".format(players[gagnant - 1][1],gagnant))
            affiche(grille,taille)
        else:
            affiche(grille,taille)
            print("\nMatch nul\n")
    if n == 0 :
        n = 1
    else:
       n = 0
    
    
    
        
        
    
        