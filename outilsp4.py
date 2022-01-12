# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 09:34:26 2021

@author: smoot
"""

#Etudiants :
    #Coralie Vernay
    #Chloé Jaunain
    #Ronan Loizeau
    #Paul Croizet

#affiche
def affiche(grille):
    Caract=["A","B","C","D","E","F","G"]
    print("  " + 7*"- " + " ")
    for i in range(6):
        print("|", end=" ")
        for k in range(35-i*7,42-i*7):
            print(grille[k], end=" ")
        print("|")
    print("  " + 7*"- " + " ")
    print("  ",end="")
    for i in range(len(Caract)):
        print(Caract[i],end=" ")
    print(" ")

#pion
def pion(joueur):
    if joueur==1:
        return "X"
    else:
        return "O"

#joueur
def joueur(pion):
    if pion=="X":
        return 1
    else:
        return 2

#val
def val(colonne):
    Caract=["A","B","C","D","E","F","G"]
    x = Caract.index(colonne.upper())
    return x

#coord2to1
def coord1to2(position_pion):
    y = 0
    x = position_pion
    while x > 6:
        x = x-7
        y = y+1
    return x,y

#coord2to1
def coord2to1(x,y):
    return x+y*7

#newG
def newG():
    return [" " for n in range(42)]


#hauteur
def hauteur(c,grille):
    x=val(c)
    a = 0
    for i in range(6):
        if grille[coord2to1(x,i)] != " ":
            a = a + 1
    return a

#posepion
def posepion(j,N,grille):
    grille[N]=pion(j)

#joue
def joue(j,c,grille):
    posepion(j,hauteur(c,grille)*7+val(c),grille)

#col
def col(grille):
    L=[]
    for k in range(0,7):
        for u in range(0,3):
            L.append("".join(grille[k+7*(i+u)] for i in range(0,4)))
    return L        

#row
def row(grille):
    L=[]
    for i in range(6):
        for k in range(4):
            L.append("".join(grille[i*7+k:i*7+4+k]))
    return L

#quelleCol
def quelleCol(joueur,grille):
    Caract=["A","B","C","D","E","F","G"]
    while True:
        colonne = input("Joueur {} Dans quelle colonne jouez vous ? ".format(joueur))
        print("\n")
        colonne = colonne.upper()
        if colonne in Caract :
            if hauteur(colonne,grille) < 6:
                return colonne
            else:
                print("Vous ne pouvez pas jouez dans cette colonne")
        else:
            print("Vous ne pouvez pas jouez dans cette colonne car cette colonne n'existe pas")


   
#diag
def diag(grille):
    L=[]
    for k in range (3):
        for i in range (35-7*k,39-7*k):
            L.append("".join(grille[i-6*j] for j in range (4)))
    for k in range (3):
        for i in range (38-7*k,42-7*k):
            L.append("".join(grille[i-8*j] for j in range (4)))
    return L
   
#victoire
def victoire(grille):
    L = col(grille) + diag(grille) + row (grille)
    if 'XXXX' in L :
        return True,1
    elif 'OOOO' in L :
        return True,2
    elif " " not in grille:
        return True,0
    else:
        return False,0
    
#test des fonctions 


if __name__ == "__main__":
    

    G=["X","O","O","O","X","X"," "," ","O","X","X","O"," "," ",
" "," ","X","O","X"," "," "," "," ","O"," "," "," "," ",
" "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    
    #test de la fonction val :
    
    print("\n")   
    print('Test de val(colonne) avec e : valeur attendu : 4 ')
    valeur = val("e")
    print("val('e') = {} : ".format(valeur),end="")
    if valeur == 4 :
        print("OK")
    else :
        print("NOK")

    #test de la fonction coord1to2:
    
    print("\n")
    print('Test de coord1to2 avec 34 : valeur attendu : (6,4) ')
    valeur = coord1to2(34)
    print("coord1to2(34) = {} : ".format(valeur),end="")
    if valeur == (6,4) :
        print("OK")
    else :
        print("NOK")
        
    #test de la fonction coord2to1:
    
    print("\n")
    print('Test de coord2to1 avec 4 et 3 : valeur attendu : 25 ')
    valeur = coord2to1(4,3)
    print("coord2to1(4,3) = {} : ".format(valeur),end="")
    if valeur == 25 :
        print("OK")
    else :
        print("NOK")  
      
    #test de la fonction hauteur :
    
    print("\n")   
    print('Test de hauteur avec c et G : valeur attendu : 4 ')
    valeur = hauteur("c",G)
    print("hauteur('c',G) = {} : ".format(valeur),end="")
    if valeur == 4 :
        print("OK")
    else :
        print("NOK")
        
    
    
    #test de la fonction pion : 
    
    print("\n")
    print('Test de la fonction pion avec 1, attendu : X')
    valeur = pion(1)
    print('pion(1) = {} : '.format(valeur),end="")
    if valeur == "X":
        print("OK")
    else:
        print("NOK")
    
    
    #test de la fonction joueur :
    
    print("\n")
    print('Test de la fonction joueur avec "O", attendu : 2')
    valeur = joueur("O")
    print('joueur("O") = {} : '.format(valeur),end="")
    if valeur == 2:
        print("OK")
    else:
        print("NOK")
    
    
    #test de la fonction col :
    
    print("\n")
    colonnes=['X   ', '    ', '    ', 'OO  ', 'O   ', '    ', 'OXXO', 'XXO ', 'XO  ', 'OXO ', 'XO  ', 'O   ', 'XOX ', 'OX  ', 'X   ', 'X   ', '    ', '    ', '    ', '    ', '    ']
    print('Test de la fonction col avec G, attendu : {}'.format(colonnes))
    valeur = col(G)
    print('col(G) = {} : '.format(valeur),end="")
    if valeur == colonnes:
        print("OK")
    else:
        print("NOK")  
    

    #test de la fonction row :
    
    print("\n")
    lignes=['XOOO', 'OOOX', 'OOXX', 'OXX ', ' OXX', 'OXXO', 'XXO ', 'XO  ', '  XO', ' XOX', 'XOX ', 'OX  ', '  O ', ' O  ', 'O   ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ']
    print('Test de la fonction row avec G, attendu : {}'.format(lignes))
    valeur = row(G)
    print('row(G) = {} : '.format(valeur),end="")
    if valeur == lignes:
        print("OK")
    else:
        print("NOK") 
    
    
    #test de la fonction diag : 
    
    print("\n")
    diagonales=['  OO', '   X', '    ', '    ', '  XX', ' OOO', '  X ', '    ', '  XO', ' XXX', 'OOOX', ' X  ', '    ', '  O ', '   X', '   O', ' O  ', '  XO', '  OX', '  XX', ' XOX', ' OXO', ' XXO', '  OO']
    print('Test de la fonction diag avec G, attendu : {}'.format(diagonales))
    valeur = diag(G)
    print('diag(G) = {} : '.format(valeur),end="")
    if valeur == diagonales:
        print("OK")
    else:
        print("NOK") 


