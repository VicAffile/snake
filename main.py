import sys, random
import pygame

pygame.display.set_caption('Snake')

largeur_ecran = 800
hauteur_ecran = 600


class Jeu:


    def __init__(self):

        self.ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

        self.joue = True


    def boucle(self):

        while self.joue:

            for evenement in pygame.event.get():

                if evenement.type == pygame.QUIT:
                    sys.exit()


            self.ecran.fill((0, 0, 0))
            pygame.display.flip()


if __name__ == '__main__':

    pygame.init()
    Jeu().boucle()
    pygame.quit()