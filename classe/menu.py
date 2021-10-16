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
            self.afficher_message(titre.upper(), 'grande', (255, 255, 255), ((largeur_ecran / 2 - 55), (hauteur_ecran / 2 - 250), 100, 50), ecran)
            self.afficher_message("Le but du jeu est de manger le plus de pommes possible", 'petite', (240, 240, 240), ((largeur_ecran / 2 - 180), (hauteur_ecran / 2 - 130), 200, 5), ecran)
            self.afficher_message("Le serpent grossira à chaque pomme manger, s'il touche le bord ou se mord la queue c'est perdu", 'petite', (240, 240, 240), ((largeur_ecran / 2 - 300), (hauteur_ecran / 2 - 110), 200, 50), ecran)
            self.afficher_message("Meilleurs Scores", 'grande', (255, 255, 255), ((largeur_ecran / 2 - 115), (hauteur_ecran / 2 - 40), 100, 50), ecran)
            premier = self.bdd.classement(1)
            self.afficher_message("1. {} - {}".format(premier[1], str(premier[2])), 'moyenne', (255, 255, 255), ((largeur_ecran / 2 - 70), (hauteur_ecran / 2), 100, 50), ecran)
            deuxieme = self.bdd.classement(2)
            self.afficher_message("2. {} - {}".format(deuxieme[1], str(deuxieme[2])), 'moyenne', (255, 255, 255), ((largeur_ecran / 2 - 70), (hauteur_ecran / 2 + 20), 100, 50), ecran)
            troisieme = self.bdd.classement(3)
            self.afficher_message("3. {} - {}".format(troisieme[1], str(troisieme[2])), 'moyenne', (255, 255, 255), ((largeur_ecran / 2 - 70), (hauteur_ecran / 2 + 40), 100, 50), ecran)
            quatrieme = self.bdd.classement(4)
            self.afficher_message("4. {} - {}".format(quatrieme[1], str(quatrieme[2])), 'moyenne', (255, 255, 255), ((largeur_ecran / 2 - 70), (hauteur_ecran / 2 + 60), 100, 50), ecran)
            cinquieme = self.bdd.classement(5)
            self.afficher_message("5. {} - {}".format(cinquieme[1], str(cinquieme[2])), 'moyenne', (255, 255, 255), ((largeur_ecran / 2 - 70), (hauteur_ecran / 2 + 80), 100, 50), ecran)
            self.afficher_message("Appuyer sur Entrée pour jouer", 'moyenne', (255, 255, 255), ((largeur_ecran / 2 - 150), (hauteur_ecran / 2 + 150), 200, 5), ecran)