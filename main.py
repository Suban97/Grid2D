import pygame, sys
import random

#  =====================================================
#  Importation des classes PlayerManager et GrilleManager
#  =====================================================

from engine.Grille import GrilleManager
from engine.Player import PlayerManager


# =========================
# CONFIGURATION DE LA GRILLE
# =========================

lignes = 10
colonnes = 10
taille_cases = 50
rayon = 3

# Dimensions de la fenêtre calculées selon la taille de la grille
largeur = colonnes * taille_cases
hauteur = lignes * taille_cases

# Création de la fenêtre pygame
screen = pygame.display.set_mode((largeur, hauteur))

        


def main():
    # Création de l'instance grille
    grille = GrilleManager(colonnes, lignes, taille_cases)

    # Création de l'instance player
    player = PlayerManager((255,0,0), rayon, random.choice(list(grille.cases)))

    while True:
        screen.fill((255,255,255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = event.pos #récupère les coordonnées de la souris

                case_cliquee = ( # Recherche l'emplacement de la souris selon les cases
                    mouse[0] // grille.taille_case,
                    mouse[1] // grille.taille_case
                )
                
                player.apply_move(case_cliquee, grille)
                
        player.update_moves(grille)
        
        grille.draw(screen, player.case_move)
        player.draw(screen, grille)
        
        
        pygame.display.update()




if __name__ == "__main__":
    main()
