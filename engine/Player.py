import pygame

class PlayerManager:

    def __init__(self, couleur, rayon, pos):

        # Position actuelle du joueur dans la grille
        self.pos = pos

        # Distance maximale de déplacement
        self.rayon = rayon

        # Couleur du joueur au format RGB
        self.couleur = couleur

        # Liste des cases accessibles depuis la position actuelle
        self.case_move = []
    
    
    def update_moves(self, grille):
        self.case_move = [case for case in grille.cases if grille.can_move(self.pos, case, self.rayon)]        
        
    def draw(self, screen, grille): # Déssine le joueur
        # Convertis les cases en pixel et dessine le joueur
        pygame.draw.rect(screen, self.couleur,(self.pos[0] *  grille.taille_case, self.pos[1] * grille.taille_case , grille.taille_case, grille.taille_case), 0, 20)
        
        
    def apply_move(self, case_cliquee, grille):

        # Déplace le joueur uniquement si la case est atteignable
        if grille.can_move(self.pos, case_cliquee, self.rayon):

            # Mise à jour de la position
            self.pos = case_cliquee

            # Vide les anciennes cases accessibles
            # pour les recalculer au prochain frame
            self.case_move.clear()
