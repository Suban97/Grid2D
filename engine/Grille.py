# Création class Grille
import pygame

class GrilleManager:
    
    def __init__(self, colonne, ligne, taille_case):
        # Nombre de colonnes et de lignes de la grille
        self.colonne = colonne
        self.ligne = ligne

        # Taille d'une case en pixels
        self.taille_case = taille_case

        # Dimensions totales de la grille
        self.largeur = colonne * taille_case
        self.hauteur = ligne * taille_case

        # Coordonnées du centre d'une case
        self.centre = taille_case / 2

        # Dictionnaire contenant toutes les positions de la grille
        # Exemple :
        # {
        #   (0,0): None,
        #   (1,0): None
        # }
        self.cases = {
            (x, y): None
            for x in range(self.colonne)
            for y in range(self.ligne)
        }
    
    def draw(self, screen, highlighted_cases=None):

        # Parcourt toutes les cases de la grille
        for case in self.cases:

            # Vérifie si le joueur peut atteindre cette case
            if case in highlighted_cases:



                # Dessine les cases accessibles en vert
                pygame.draw.rect(
                    screen,
                    (0, 255, 0),
                    (
                        case[0] * self.taille_case,
                        case[1] * self.taille_case,
                        self.taille_case,
                        self.taille_case
                    )
                )

            else:

                # Dessine les cases non accessibles en blanc
                pygame.draw.rect(
                    screen,
                    (250, 250, 250),
                    (
                        case[0] * self.taille_case,
                        case[1] * self.taille_case,
                        self.taille_case,
                        self.taille_case
                    )
                )

            # Dessine le contour noir des cases
            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (
                    case[0] * self.taille_case,
                    case[1] * self.taille_case,
                    self.taille_case,
                    self.taille_case
                ),
                1
            )
            
    def manhattan(self, a, b):

        # Calcule la distance Manhattan entre deux positions
        # Exemple :
        # de (0,0) à (2,1) = 3
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def can_move(self, start_pos, target_pos, max_range):

        # Retourne True si la case cible est dans le rayon
        # de déplacement du joueur
        return self.manhattan(start_pos, target_pos) <= max_range
