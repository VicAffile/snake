import sys, random
import pygame

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

        self.serpent_tete = [300, 300]
        self.serpent_position = []
        self.serpent_position.append([int(self.serpent_tete[0]), int(self.serpent_tete[1])])
        self.serpent_position.append([self.serpent_tete[0] - self.taille, self.serpent_tete[1]])
        self.serpent_position.append([self.serpent_tete[0] - 2 * self.taille, self.serpent_tete[1]])
        self.serpent_direction = [10, 0]
        self.serpent_longueur = 3

        self.pomme = [random.randrange((marge_horizontal + self.taille), (largeur_ecran - marge_horizontal - self.taille), 10), random.randrange((marge_vertical + self.taille), (hauteur_ecran - marge_vertical - self.taille), 10)]

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
            self.serpent_position.insert(0, [int(self.serpent_tete[0]), int(self.serpent_tete[1])])
            if len(self.serpent_position) >= self.serpent_longueur:
                self.serpent_position.pop()

            if self.pomme[0] == self.serpent_tete[0] and self.pomme[1] == self.serpent_tete[1]:
                self.serpent_longueur += 1
                self.pomme = [random.randrange((marge_horizontal + self.taille), (largeur_ecran - marge_horizontal - self.taille), 10), random.randrange((marge_vertical + self.taille), (hauteur_ecran - marge_vertical - self.taille), 10)]

            self.ecran.fill((0, 0, 0))

            self.bordure()
            self.temps_boucle.tick(15)

            self.generer_serpent()

            pygame.draw.rect(self.ecran, (255, 0, 0), (self.pomme[0], self.pomme[1], self.taille, self.taille))

            if self.serpent_tete[0] <= 95 or self.serpent_tete[0] >= 700 or self.serpent_tete[1] <= 45 or self.serpent_tete[1] >= 550:
                sys.exit()

            pygame.display.flip()


    def bordure(self):
        pygame.draw.rect(self.ecran, (255, 255, 255), (marge_horizontal, marge_vertical, (largeur_ecran - 2 * marge_horizontal), (hauteur_ecran - 2 * marge_vertical)), 3)


    def generer_serpent(self):
        for partie_serpent in self.serpent_position:
            pygame.draw.rect(self.ecran, (0, 255, 0), (partie_serpent[0], partie_serpent[1], self.taille, self.taille))


if __name__ == '__main__':
    pygame.init()
    Jeu().boucle()
    pygame.quit()
