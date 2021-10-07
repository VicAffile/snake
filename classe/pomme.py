import random
import pygame


class Pomme:

    def __init__(self, marge_horizontal, marge_vertical, largeur_ecran, hauteur_ecran):

        self.taille = 10

        self.position = self.generer(marge_horizontal, marge_vertical, largeur_ecran, hauteur_ecran)


    def generer(self, marge_horizontal, marge_vertical, largeur_ecran, hauteur_ecran):
        return [random.randrange((marge_horizontal + self.taille), (largeur_ecran - marge_horizontal - self.taille), 10), random.randrange((marge_vertical + self.taille), (hauteur_ecran - marge_vertical - self.taille), 10)]


    def afficher(self, ecran):
        pygame.draw.rect(ecran, (255, 0, 0), (self.position[0], self.position[1], self.taille, self.taille))