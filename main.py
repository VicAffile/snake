import sys, random
import pygame

pygame.display.set_caption('Snake')

largeur_ecran = 800
hauteur_ecran = 600

class Jeu:

    def __init__(self):

        self.ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

        self.joue = True

        self.tete = [300, 300]
        self.direction = [10, 0]
        self.taille = 10

        self.temps_boucle = pygame.time.get_ticks()


    def boucle(self):

        while self.joue:

            for evenement in pygame.event.get():

                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:

                    if evenement.key == pygame.K_UP:
                        self.direction = [0, -10]

                    if evenement.key == pygame.K_RIGHT:
                        self.direction = [10, 0]

                    if evenement.key == pygame.K_LEFT:
                        self.direction = [-10, 0]

                    if evenement.key == pygame.K_DOWN:
                        self.direction = [0, 10]


            if (pygame.time.get_ticks() - self.temps_boucle) >= 200:
                self.tete[0] += self.direction[0]
                self.tete[1] += self.direction[1]
                self.temps_boucle = pygame.time.get_ticks()


            self.ecran.fill((0, 0, 0))

            self.bordure()

            pygame.draw.rect(self.ecran, (0, 255, 0), (self.tete[0], self.tete[1], self.taille, self.taille))

            if self.tete[0] <= 100 or self.tete[0] >= 700 or self.tete[1] <= 50 or self.tete[1] >= 550:
                sys.exit()

            pygame.display.flip()


    def bordure(self):
        pygame.draw.rect(self.ecran, (255, 255, 255), (100, 50, 600, 500), 3)


if __name__ == '__main__':
    pygame.init()
    Jeu().boucle()
    pygame.quit()
