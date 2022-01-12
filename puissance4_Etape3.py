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


from outilsp4_Etape3 import*

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
        colonne,bomb = quelleCol(N,players[n],grille,taille)
        if bomb == 1:
            Bombe(colonne,grille,N,taille)
            players[n][2] = 0
            print("Attention la bombe est envoyé, il ne vous en reste plus")
        else:
            joue(players[n],colonne,grille,taille)
    else:
        colonne,bomb = quelleCol_IA(N,grille,taille,players[n])
        if bomb == 1 :
            Bombe(colonne,grille,N,taille)
            players[n][2] = 0
            print("\nL'ordinateur {} a joué une maxi bombe sur la colonne {}\n".format(players[n][0],colonne))
        else:
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
    
    
    
        
        
    
        