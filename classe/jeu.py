import sys

import pygame

from classe.ecran import Ecran
from classe.pomme import Pomme
from classe.serpent import Serpent


class Jeu(Ecran):

    def __init__(self, actif, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical):

        Ecran.__init__(self, actif)

        self.temps_boucle = pygame.time.Clock()

        self.serpent = Serpent()
        self.pomme = Pomme(marge_horizontal, marge_vertical, largeur_ecran, hauteur_ecran, self.serpent.positions)

        self.score = 0


    def boucle(self, ecran, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical):

        while self.actif:

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

            if self.serpent.mordre_queue():
                if self.nouveau_score():
                    self.pseudo = []
                self.fin_jeu(ecran, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical)

            self.pomme_mange(largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical)

            ecran.fill((0, 0, 0))

            self.afficher_message('Score : {}'.format(str(self.score)), 'grande', (240, 240, 240), (5, 5, 100, 50), ecran)

            self.bordures(ecran, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical)

            self.serpent.afficher(ecran)

            self.pomme.afficher(ecran)

            if self.sortie_bordures(largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical):
                if self.nouveau_score():
                    self.pseudo = []
                self.fin_jeu(ecran, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical)

            self.temps_boucle.tick(15)

            pygame.display.flip()


    def bordures(self, ecran, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical):
        pygame.draw.rect(ecran, (255, 255, 255), (marge_horizontal, marge_vertical, (largeur_ecran - 2 * marge_horizontal), (hauteur_ecran - 2 * marge_vertical)), 3)


    def sortie_bordures(self, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical):

        if self.serpent.tete[0] <= (marge_horizontal - 5) or self.serpent.tete[0] >= (largeur_ecran - marge_horizontal) or self.serpent.tete[1] <= (marge_vertical - 5) or self.serpent.tete[1] >= (hauteur_ecran - marge_vertical):
            return True

        return False


    def pomme_mange(self, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical):
        if self.pomme.position[0] == self.serpent.tete[0] and self.pomme.position[1] == self.serpent.tete[1]:
            self.serpent.longueur += 1
            self.score += 1
            self.pomme.position = self.pomme.generer(marge_horizontal, marge_vertical, largeur_ecran, hauteur_ecran, self.serpent.positions)


    def fin_jeu(self, ecran, largeur_ecran, hauteur_ecran, marge_horizontal, marge_vertical):

        pygame.time.delay(1000)

        while self.actif:

            for evenement in pygame.event.get():

                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:

                    if self.nouveau_score():

                        if evenement.key == pygame.K_RETURN and len(self.pseudo) > 0:
                            self.bdd.ajouter(self.nouveau_pseudo(), self.score)
                            self.actif = False

                        if evenement.key == pygame.K_BACKSPACE and len(self.pseudo) > 0:
                            self.pseudo.pop()

                        if evenement.key == pygame.K_a and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('a')
                            else:
                                self.pseudo.append('A')

                        if evenement.key == pygame.K_b and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('b')
                            else:
                                self.pseudo.append('B')

                        if evenement.key == pygame.K_c and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('c')
                            else:
                                self.pseudo.append('C')

                        if evenement.key == pygame.K_d and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('d')
                            else:
                                self.pseudo.append('D')

                        if evenement.key == pygame.K_e and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('e')
                            else:
                                self.pseudo.append('E')

                        if evenement.key == pygame.K_f and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('f')
                            else:
                                self.pseudo.append('F')

                        if evenement.key == pygame.K_g and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('g')
                            else:
                                self.pseudo.append('G')

                        if evenement.key == pygame.K_h and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('h')
                            else:
                                self.pseudo.append('H')

                        if evenement.key == pygame.K_i and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('i')
                            else:
                                self.pseudo.append('I')

                        if evenement.key == pygame.K_j and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('j')
                            else:
                                self.pseudo.append('J')

                        if evenement.key == pygame.K_k and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('k')
                            else:
                                self.pseudo.append('K')

                        if evenement.key == pygame.K_l and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('l')
                            else:
                                self.pseudo.append('L')

                        if evenement.key == pygame.K_m and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('m')
                            else:
                                self.pseudo.append('M')

                        if evenement.key == pygame.K_n and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('n')
                            else:
                                self.pseudo.append('N')

                        if evenement.key == pygame.K_o and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('o')
                            else:
                                self.pseudo.append('O')

                        if evenement.key == pygame.K_p and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('p')
                            else:
                                self.pseudo.append('P')

                        if evenement.key == pygame.K_q and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('q')
                            else:
                                self.pseudo.append('Q')

                        if evenement.key == pygame.K_r and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('r')
                            else:
                                self.pseudo.append('R')

                        if evenement.key == pygame.K_s and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('s')
                            else:
                                self.pseudo.append('S')

                        if evenement.key == pygame.K_t and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('t')
                            else:
                                self.pseudo.append('T')

                        if evenement.key == pygame.K_u and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('u')
                            else:
                                self.pseudo.append('U')

                        if evenement.key == pygame.K_v and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('v')
                            else:
                                self.pseudo.append('V')

                        if evenement.key == pygame.K_w and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('w')
                            else:
                                self.pseudo.append('W')

                        if evenement.key == pygame.K_x and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('x')
                            else:
                                self.pseudo.append('X')

                        if evenement.key == pygame.K_y and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('y')
                            else:
                                self.pseudo.append('Y')

                        if evenement.key == pygame.K_z and len(self.pseudo) < 10:
                            if len(self.pseudo) > 0:
                                self.pseudo.append('z')
                            else:
                                self.pseudo.append('Z')

                    else:
                        if evenement.key == pygame.K_RETURN:
                            self.actif = False

            ecran.fill((0, 0, 0))

            self.afficher_message('FIN', 'grande', (240, 240, 240), ((largeur_ecran / 2 - 20), (hauteur_ecran / 2 - 100), 100, 50), ecran)
            self.afficher_message('Ton score est {}'.format(str(self.score)), 'moyenne', (240, 240, 240), ((largeur_ecran / 2 - 80), (hauteur_ecran / 2 - 50), 100, 50), ecran)

            if self.nouveau_score():
                self.afficher_message("Nouveau score, tape ton nom :", 'moyenne', (255, 255, 255), ((largeur_ecran / 2 - 150), (hauteur_ecran / 2 + 100), 100, 50), ecran)
                pygame.draw.rect(ecran, (255, 255, 255), ((largeur_ecran / 2 - 75), (hauteur_ecran / 2 + 130), 150, 22))
                self.afficher_message("{}".format(self.nouveau_pseudo()), 'moyenne', (0, 0, 0), ((largeur_ecran / 2 - 73), (hauteur_ecran / 2 + 132), 100, 50), ecran)


            pygame.display.flip()


    def nouveau_score(self):

        if self.score > self.bdd.minimum()[2]:
            return True

        return  False


    def nouveau_pseudo(self):
        pseudo = ""
        for lettre in self.pseudo:
            pseudo += lettre
        return pseudo