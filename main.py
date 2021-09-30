import sys, random
import pygame

pygame.display.set_caption('Snake')

largeur_ecran = 800
hauteur_ecran = 600


class Jeu:

    def __init__(self):

        self.ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

        self.joue = True

        self.serpent = [300, 300]
        self.direction = [0, 0]
        self.taille = 10

    def boucle(self):

        while self.joue:

            for evenement in pygame.event.get():

                '''keystate = pygame.key.get_pressed()
                if keystate[pygame.K_LEFT]:
                    self.direction = [-10, 0]
                if keystate[pygame.K_RIGHT]:
                    self.direction = [10, 0]
                if keystate[pygame.K_UP]:
                    self.direction = [0, 10]
                if keystate[pygame.K_DOWN]:
                    self.direction = [0, -10]'''

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

                
                
            self.serpent[0] += self.direction[0]
            self.serpent[1] += self.direction[1]

            self.direction = [0, 0]

            self.ecran.fill((0, 0, 0))

            self.bordure()

            pygame.draw.rect(self.ecran, (0, 255, 0), (self.serpent[0], self.serpent[1], self.taille, self.taille))

            pygame.display.flip()


    def bordure(self):
        pygame.draw.rect(self.ecran, (255, 255, 255), (100, 50, 600, 500), 3)


if __name__ == '__main__':
    pygame.init()
    Jeu().boucle()
    pygame.quit()
