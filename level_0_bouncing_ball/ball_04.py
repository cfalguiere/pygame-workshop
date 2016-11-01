#
# Faire rebondir une balle
# 04 - Déplacer la balle
#

# initialise pygame
import pygame
pygame.init()

# défini la zone d'affichage
width = 320
height = 240
window_size = ( width, height )
game_surface = pygame.display.set_mode(window_size)

# défini la couleur noire pour le fond
color_black = ( 0, 0, 0 )

# charge l'image de la balle
ball_image = pygame.image.load("ball.bmp")
ball_rect = ball_image.get_rect()

# boucle infinie
running = True
while running:
    for event in pygame.event.get():
        # pour le bouton de fermeture de la fenêtre, quitte le programme
        if event.type == pygame.QUIT:
          running = False

    # recalcule la position
    ball_rect = ball_rect.move( [2, 1] )

    # reaffiche le fond et la balle
    game_surface.fill(color_black)
    game_surface.blit(ball_image, ball_rect)
    pygame.display.flip()

