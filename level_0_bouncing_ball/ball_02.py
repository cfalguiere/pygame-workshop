#
# Faire rebondir une balle
# 02 - Gérer la sortie du programme
#

# initialise pygame
import pygame
pygame.init()

# défini la zone d'affichage
width = 320
height = 240
window_size = ( width, height )
game_surface = pygame.display.set_mode(window_size)

# boucle infinie
running = True
while running:
    for event in pygame.event.get():
        # pour le bouton de fermeture de la fenêtre, quitte le programme
        if event.type == pygame.QUIT:
          running = False


