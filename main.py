import sys, random
import pygame

from classe.menu import Menu
from classe.serpent import Serpent
from classe.pomme import Pomme




class Jeu:

    def __init__(self):
        self.titre = 'Snake'
        self.largeur_ecran = 800
        self.hauteur_ecran = 600
        self.marge_horizontal = 100
        self.marge_vertical = 50

        pygame.display.set_caption(self.titre)

        self.ecran = pygame.display.set_mode((self.largeur_ecran, self.hauteur_ecran))
        self.menu = Menu(True)
        self.joue = False

        self.taille = 10

        self.serpent = Serpent()
        self.pomme = Pomme(self.marge_horizontal, self.marge_vertical, self.largeur_ecran, self.hauteur_ecran, self.serpent.positions)

        self.score = 0

        self.temps_boucle = pygame.time.Clock()


    def boucle(self):

        if self.menu.actif == True:
            self.menu.boucle(self.ecran, self.titre, self.largeur_ecran, self.hauteur_ecran)
            self.joue = True


        while self.joue:

            for evenement in pygame.event.get():

                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:

                    if evenement.key == pygame.K_UP and self.serpent.direction != [0, 10]:
                            self.serpent.direction = [0, -10]

                    if evenement.key == pygame.K_RIGHT and self.serpent.direction != [-10, 0]:
                            self.serpent.direction = [10, 0]

                    if evenement.key == pygame.K_LEFT and self.serpent.direction != [10, 0]:
                            self.serpent.direction = [-10, 0]

                    if evenement.key == pygame.K_DOWN and self.serpent.direction != [0, -10]:
                            self.serpent.direction = [0, 10]


            self.serpent.avancer()

            self.serpent.mordre_queue()

            self.pomme_mange()

            self.ecran.fill((0, 0, 0))

            self.bordures()

            self.serpent.afficher(self.ecran)

            self.pomme.afficher(self.ecran)

            self.sortie_bordures()

            self.temps_boucle.tick(15)

            pygame.display.flip()


    def bordures(self):
        pygame.draw.rect(self.ecran, (255, 255, 255), (self.marge_horizontal, self.marge_vertical, (self.largeur_ecran - 2 * self.marge_horizontal), (self.hauteur_ecran - 2 * self.marge_vertical)), 3)


    def sortie_bordures(self):
        if self.serpent.tete[0] <= (self.marge_horizontal - 5) or self.serpent.tete[0] >= (self.largeur_ecran - self.marge_horizontal) or self.serpent.tete[1] <= (self.marge_vertical - 5) or self.serpent.tete[1] >= (self.hauteur_ecran - self.marge_vertical):
            sys.exit()


    def pomme_mange(self):
        if self.pomme.position[0] == self.serpent.tete[0] and self.pomme.position[1] == self.serpent.tete[1]:
            self.serpent.longueur += 1
            self.score += 1
            self.pomme.position = self.pomme.generer(self.marge_horizontal, self.marge_vertical, self.largeur_ecran, self.hauteur_ecran, self.serpent.positions)



if __name__ == '__main__':
    pygame.init()
    Jeu().boucle()
    pygame.quit()
