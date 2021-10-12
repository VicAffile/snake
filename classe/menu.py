import sys

import pygame

from classe.ecran import Ecran


class Menu(Ecran):

    def __init__(self, actif):

        Ecran.__init__(self, actif)


    def boucle(self, ecran, titre, largeur_ecran, hauteur_ecran):

        while self.actif:

            for evenement in pygame.event.get():

                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:
                        self.actif = False

            ecran.fill((0, 0, 0))

            self.afficher_messages(ecran, titre, largeur_ecran, hauteur_ecran)

            pygame.display.flip()


    def afficher_messages(self, ecran, titre, largeur_ecran, hauteur_ecran):
            self.afficher_message(titre.upper(), 'grande', (255, 255, 255), ((largeur_ecran / 2 - 50), (hauteur_ecran / 2 - 250), 100, 50), ecran)
            self.afficher_message("Le but du jeu est de manger le plus de pommes possible", 'petite', (240, 240, 240), ((largeur_ecran / 2 - 180), (hauteur_ecran / 2 - 100), 200, 5), ecran)
            self.afficher_message( "Le serpent grossira à chaque pomme manger, s'il touche le bord ou se mord la queue c'est perdu", 'petite', (240, 240, 240), ((largeur_ecran / 2 - 300), (hauteur_ecran / 2 - 80), 200, 50), ecran)
            self.afficher_message("Appuyer sur Entrée pour jouer", 'moyenne', (255, 255, 255), ((largeur_ecran / 2 - 150), (hauteur_ecran / 2 + 150), 200, 5), ecran)