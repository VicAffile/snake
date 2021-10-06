import sys, random
import pygame

from classe.serpent import Serpent

pygame.display.set_caption('Snake')

largeur_ecran = 800
hauteur_ecran = 600
marge_horizontal = 100
marge_vertical = 50

class Jeu:

    def __init__(self):

        self.ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

        self.joue = True

        self.taille = 10

        self.serpent = Serpent()
        #self.serpent_tete = [300, 300]
        #self.serpent_position = []
        #self.serpent_position.append([int(self.serpent_tete[0]), int(self.serpent_tete[1])])
        #self.serpent_position.append([self.serpent_tete[0] - self.taille, self.serpent_tete[1]])
        #self.serpent_position.append([self.serpent_tete[0] - 2 * self.taille, self.serpent_tete[1]])
        #self.serpent_direction = [10, 0]
        #self.serpent_longueur = 3

        self.pomme = [random.randrange((marge_horizontal + self.taille), (largeur_ecran - marge_horizontal - self.taille), 10), random.randrange((marge_vertical + self.taille), (hauteur_ecran - marge_vertical - self.taille), 10)]

        self.score = 0

        self.temps_boucle = pygame.time.Clock()


    def boucle(self):

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


            if self.pomme[0] == self.serpent.tete[0] and self.pomme[1] == self.serpent.tete[1]:
                self.serpent.longueur += 1
                self.score += 1
                self.pomme = [random.randrange((marge_horizontal + self.taille), (largeur_ecran - marge_horizontal - self.taille), 10), random.randrange((marge_vertical + self.taille), (hauteur_ecran - marge_vertical - self.taille), 10)]

            self.ecran.fill((0, 0, 0))

            self.bordures()

            self.serpent.generer(self.ecran)

            pygame.draw.rect(self.ecran, (255, 0, 0), (self.pomme[0], self.pomme[1], self.taille, self.taille))

            self.sortie_bordures()

            self.temps_boucle.tick(15)

            pygame.display.flip()


    def bordures(self):
        pygame.draw.rect(self.ecran, (255, 255, 255), (marge_horizontal, marge_vertical, (largeur_ecran - 2 * marge_horizontal), (hauteur_ecran - 2 * marge_vertical)), 3)


    def sortie_bordures(self):
        if self.serpent.tete[0] <= (marge_horizontal - 5) or self.serpent.tete[0] >= (largeur_ecran - marge_horizontal) or self.serpent.tete[1] <= (marge_vertical - 5) or self.serpent.tete[1] >= (hauteur_ecran - marge_vertical):
            sys.exit()



if __name__ == '__main__':
    pygame.init()
    Jeu().boucle()
    pygame.quit()
