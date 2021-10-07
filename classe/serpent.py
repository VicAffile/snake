import sys
import pygame


class Serpent:

    def __init__(self):

        self.taille = 10
        self.longueur = 3

        self.tete = [300, 300]

        self.position = []
        self.position.append([int(self.tete[0]), int(self.tete[1])])
        self.position.append([self.tete[0] - self.taille, self.tete[1]])
        self.position.append([self.tete[0] - 2 * self.taille, self.tete[1]])

        self.direction = [10, 0]


    def afficher(self, ecran):
        for partie in self.position:
            pygame.draw.rect(ecran, (0, 255, 0), (partie[0], partie[1], self.taille, self.taille))


    def avancer(self):
        self.tete[0] += self.direction[0]
        self.tete[1] += self.direction[1]
        self.position.insert(0, [int(self.tete[0]), int(self.tete[1])])
        if len(self.position) >= self.longueur:
            self.position.pop()


    def mordre_queue(self):
        del self.position[0]
        for partie in self.position:
            if partie == self.tete:
                sys.exit()
        self.position.insert(0, [int(self.tete[0]), int(self.tete[1])])