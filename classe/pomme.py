import random
import pygame


class Pomme:

    def __init__(self, marge_horizontal, marge_vertical, largeur_ecran, hauteur_ecran, serpent_positions):

        self.taille = 10

        self.position = self.generer(marge_horizontal, marge_vertical, largeur_ecran, hauteur_ecran, serpent_positions)


    def generer(self, marge_horizontal, marge_vertical, largeur_ecran, hauteur_ecran, serpent_positions):

        superposition = True
        pomme_position = 0

        while superposition:

            superposition = False
            pomme_position = [random.randrange((marge_horizontal + self.taille), (largeur_ecran - marge_horizontal - self.taille), 10), random.randrange((marge_vertical + self.taille), (hauteur_ecran - marge_vertical - self.taille), 10)]

            for serpent_position in serpent_positions:
                if pomme_position == serpent_position:
                    superposition = True

        return pomme_position


    def afficher(self, ecran):
        pygame.draw.rect(ecran, (255, 0, 0), (self.position[0], self.position[1], self.taille, self.taille))