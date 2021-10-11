import sys
import pygame


class Serpent:

    def __init__(self):

        self.taille = 10
        self.longueur = 3

        self.tete = [300, 300]

        self.positions = []
        self.positions.append([int(self.tete[0]), int(self.tete[1])])
        self.positions.append([self.tete[0] - self.taille, self.tete[1]])
        self.positions.append([self.tete[0] - 2 * self.taille, self.tete[1]])

        self.direction = [10, 0]


    def afficher(self, ecran):
        for position in self.positions:
            pygame.draw.rect(ecran, (0, 255, 0), (position[0], position[1], self.taille, self.taille))


    def avancer(self):
        self.tete[0] += self.direction[0]
        self.tete[1] += self.direction[1]
        self.positions.insert(0, [int(self.tete[0]), int(self.tete[1])])
        if len(self.positions) >= self.longueur:
            self.positions.pop()


    def mordre_queue(self):
        del self.positions[0]
        for position in self.positions:
            if position == self.tete:
                sys.exit()
        self.positions.insert(0, [int(self.tete[0]), int(self.tete[1])])