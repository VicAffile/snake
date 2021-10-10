import sys, random
import pygame

from classe.serpent import Serpent
from classe.pomme import Pomme

pygame.display.set_caption('Snake')

largeur_ecran = 800
hauteur_ecran = 600
marge_horizontal = 100
marge_vertical = 50

class Jeu:

    def __init__(self):

        self.ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
        self.menu = True
        self.joue = True

        self.taille = 10

        self.serpent = Serpent()
        self.pomme = Pomme(marge_horizontal, marge_vertical, largeur_ecran, hauteur_ecran)

        self.score = 0

        self.temps_boucle = pygame.time.Clock()


    def boucle(self):

        while self.menu:

            for evenement in pygame.event.get():

                if evenement.type == pygame.quit():
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:
                        self.menu = False
                        self.joue = True

            self.ecran.fill((0, 0, 0))

            pygame.display.flip()


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
        pygame.draw.rect(self.ecran, (255, 255, 255), (marge_horizontal, marge_vertical, (largeur_ecran - 2 * marge_horizontal), (hauteur_ecran - 2 * marge_vertical)), 3)


    def sortie_bordures(self):
        if self.serpent.tete[0] <= (marge_horizontal - 5) or self.serpent.tete[0] >= (largeur_ecran - marge_horizontal) or self.serpent.tete[1] <= (marge_vertical - 5) or self.serpent.tete[1] >= (hauteur_ecran - marge_vertical):
            sys.exit()


    def pomme_mange(self):
        if self.pomme.position[0] == self.serpent.tete[0] and self.pomme.position[1] == self.serpent.tete[1]:
            self.serpent.longueur += 1
            self.score += 1
            self.pomme.position = self.pomme.generer(marge_horizontal, marge_vertical, largeur_ecran, hauteur_ecran)



if __name__ == '__main__':
    pygame.init()
    Jeu().boucle()
    pygame.quit()
