import pygame

from classe.table import Table


class Ecran:

    def __init__(self, actif):

        self.actif = actif
        self.bdd = Table()


    def afficher_message(self, message, taille, couleur, dimension, ecran):

        if taille == 'petite':
            taille = pygame.font.SysFont('Lato', 20, False)
        elif taille == 'moyenne':
            taille = pygame.font.SysFont('Lato', 30, False)
        elif taille == 'grande':
            taille = pygame.font.SysFont('Lato', 40, False)

        message = taille.render(message, True, couleur)

        ecran.blit(message, dimension)