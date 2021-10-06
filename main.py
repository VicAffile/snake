import sys, random
import pygame

pygame.display.set_caption('Snake')

largeur_ecran = 800
hauteur_ecran = 600

class Jeu:

    def __init__(self):

        self.ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

        self.joue = True

        self.serpent_tete = [300, 300]
        self.serpent_direction = [10, 0]

        self.pomme = [random.randrange(110, 690, 10), random.randrange(60, 540, 10)]

        self.taille = 10

        self.temps_boucle = pygame.time.Clock()


    def boucle(self):

        while self.joue:

            for evenement in pygame.event.get():

                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:

                    if evenement.key == pygame.K_UP:
                        self.serpent_direction = [0, -10]

                    if evenement.key == pygame.K_RIGHT:
                        self.serpent_direction = [10, 0]

                    if evenement.key == pygame.K_LEFT:
                        self.serpent_direction = [-10, 0]

                    if evenement.key == pygame.K_DOWN:
                        self.serpent_direction = [0, 10]


            self.serpent_tete[0] += self.serpent_direction[0]
            self.serpent_tete[1] += self.serpent_direction[1]

            if self.pomme[0] == self.serpent_tete[0] and self.pomme[1] == self.serpent_tete[1]:
                self.pomme = [random.randrange(110, 690, 10), random.randrange(60, 540, 10)]


            self.ecran.fill((0, 0, 0))

            self.bordure()
            self.temps_boucle.tick(20)

            pygame.draw.rect(self.ecran, (0, 255, 0), (self.serpent_tete[0], self.serpent_tete[1], self.taille, self.taille))

            pygame.draw.rect(self.ecran, (255, 0, 0), (self.pomme[0], self.pomme[1], self.taille, self.taille))

            if self.serpent_tete[0] <= 95 or self.serpent_tete[0] >= 700 or self.serpent_tete[1] <= 45 or self.serpent_tete[1] >= 550:
                sys.exit()

            pygame.display.flip()


    def bordure(self):
        pygame.draw.rect(self.ecran, (255, 255, 255), (100, 50, 600, 500), 3)


if __name__ == '__main__':
    pygame.init()
    Jeu().boucle()
    pygame.quit()
