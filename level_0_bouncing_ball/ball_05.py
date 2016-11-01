#
# Faire rebondir une balle
# 05 - Gérer le rebond
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

# initialise le vecteur de déplacement
ball_speed = [5, 5]
X = 0
Y = 1

# boucle infinie
running = True
while running:
    for event in pygame.event.get():
        # pour le bouton de fermeture de la fenêtre, quitte le programme
        if event.type == pygame.QUIT:
          running = False

    # recalcule la position
    ball_rect = ball_rect.move(ball_speed)

    # rebond sur les bords gauche et droit
    if ball_rect.left < 0 or ball_rect.right > width:
        ball_speed[X] = -ball_speed[X]

    # rebond sur les bords haut et bas
    if ball_rect.top < 0 or ball_rect.bottom > height:
        ball_speed[Y] = -ball_speed[Y]

    # reaffiche le fond et la balle
    game_surface.fill(color_black)
    game_surface.blit(ball_image, ball_rect)
    pygame.display.flip()

