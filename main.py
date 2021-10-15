import pygame

from classe.menu import Menu
from classe.jeu import Jeu
from classe.table import Table


class Logiciel:

    def __init__(self):
        self.titre = 'Snake'
        self.largeur_ecran = 800
        self.hauteur_ecran = 600
        self.marge_horizontal = 100
        self.marge_vertical = 50

        pygame.display.set_caption(self.titre)

        self.ecran = pygame.display.set_mode((self.largeur_ecran, self.hauteur_ecran))

        self.menu = Menu(True)
        self.jeu = Jeu(False, self.largeur_ecran, self.hauteur_ecran, self.marge_horizontal, self.marge_vertical)

        self.bdd = Table()
        self.bdd.initialisation()
        self.bdd.remplissage()
        self.bdd.ajouter("Guillaume", 1)
        print(self.bdd.classement(5))


    def boucle(self):

        while self.menu.actif == True or self.jeu.actif == True:

            if self.menu.actif == True:
                self.menu.boucle(self.ecran, self.titre, self.largeur_ecran, self.hauteur_ecran)
                self.jeu = Jeu(False, self.largeur_ecran, self.hauteur_ecran, self.marge_horizontal, self.marge_vertical)
                self.jeu.actif = True


            if self.jeu.actif == True:
                self.jeu.boucle(self.ecran, self.largeur_ecran, self.hauteur_ecran, self.marge_horizontal, self.marge_vertical)
                self.menu.actif = True


if __name__ == '__main__':
    pygame.init()
    Logiciel().boucle()
    pygame.quit()
