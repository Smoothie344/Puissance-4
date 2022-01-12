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
    


#choix_taille
def choix_taille():
    G = [str(n) for n in range(3,27)]
    VerifC = False
    while VerifC == False:
        C = input("Choisir un nombre de colonnes entre 3 et 26 : ")
        if C in G:
            C = int(C)
            VerifC = True
        else:
            print("Nombre de Colonnes pas valide")
    VerifR = False
    while VerifR == False:
        R = input("Choisir un nombre de rangées entre 3 et 26 : ")
        if R in G:
            R = int(R)
            VerifR = True
        else:
            print("Nombre de Rangées pas valide")
    return [C,R]

#choix_N:
def choix_N(taille):
    G = [str(n) for n in range (1,27)]
    VerifN = False
    while VerifN == False:
        N = input("En combien de coups voulez vous gagner ? :")
        if N in G :
            N = int(N)
            if N <= min(taille[0],taille[1]):
                return N
        else:
            print("Valeur pas valide")
            
        
        

#affiche
def affiche(grille,taille):
    Caract=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print("  " + taille[0]*"- " + " ")
    for i in range(taille[1]):
        print("|", end=" ")
        for k in range((taille[0]*taille[1] - taille[0])-i*taille[0],taille[0]*taille[1]-i*taille[0]):
            print(grille[k], end=" ")
        print("|")
    print("  " + taille[0]*"- " + " ")
    print("  ",end="")
    for i in range(taille[0]):
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
    Caract=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    x = Caract.index(colonne.upper())
    return x

#coord2to1
def coord1to2(N,taille):
    y = 0
    x = N 
    while x > taille[1]:
        x = x-taille[0]
        y = y+1
    return x,y

#coord2to1
def coord2to1(x,y,taille):
    return x+y*taille[0]

#newG
def newG(taille):
    return [" " for n in range(taille[0]*taille[1])]


#hauteur
def hauteur(c,grille,taille):
    x=val(c)
    a = 0
    for i in range(taille[1]):
        if grille[coord2to1(x,i,taille)] != " ":
            a = a + 1
    return a

#posepion
def posepion(j,N,grille):
    grille[N]=pion(j)

#joue
def joue(j,c,grille,taille):
    posepion(j,hauteur(c,grille,taille)*taille[0]+val(c),grille)

#col
def col(N,grille,taille):
    L=[]
    for k in range(0,taille[0]):
        for u in range(0,taille[1]-N+1):
                L.append("".join(grille[k+taille[0]*(i+u)] for i in range(N)))
    return L        

#row
def row(N,grille,taille):
    L=[]
    for i in range(taille[1]):
        for k in range(N):
            L.append("".join(grille[i*taille[0]+k:i*taille[0]+(N)+k]))
    return L

#diag
def diag(N,grille,taille):
    L=[]
    for k in range (N-1):
        for i in range (taille[0]*(taille[1]-1)-taille[0]*k,(taille[0]*taille[1]-(N-1))-taille[0]*k):
            L.append("".join(grille[i-taille[1]*j] for j in range (N)))
    for k in range (N-1):
        for i in range (taille[0]*(taille[1]-1)+(N-1)-taille[0]*k,taille[0]*taille[1]-taille[0]*k):
            L.append("".join(grille[i-taille[1]*j] for j in range (N)))
    return L

#quelleCol
def quelleCol(N,joueur,grille,taille):
    Caract=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    Caract_N =[]
    for i in range(N):
        Caract_N.append(Caract[i])
    while True:
        colonne = input("Joueur {} Dans quelle colonne jouez vous ? ".format(joueur))
        print("\n")
        colonne = colonne.upper()
        if colonne in Caract_N :
            if hauteur(colonne,grille,taille) < taille[1]:
                return colonne
            else:
                print("Vous ne pouvez pas jouez dans cette colonne")
        else:
            print("Vous ne pouvez pas jouez dans cette colonne car cette colonne n'existe pas")


   

   
#victoire
def victoire(N,grille,taille):
    L = col(N,grille,taille) + diag(N,grille,taille) + row (N,grille,taille)
    if 'X'*N in L :
        return True,1
    elif 'O'*N in L :
        return True,2
    elif " " not in grille:
        return True,0
    else:
        return False,0
    
#test des fonctions 


if __name__ == "__main__":
    
    G=["X","O","O","O","X","X"," "," ","O","X","X","O"," "," "," "," ","X","O","X"," "," "," "," ","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    

    #test de newG :
    print("\n")
    grille=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    print('Test de newG(taille) avec [7,6] , attendu : {}'.format(grille))
    valeur = newG([7,6])
    print('newG([7,6]) = {} : '.format(valeur),end="")
    if valeur == grille:
        print("OK")
    else:
        print("NOK") 

  #test de la fonction val :
    
    print("\n")   
    print('Test de val(colonne) avec y : valeur attendu : 24 ')
    valeur = val("y")
    print("val('y') = {} : ".format(valeur),end="")
    if valeur == 24 :
        print("OK")
    else :
        print("NOK")

    #test de la fonction coord1to2:
   
    print("\n")
    print('Test de coord1to2(N,taille) avec 34 et [7,6], : valeur attendu : (6,4) ')
    valeur = coord1to2(34,[7,6])
    print("coord1to2(34,[7,6]) = {} : ".format(valeur),end="")
    if valeur == (6,4) :
        print("OK")
    else :
        print("NOK")
  
    #test de la fonction coord2to1:
    
    print("\n")
    print('Test de coord2to1(x,y,taille) avec 4, 3 et [7,6]: valeur attendu : 25 ')
    valeur = coord2to1(4,3,[7,6])
    print("coord2to1(4,3,[7,6]) = {} : ".format(valeur),end="")
    if valeur == 25 :
        print("OK")
    else :
        print("NOK")  
      
    #test de la fonction hauteur :
    
    print("\n")   
    print('Test de hauteur(c,grille,taille) avec c, G et [7,6] : valeur attendu : 4 ')
    valeur = hauteur("c",G,[7,6])
    print("hauteur('c',G,[7,6]) = {} : ".format(valeur),end="")
    if valeur == 4 :
        print("OK")
    else :
        print("NOK")
        
    
    
    #test de la fonction pion : 
    
    print("\n")
    print('Test de la fonction pion(joueur) avec 1, attendu : X')
    valeur = pion(1)
    print('pion(1) = {} : '.format(valeur),end="")
    if valeur == "X":
        print("OK")
    else:
        print("NOK")
    
    
    #test de la fonction joueur :
    
    print("\n")
    print('Test de la fonction joueur(pion) avec "O", attendu : 2')
    valeur = joueur("O")
    print('joueur("O") = {} : '.format(valeur),end="")
    if valeur == 2:
        print("OK")
    else:
        print("NOK")
    
    
    #test de la fonction col :
    
    print("\n")
    colonnes=['X   ', '    ', '    ', 'OO  ', 'O   ', '    ', 'OXXO', 'XXO ', 'XO  ', 'OXO ', 'XO  ', 'O   ', 'XOX ', 'OX  ', 'X   ', 'X   ', '    ', '    ', '    ', '    ', '    ']
    print('Test de la fonction col(N,grille,taille) avec 4, G et [7,6], attendu : {}'.format(colonnes))
    valeur = col(4,G,[7,6])
    print('col(4,G,[7,6]) = {} : '.format(valeur),end="")
    if valeur == colonnes:
        print("OK")
    else:
        print("NOK")  
    

    #test de la fonction row :
    
    print("\n")
    lignes=['XOOO', 'OOOX', 'OOXX', 'OXX ', ' OXX', 'OXXO', 'XXO ', 'XO  ', '  XO', ' XOX', 'XOX ', 'OX  ', '  O ', ' O  ', 'O   ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ', '    ']
    print('Test de la fonction row(N,grille,taille) avec 4, G et [7,6], attendu : {}'.format(lignes))
    valeur = row(4,G,[7,6])
    print('row(4,G,[7,6]) = {} : '.format(valeur),end="")
    if valeur == lignes:
        print("OK")
    else:
        print("NOK") 
    
    
    #test de la fonction diag : 
    
    print("\n")
    diagonales=['  OO', '   X', '    ', '    ', '  XX', ' OOO', '  X ', '    ', '  XO', ' XXX', 'OOOX', ' X  ', '    ', '    ', '    ', '   O', '    ', '    ', '    ', '   X', ' X  ', '    ', '   O', '   X']
    print('Test de la fonction diag(N,grille,taille) avec 4, G et [7,6], attendu : {}'.format(diagonales))
    valeur = diag(4,G,[7,6])
    print('diag(4,G,[7,6]) = {} : '.format(valeur),end="")
    if valeur == diagonales:
        print("OK")
    else:
        print("NOK") 
        
    #test de la fonction victoire :
        
    print('\n')
    print('Test de la fonction victoire avec 4, G et [7,6], résultat attendu : False,O')
    v1,v2 = victoire(4,G,[7,6])
    print('victoire(4,G,[7,6]) = {} : '.format(valeur),end="")
    if v1 == False and v2 == 0 :
        print('OK')
    else:
        print('NOK')



