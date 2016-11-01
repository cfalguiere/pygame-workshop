#
# Déplacer une balle avec la souris et quitter la fenêtre
#

# initialise pygame
import sys, pygame

# défini les dimensions du canvas d'affichage et les couleurs
pygame.init()
width = 320
height = 240
window_size = ( width, height )
color_black = 0, 0, 0
screen = pygame.display.set_mode(window_size)

# charge l'image de la balle
ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

# intialise le vecteur de déplacement à immobile
speed_vector = [0, 0]

# boucle infinie
while True:
    # pour chaque événement reçu
    for event in pygame.event.get():
        print(event)
        # pour le bouton de fermeture de la fenêtre, quitte le programme
        if event.type == pygame.QUIT:
           sys.exit()
        # pour l'utilisation des touches, modifie le vecteur de déplacement
        if event.type == pygame.KEYDOWN:
           print(event.key)
           if event.key == pygame.K_RIGHT:
              speed_vector = [20, 0]
           if event.key == pygame.K_LEFT:
              speed_vector = [-20, 0]
           if event.key == pygame.K_UP:
              speed_vector = [0, -20]
           if event.key == pygame.K_DOWN:
              speed_vector = [0, 20]
        if event.type == pygame.KEYUP:
              speed_vector = [0, 0]

    # réaffiche le fond et la balle en tenant compte du déplacement
    screen.fill(color_black)
    ballrect = ballrect.move(speed_vector)
    screen.blit(ball, ballrect)

    # Affiche l'image sur la fenêtre
    pygame.display.flip()

