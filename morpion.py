from fltk import *

taille = 300

plt = [[False, False, False],[False, False, False],[False, False, False]]
j1 = 'x'
j2 = 'o'
def affiche_plateau(plt):
    for i in range(len(plt)):
        k = 0
        for j in range(len(plt[i])):
            ligne(k, 0, k, taille, couleur ='red')
            ligne(0, k, taille, k, couleur ='red')
            k += taille//3
            mise_a_jour()

def pixelverscase(x, y):
    x = x//(taille//3)
    y = y//(taille//3)
    return x,y

def saisie(j, plt):
    x, y = attend_clic_gauche()
    a, b = pixelverscase(x, y)
    while(plt[a][b] != False):
        print("coordonée deja utilisé")
        x, y = attend_clic_gauche()
        a, b = pixelverscase(x, y)
    texte(a*(taille//3)+ taille//6, b*(taille//3) + taille//6, j, ancrage='center', couleur='black', police = "Helvetica", taille = 24)
    plt[a][b] = j
    mise_a_jour()
    return plt

casvictoire = {
'0': [(0,0), (1,1), (2,2)],
'1': [(2,0), (1,1), (0,2)],
'2': [(0,0), (1,0), (2,0)],
'3': [(0,1), (1,1), (2,1)],
'4': [(0,2), (1,2), (2,2)],
'5': [(0,0), (0,1), (0,2)],
'6': [(1,0), (1,1), (1,2)],
'7': [(2,0), (2,1), (2,2)]
        }

def verif_victoire(plt, jr):
    for k in range(len(casvictoire)):        
        res = 0
        for i in range(len(plt)):
            for j in range(len(plt[i])):
                if (i, j) in casvictoire[f'{k}'] and plt[i][j] == jr:
                    res += 1
                    if res == 3:
                        print(f'victoire de {jr} !')
                        if jr == j1:
                            return 1 #victoire de j1
                        else:
                            return 2 #victoire de j2
    #verif si toute les cases sont full mais que personne a encore gagné:
    for a in range(len(plt)):
        for b in range(len(plt[a])):
            if plt[a][b] == False:
                return 0
    return 3
            
def main():
    #j1 commence
    j = 1
    p = None
    jeu = True
    cree_fenetre(taille, taille)
    while(jeu):
        if j%2 == 1:
            p = j1
        else:
            p = j2
        affiche_plateau(plt)
        saisie(p, plt)  
        vv = verif_victoire(plt, p)
        if vv == 1:
            print("Victoire de J1 !")
            break
        elif vv == 2:
            print("Victoire de J2 !")
            break
        elif vv == 3:
            print("match nul")
            break
        j+=1
    affiche_plateau(plt)
    print("fin de la partie")

main()
