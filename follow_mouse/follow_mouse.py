#
# Faire rebondir une balle
#
# initialise pygame
import sys, pygame
pygame.init()

# défini le canvas d'affichage et les couleurs
window_size = width, height = 320, 240
i_hor = 0
i_ver = 1
color_black = ( 0, 0, 0 )
screen = pygame.display.set_mode(window_size)

# charge l'image de la balle
ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

mem_mouse_pos = [ -1, -1]

# boucle infinie
while True:
    for event in pygame.event.get():
        # pour le bouton de fermeture de la fenêtre, quitte le programme
        if event.type == pygame.QUIT: sys.exit()
        # pour la souris
        if event.type == pygame.MOUSEMOTION:
          mouse_pos = pygame.mouse.get_pos()
          ballrect.center = mouse_pos

    # reaffiche le fond et la balle
    screen.fill(color_black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

