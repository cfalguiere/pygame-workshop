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

# initialise le vecteur de déplacement
speed = [5, 5]

# boucle infinie
while True:
    for event in pygame.event.get():
        # pour le bouton de fermeture de la fenêtre, quitte le programme
        if event.type == pygame.QUIT: sys.exit()

    # recalcule la position
    ballrect = ballrect.move(speed)

    # rebond sur les bords gauche et droit
    if ballrect.left < 0 or ballrect.right > width:
        speed[i_hor] = -speed[i_hor]

    # rebond sur les bords haut et bas
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[i_ver] = -speed[i_ver]

    # reaffiche le fond et la balle
    screen.fill(color_black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

