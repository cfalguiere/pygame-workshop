#
# Détecter la position de la souris et déplacer la balle avec la souris
#
# initialise pygame
import pygame
pygame.init()

# défini le canvas d'affichage et les couleurs
window_size = width, height = 320, 240
X = 0
Y = 1
color_black = ( 0, 0, 0 )
screen = pygame.display.set_mode(window_size)

# charge l'image de la balle
ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

# boucle infinie
running = True
while running:
    for event in pygame.event.get():
        # pour le bouton de fermeture de la fenêtre, quitte le programme
        if event.type == pygame.QUIT: running = False
        # pour la souris
        if event.type == pygame.MOUSEMOTION:
          ballrect.center = pygame.mouse.get_pos()

    # reaffiche le fond et la balle
    screen.fill(color_black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

