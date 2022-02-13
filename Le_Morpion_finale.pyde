#    Le morpion3
# Julien Goetghebeur
# jeu de base(1) + ordinateur "inteligent"(2) + scores(3)

from random import randint 

VIDE = 0
JOUEUR = 7
ORDINATEUR = 5
PERSONNE = 10
PION_JOUEUR = "X"
PION_ORDINATEUR = "O"
TAILLE_GRILLE = 3
TAILLE_CASE = 200

def grille_vide():
    """
    Renvoie une plateau vide
    Entrée : 
        * vide
    Sortie : 
        * liste : une liste de listes avec des valeurs correspondant à VIDE
    """
    return [[VIDE,VIDE,VIDE],[VIDE,VIDE,VIDE],[VIDE,VIDE,VIDE]]

joueur = JOUEUR 
p1 = grille_vide()
vainqueur = PERSONNE
affichage = 'accueil'
clic = ''
ligne = -1
colonne = -1
score_ordi = 0
score_joueur = 0 




def setup():
    global TAILLE_GRILLE, TAILLE_CASE
    size(TAILLE_GRILLE*TAILLE_CASE+200,TAILLE_GRILLE*TAILLE_CASE)
    background(255)
    
    rectMode(CENTER)
    strokeWeight(5)
    
    textAlign(CENTER)
    font = createFont("Pixeled.ttf",24)
    textFont(font)
    

def draw():
    global affichage,clic
    
    if affichage == 'accueil' :
        clic = ecran_titre()
        if clic == 'JOUER':
           affichage = 'jeu'
           delai()
        elif clic == 'QUITTER':
            exit()
    elif affichage == 'jeu':
        jeu()
    elif affichage == 'fin':
        clic = ecran_fin()
        if clic == 'REJOUER' :
            affichage = 'jeu'
            delai()
            initialisation()
        elif clic == 'QUITTER' :
            exit()
    elif affichage == 'recommencer':
        initialisation()
        jeu()
        




def jeu():
    global affichage,ligne,colonne,p1,joueur,vainqueur,score_joueur,score_ordi
    
    afficher_la_grille(p1)

    (ligne,colonne) = le_joueur_fait_une_proposition(joueur)
    if la_case_est_vide(ligne,colonne,p1) and 0<=ligne<=2 and 0<=colonne<=2 :
        p1[ligne][colonne] = joueur
        
        afficher_la_grille(p1)
        
        if alignement_reussi(joueur,p1) :
            vainqueur = joueur
            if joueur == JOUEUR :
                score_joueur += 1
            elif joueur == ORDINATEUR :
                score_ordi += 1
            affichage = 'fin'
            delai()
        else :
            if le_plateau_est_plein(p1):
                affichage = 'fin'
                delai()
        if joueur == JOUEUR :
            joueur = ORDINATEUR 
        else:
            joueur = JOUEUR
            
    
def initialisation():
    """
    Fonction qui réinitialise les variables quand on relance une partie.
    """
    global joueur,p1,vainqueur,affichage,clic,ligne,colonne
    joueur = JOUEUR 
    p1 = grille_vide()
    vainqueur = PERSONNE
    affichage = 'jeu'
    clic = ''
    ligne = -1
    colonne = -1
    
    
def delai():
    """
    Fonction qui créer un délai de 200 ms.
    """
    temps1 = millis()
    while (millis() > temps1 + 200 ) == False:
        pass
        

        
                
        
def motif(n):
    """
    Renvoie le motif associer à un joueur : JOUEUR->PION_JOUEUR, ORDINATEUR->PION_ORDINATEUR et VIDE->" "
    Entrée :
        * n : int, la valeur du plateau à représenter
    Sortie :
        * m : string, le motif : un espace si c'est vide, un X ou un O
    """
    m=""
    if n == JOUEUR :
        m = PION_JOUEUR
    elif n == ORDINATEUR :
        m = PION_ORDINATEUR
    elif n == VIDE :
        m = " "
    return m

def afficher_la_grille(t):
    global affichage
    """
    Imprime à l'écran la grille
    Entrée :
        * t : liste : la liste de listes représentant le plateau
    Sortie :
        * affichage dans la console
    """
    background(255)
    tracer_lignes()
    for i in range(0,len(t)) :
        for j in range(0,len(t[0])):
            if motif(t[i][j]) == "X" :
                tracer_croix(j,i)
            elif motif(t[i][j]) == "O" :
                tracer_cercle(j,i)
    
    clic = afficher_bande()
    if clic == 'RECOMMENCER':
        affichage = 'recommencer'
    elif clic == 'QUITTER' :
        exit()
    
def tracer_cercle(x,y):
    fill(255)
    stroke(255,0,0)
    ellipse(x*TAILLE_CASE+TAILLE_CASE/2,y*TAILLE_CASE+TAILLE_CASE/2,TAILLE_CASE/2,TAILLE_CASE/2)
    stroke(0)
    
def tracer_croix(x,y):
    stroke(0,0,255)
    line((x*TAILLE_CASE+TAILLE_CASE/2)-50,(y*TAILLE_CASE+TAILLE_CASE/2)-50,(x*TAILLE_CASE+TAILLE_CASE/2)+50,(y*TAILLE_CASE+TAILLE_CASE/2)+50)
    line((x*TAILLE_CASE+TAILLE_CASE/2)-50,(y*TAILLE_CASE+TAILLE_CASE/2)+50,(x*TAILLE_CASE+TAILLE_CASE/2)+50,(y*TAILLE_CASE+TAILLE_CASE/2)-50)
    stroke(0)
    
def tracer_lignes():
    for i in range(4):
        line(TAILLE_GRILLE*TAILLE_CASE/3*i,0,TAILLE_GRILLE*TAILLE_CASE/3*i,TAILLE_GRILLE*TAILLE_CASE)
    for j in range(4):
        line(0,(TAILLE_GRILLE*TAILLE_CASE)/3*j,TAILLE_GRILLE*TAILLE_CASE,(TAILLE_GRILLE*TAILLE_CASE)/3*j)

def ecran_fin():
    global score_joueur,score_ordi,affichage
    """
    Fonction qui affiche l'écran de fin.
    -Affiche qui a gagné 
    -Proposer de rejouer ou de quitter
    """
    clic1 = afficher_bande()
    if clic1 == 'RECOMMENCER':
        affichage = 'recommencer'
    elif clic1 == 'QUITTER' :
        exit()
    clic = ''
    if vainqueur == JOUEUR :
        textSize(60)
        fill(50,255,40)
        text("VICTOIRE !!",TAILLE_GRILLE*TAILLE_CASE/2,300)
    elif vainqueur == ORDINATEUR :
        textSize(60)
        fill(60,200,255)
        text("PERDU !!",TAILLE_GRILLE*TAILLE_CASE/2,300)
    elif vainqueur == PERSONNE :
        textSize(60)
        fill(255,200,60)
        text("EGALITE !!",TAILLE_GRILLE*TAILLE_CASE/2,300)
    if bouton(150,500,200,75,"REJOUER",[100,255,100],[0,255,0],26):
        clic = 'REJOUER'
    elif bouton(450,500,200,75,"QUITTER",[255,100,100],[255,0,0],26):
        clic = 'QUITTER'
    return clic
    
    
def ecran_titre():
    """
    Affiche l'ecran titre du jeu.
    -propose de choisir son pion 
    -propose de jouer ou de quitter
    """
    global PION_JOUEUR , PION_ORDINATEUR
    textSize(50)
    fill(0)
    text("Le Morpion",width/2,height/3)
    textSize(15)
    text("Choisissez votre pion : ",width/3,height/2)
    choix = 'rien'
    if bouton_pion(width/3+20,375,100,100,[250,250,250],'croix'):
        choix = 'croix'
        
    elif bouton_pion(width/3*2-20,375,100,100,[250,250,250],'rond'):
        choix='rond'
    if choix == 'croix' :
        noStroke()
        fill (240,240,240)
        rect(width/3+20,375,100,100,20)
        fill(255)
        rect(width/3*2-20,375,100,100,20)
        stroke(0)
        PION_JOUEUR = "X"
        PION_ORDINATEUR = "O"
    elif choix == 'rond' :
        noStroke()
        fill (240,240,240)
        rect(width/3*2-20,375,100,100,20)
        fill (255)
        rect(width/3+20,375,100,100,20)
        stroke(0)
        PION_JOUEUR = "O"
        PION_ORDINATEUR = "X"
    strokeWeight(5)
    clic = ''
    if bouton(250,500,200,75,"JOUER",[100,255,100],[0,255,0],26):
        clic = 'JOUER'
    elif bouton(550,500,200,75,"QUITTER",[255,100,100],[255,0,0],26):
        clic = 'QUITTER'
    return clic

def bouton(x,y,largeur,hauteur,texte,couleur,couleur2,Size):
    """
    Fonction qui affiche un bouton qui change de couleur quand la souris passe dessus.
    x,y : coordonnées du bouton
    largeur,hauteur : dimension du bouton
    couleur : couleur du bouton quand la souris passe dessus
    couleur2 : couleur du bouton
    """
    textSize(Size)
    if  x - largeur/2 < mouseX < x + largeur/2 and  y-hauteur/2 < mouseY < y + hauteur/2 :
        fill (couleur[0],couleur[1],couleur[2])
        rect(x,y,largeur,hauteur,20)
        fill(0,0,0)
        text(texte,x,y+hauteur*0.28)
        if mousePressed :
            return True
    else:
        fill (couleur2[0],couleur2[1],couleur2[2])
        rect(x,y,largeur,hauteur,20)
        fill(0,0,0)
        text(texte,x,y+hauteur*0.28)
    return False

def bouton_pion(x,y,largeur,hauteur,couleur,pion):
    """
    Fonction qui affiche un bouton qui change de couleur quand la souris clique dessus.
    x,y : coordonnées du bouton
    largeur,hauteur : dimension du bouton
    couleur : couleur du bouton quand la souris clique dessus
    pion : 'croix' ou 'rond' 
    """
    if  x - largeur/2 < mouseX < x + largeur/2 and  y-hauteur/2 < mouseY < y + hauteur/2 :
        strokeWeight(5)
        fill(255)
        if pion == 'croix':
            stroke(0,0,255)
            line(x-40,y-40,x+40,y+40)
            line(x-40,y+40,x+40,y-40)
            stroke(0)
        elif pion == 'rond':
            noFill()
            stroke(255,0,0)
            ellipse(x,y,80,80)
            stroke(0)
        if mousePressed :
            return True
    else:
        strokeWeight(5)
        fill(255)
        if pion == 'croix':
            stroke(0,0,255)
            line(x-40,y-40,x+40,y+40)
            line(x-40,y+40,x+40,y-40)
            stroke(0)
        elif pion == 'rond':
            noFill()
            stroke(255,0,0)
            ellipse(x,y,80,80)
            stroke(0)
    return False

def afficher_bande():
    global score_joueur,score_ordi
    """
    Fonction qui affiche les informations dans la bande droite de la fenêtre, à coté de la grille de jeu.
    -affiche les scores
    -permet de recommencer ou de quitter la partie
    """
    clic = ''
    textAlign(LEFT)
    textSize(20)
    text("scores : ",TAILLE_GRILLE*TAILLE_CASE+10,40)
    textSize(15)
    text("JOUEUR : " + str(score_joueur),TAILLE_GRILLE*TAILLE_CASE+15,80)
    text("ORDINATEUR : " + str(score_ordi),TAILLE_GRILLE*TAILLE_CASE+15,110)
    textAlign(CENTER)
    
    if bouton(TAILLE_GRILLE*TAILLE_CASE+100, height -35, 175,50,"QUITTER",[255,100,100],[255,0,0],20):
        clic = "QUITTER"
    elif bouton(TAILLE_GRILLE*TAILLE_CASE+100, height - 95,175,50,"RECOMMENCER",[100,255,100],[0,255,0],14):
        clic= "RECOMMENCER"
    return clic


def alignement_horizontal(joueur,t):
    """
    Teste les lignes du plateau à la recherche d'un alignement de 3 pions pour le joueur j
    Entrée :
        * joueur : int, identifiant du joueur (ici : JOUEUR ou ORDINATEUR)
        * t : liste correspondant au plateau
    Sortie :
        * resultat, bool
    """
    for i in range(len(t)):
        s = 0
        for j in range(len(t[i])):
            s += t[i][j]
        if s == 3*joueur:
            return True
    return False

def alignement_vertical(joueur,t):
    """
    Teste les colonnes du plateau à la recherche d'un alignement de 3 pions pour le joueur j
    Entrée :
        * joueur : int, identifiant du joueur (ici : JOUEUR ou ORDINATEUR)
        * t : liste correspondant au plateau
    Sortie :
        * resultat, bool
    """
    for i in range(0,len(t)):
        s = 0
        for j in range(len(t[i])):
            s += t[j][i]
        if s == 3*joueur :
            return True 
    return False

def alignement_premiere_diagonale(joueur,t):
    """
    Teste la premiere diagonale à la recherche d'un alignement de 3 pions pour le joueur j
    Entrée :
        * joueur : int, identifiant du joueur (ici : JOUEUR ou ORDINATEUR)
        * t : liste correspondant au plateau
    Sortie :
        * resultat, bool
    """
    s = 0
    for i in range(len(t)):
        s += t[i][i]
    if s == 3*joueur :
        return True
    else :
        return False

def alignement_seconde_diagonale(joueur,t):
    """
    Teste la seconde diagonale à la recherche d'un alignement de 3 pions pour le joueur j
    Entrée :
        * joueur : int, identifiant du joueur (ici : JOUEUR ou ORDINATEUR)
        * t : liste correspondant au plateau
    Sortie :
        * resultat, bool
    """
    s = 0
    for i in range(0,len(t)):
        s += t[i][2-i]
    if s == 3*joueur :
        return True
    else :
        return False

def alignement_reussi(joueur,t):
    """
    Teste les 4 alignements possibles pour le joueur. Renvoie True s'il a gagné, False sinon.
    Entrée :
        * joueur : int, identifiant du joueur (ici : JOUEUR ou ORDINATEUR)
        * t : liste correspondant au plateau
    Sortie :
        * resultat, bool
    """ 
    resultat = False
    resultat = resultat or alignement_horizontal(joueur,t)
    resultat = resultat or alignement_vertical(joueur,t)
    resultat = resultat or alignement_premiere_diagonale(joueur,t)
    resultat = resultat or alignement_seconde_diagonale(joueur,t)
    return resultat 

def le_plateau_est_plein(t):
    """
    Teste si le plateau est plein
    Entrée :
        * t : liste correspondant au plateau
    Sortie :
        * resultat, bool
    """
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] == VIDE :
                return False
    return True

def la_case_est_vide(i,j,t):
    """
    Teste si la case de la ligne i et de la colonne j est vide
    Entrée :
        * i : int, la ligne de la case à tester
        * j : int, la colonne de la case
        * t : liste correspondant au plateau
    Sortie :
        * bool
    """
    if t[i][j] == VIDE :
        return True
    return False

def le_joueur_fait_une_proposition(j) :
    """
    Renvoie la ligne et la colonne choisi par le joueur j
    Entrée : 
        * j , int, identifiant le JOUEUR
    Sortie :
        * prop, couple de deux entiers
    """
    if j==JOUEUR :
        prop = l_homme_fait_une_proposition()
    else :
        prop = l_ordinateur_fait_une_proposition()
        delai()
    return prop

def l_homme_fait_une_proposition() :
    global ligne,colonne
    """
    Renvoie la ligne et la colonne choisi par le JOUEUR. Le joueur clique sur la case choisi.
    Entrée : 
        * vide
    Sortie :
        * prop, couple de deux entiers
    """
    if mousePressed  and 0 < mouseX < TAILLE_GRILLE*TAILLE_CASE :
        ligne = mouseY // 200
        colonne = mouseX // 200
    return (ligne,colonne)  

def l_ordinateur_fait_une_proposition() :
    """
    Choisi la case pour gagner au prochain tour
    Sinon, fait en sorte que l'ordinateur bloque le joueur si il va gagner
    Sinon, renvoie la ligne et la colonne choisi au hasard.
    Entrée : 
        * vide
    Sortie :
        * prop, couple de deux entiers
    
    """
    prop = prochain_tour(ORDINATEUR)
    if prop != (-1,-1) :
        return prop
    prop = prochain_tour(JOUEUR)
    if prop != (-1,-1) :
        return prop
    ligne = randint(0,2)
    colonne = randint(0,2)
    return (ligne,colonne)

def prochain_tour(joueur):
    """
    Trouve les coordonnées de la case que le joueur doit choisir pour gagner.
    """
    t = p1[:]
#test alignement horizontal
    for i in range(len(t)):
        s = 0
        for j in range(len(t[i])):
            s += t[i][j]
            if t[i][j] == 0:
                case = (i,j)
        if s == 2*joueur:
            return (case)
#test alignement vertical
    for i in range(0,len(t)):
        s = 0
        for j in range(len(t[i])):
            s += t[j][i]
            if t[j][i] == 0:
                case = (j,i)
        if s == 2*joueur :
            return (case)
#test alignement diagonal
    s = 0
    for i in range(len(t)):
        s += t[i][i]
        if t[i][i] == 0:
            case = (i,i)
    if s == 2*joueur :
        return (case)
    
    s = 0
    for i in range(0,len(t)):
        s += t[i][2-i]
        if t[i][2-i] == 0:
            case = (i,2-i)
    if s == 2*joueur :
         return(case)
    return (-1,-1)










# def morpion():
#     global VIDE,JOUEUR,ORDINATEUR,PERSONNE,PION_JOUEUR,PION_ORDINATEUR 
#     joueur = JOUEUR 
#     p1 = grille_vide()
#     partie_en_cours = True
#     vainqueur = 'personne'

#     afficher_la_grille(p1)
    
#     while partie_en_cours :
#         (ligne,colonne) = le_joueur_fait_une_proposition(joueur)
#         if la_case_est_vide(ligne,colonne,p1) :
#             p1[ligne][colonne] = joueur
            
#             afficher_la_grille(p1)
            
#             if alignement_reussi(joueur,p1) == True :
#                 vainqueur = joueur
#                 partie_en_cours = False
#             else :
#                 if le_plateau_est_plein(p1):
#                     partie_en_cours = False
            
#             if joueur == JOUEUR :
#                 joueur = ORDINATEUR 
#             else:
#                 joueur = JOUEUR
        
#         else :
#             if joueur == JOUEUR :
#                 print("La case est prise, choisissez en une autre")
                
    
#     if vainqueur == JOUEUR :
#         print("Bravo ! Vous avez gagné !")
#     elif vainqueur == ORDINATEUR :
#         print("Dommage, l'ordinateur a gagné.")
#     else :
#         print("Égalité !")
    
    
# morpion()
# n = input("Voulez-vous rejouez ? (oui/non)")
# while n != 'non' :
#     if n == 'oui':
#         morpion()
#     else :
#         n = input("Voulez-vous rejouez ? (oui/non)")
#     n = input("Voulez-vous rejouez ? (oui/non)")
