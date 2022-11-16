#PLOUVIN Patrice
#LMI1
#12/02/18


import random

class PuissanceQuatre():
    '''Classe qui modélise le puissance4.
    Par défaut, le jeu est construit en dimension 6 x 7.
    '''
#Exercice 1:
    
    def __init__(self,l=6,c=7):
        '''Construit un puissance4 de l lignes x c colonnes.
           Arguments: self --- class --- PuissanceQuatre
                      l --- int --- nombre de ligne du jeu
                      c --- int --- nombre de colonne du jeu
           Retour : None'''
        
        assert c > 6 and l > 5
        self.__l = l
        self.__c = c
            
        self.__plateau = []
        for i in range(l):
            ligne = []
            for j in range(c):
                ligne.append(-1)
            self.__plateau.append(ligne) #les cases à la position l,c changeront de valeur au cours du jeu
        
        self.__carac = ['O ','X ']
        self.__dernier_coup = (-1,-1)
        self.__val_dernier_coup = None

#Exercice 2:
        
    def carac(self,joueur):
        '''Méthode qui renvoie la marque sur le pion du joueur (un O ou un X)
           Argument : self --- class --- PuissanceQuatre
                      joueur --- str --- le joueur qui à joué
           Retour : str --- pion du joueur'''
        if joueur == 0:
            return self.__carac[0]
        elif joueur == 1:
            return self.__carac[1]

        
#Exercice 3:
        
    def ligne_traits(self) :
        '''Méthode qui retourne une ligne de traits.
           Argument : self --- class --- puissance4
           Retour: str --- ligne de trait'''
        res = ''
        for i in range(self.__c) : #Dessine une ligne du plateau
            res += '+--'
        res += '+\n'
        return res

    def ligne_plateau(self,lig) :
        '''Méthode qui retourne la lig-ieme ligne du plateau sous forme textuelle..
           Argument : self --- class --- puissance4
                      lig --- int --- la position
           Retour: str --- colonne de trait'''
        res = ''
        for i in range(self.__c) :
            res += '|'
            if self.__plateau[lig][i] == -1 :
                res += "  "
            elif self.__plateau[lig][i] == 0 :
                res += str(self.__carac[0])
            elif self.__plateau[lig][i] == 1:
                res += str(self.__carac[1])
            elif self.__plateau[lig][i] < 10 :
                res += " "+str(self.__plateau[lig][i])
            else :
                res += str(self.__plateau[lig][i])
        res +="|\n"
        return res


    def __str__(self):
        '''Méthode qui retourne le plateau sous forme texte.
           Argument : self --- class --- Puissance4
           Retour : str --- le plateau'''
        mess=' '
        for j in range(self.__c): #Met le chiffre en 1er ligne
            mess += str(j)+'  '
        mess += '\n'
        for i in range(self.__l):
            mess += self.ligne_traits()
            mess += self.ligne_plateau(i)
        mess += self.ligne_traits()
        return mess


#Exercice 4:

    def colonne_valide(self,col):
        '''Méthode qui vérifie que le numéro de colonne donné en paramètre est valide
           Argument : self --- class --- Puissance4
                      col --- int --- colonne à verifié
           Retour : bool'''
        if col <= self.__c :
            for i in range(self.__l):
                if self.__plateau[i][col] == -1:
                    return True
        return False



#Exercice 5:
    def pose_colonne(self,choix,joueur):
        '''Méthode qui fait tomber le pion du joueur dans la colonne choix
           Arguments : self --- class --- Puissance4
                       choix --- int --- colonne choisie
                       joueur --- str --- le joueur qui joue
           Retour : bool'''
        if self.colonne_valide(choix) :
            for i in range(1, self.__l+1):
                if self.__plateau[self.__l-i][choix] == -1:
                    self.__plateau[self.__l-i][choix] = joueur
                    self.__dernier_coup =(self.__l-i,choix)
                    
                    return True
        return False



#Exercice 6:

    def est_valide(self,lig,col):
        '''Méthode qui teste si lig et col sont des coordonnées valides.
           Arguments : self --- class --- Puissance4
                       lig --- int --- une ligne
                       col --- int --- une colonne
           Retour : bool'''
        return 0 <= lig and lig < self.__l and 0 <= col and col < self.__c

#Exercice 7:

    def compte_valeur(self,lig,col,val,inc_lig,inc_col) :
        '''Méthode qui retourne le nombre de cases de valeur val à partir de (lig,col)
           dans la direction (inc_lig, inc_col)
           Arguments : self --- class --- PuissanceQuatre
                       lig --- int --- ligne de depart
                       col --- int --- colonne de depart
                       val --- int --- valeur de la case
                       inc_lig --- int --- incrément de ligne
                       inc_col --- int --- increment de colonne
           Retour : int --- nombre de cases de valeur val'''
        total = 1
        l = lig + inc_lig
        c = col + inc_col
        while self.est_valide(l,c) :
            if self.__plateau[l][c]== val :
                total +=1
            else :
                return total
            l += inc_lig
            c += inc_col
        return total

    def partie_plein(self) :
        '''Méthode qui dit si la partie est finie (pu de place sur le plateau)
           Arguments : self --- class --- Puissance4
           Retour : bool'''
        for i in range(self.__l):
            for j in range(self.__c):
                if self.__plateau[i][j] == -1 :
                    return False
        return True

    def partie_finie(self):
        '''Méthode qui dit si la partie est finie
           Arguments : self --- class --- Puissance4
           Retour : bool'''
        
        if self.partie_plein():
            return True

        x = self.__dernier_coup[1]
        y = self.__dernier_coup[0]
        gauche = x > 2
        droite = x < 3
        bas = y < 4
        
        
        if gauche and self.compte_valeur(x,y,0,0,-1) > 3:
            return True
        elif gauche and bas and self.compte_valeur(x,y,0,1,-1) > 3:
            return True
        elif bas and self.compte_valeur(x,y,0,1,0) > 3:
            return True
        elif bas and droite and self.compte_valeur(x,y,0,1,1) > 3:
            return True
        elif droite and self.compte_valeur(x,y,0,0,1) > 3:
            return True
            
        elif gauche and self.compte_valeur(x,y,1,0,-1) > 3:
            return True
        elif gauche and bas and self.compte_valeur(x,y,1,1,-1) > 3:
            return True
        elif bas and self.compte_valeur(x,y,1,1,0) > 3:
            return True
        elif bas and droite and self.compte_valeur(x,y,1,1,1) > 3:
            return True
        elif droite and self.compte_valeur(x,y,1,0,1) >3:
            return True

        else :
            return False
            



def main() :
    p4 = PuissanceQuatre()
    joueur = random.randint(0,1)
    while not p4.partie_finie():
        print(p4)
        
        print("Aux",p4.carac(joueur),"de jouer")
        choix = int(input("Dans quelle colonne voulez-vous jouer ? "))
        res = p4.pose_colonne(choix,joueur)
        if not res :
            print("Non, ce n’est pas possible.")
        else :
            joueur = (joueur+1)%2
    print(p4)
    print("Partie finie. Bravo")



### script principal
if __name__ == '__main__' :
    main()


##        for val in self.__carac:
##            for inc1 in range(-1,2):
##                for inc2 in range(-1,2):
##                    x = self.compte_valeur(self.__dernier_coup[0],self.__dernier_coup[1],val,inc1,inc2)
##                    if x >=4:
##                        return True
##        return False
