import sys

import pygame

from classe.ecran import Ecran
from classe.pomme import Pomme
from classe.serpent import Serpent


class Jeu(Ecran):

    def __init__(self, actif, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical):

        Ecran.__init__(self, actif)

        self.temps_boucle = pygame.time.Clock()

        self.serpent = Serpent()
        self.pomme = Pomme(marge_horizontal, marge_vertical, largeur_ecran, hauteur_ecran, self.serpent.positions)

        self.score = 0


    def boucle(self, ecran, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical):

        while self.actif:

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

            self.pomme_mange(largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical)

            ecran.fill((0, 0, 0))

            self.bordures(ecran, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical)

            self.serpent.afficher(ecran)

            self.pomme.afficher(ecran)

            self.sortie_bordures(largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical)

            self.temps_boucle.tick(15)

            pygame.display.flip()


    def bordures(self, ecran, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical):
        pygame.draw.rect(ecran, (255, 255, 255), (marge_horizontal, marge_vertical, (largeur_ecran - 2 * marge_horizontal), (hauteur_ecran - 2 * marge_vertical)), 3)


    def sortie_bordures(self, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical):
        if self.serpent.tete[0] <= (marge_horizontal - 5) or self.serpent.tete[0] >= (largeur_ecran - marge_horizontal) or self.serpent.tete[1] <= (marge_vertical - 5) or self.serpent.tete[1] >= (hauteur_ecran - marge_vertical):
            sys.exit()


    def pomme_mange(self, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical):
        if self.pomme.position[0] == self.serpent.tete[0] and self.pomme.position[1] == self.serpent.tete[1]:
            self.serpent.longueur += 1
            self.score += 1
            self.pomme.position = self.pomme.generer(marge_horizontal, marge_vertical, largeur_ecran, hauteur_ecran, self.serpent.positions)
