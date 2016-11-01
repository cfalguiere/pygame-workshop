#
# Afficher les instructions
#

# initialise pygame
import sys, pygame

# défini le canvas d'affichage et les couleurs
pygame.init()
width = 320
height = 240
window_size = ( width, height )
color_black = ( 0, 0, 0 )
color_red   = ( 255, 0, 0)
screen = pygame.display.set_mode(window_size)

# charge l'image de la balle
ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

# choisi la police d'affichage
# il faut le faire en dehors de la boucle car c'est une opération un peu couteuse
pygame.font.init()
labelFont = pygame.font.SysFont("Helvetica", 18)

# initialise le vecteur de déplacement à immobile
speed_vector = [0, 0]

# boucle infinie
while True:
    # pour chaque événement reçu
    for event in pygame.event.get():
        # pour le bouton de fermeture de la fenêtre, quitte le programme
        if event.type == pygame.QUIT:
           sys.exit()
        # pour l'utilisation des touches, modifie le vecteur de déplacement
        if event.type == pygame.KEYDOWN:
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


    # reaffiche le fond 
    screen.fill(color_black)

    # affiche le texte
    label = labelFont.render("Déplacez la balle avec les flèches", True, color_red)
    labelPosition = ( (width - label.get_rect().width)/2,
                      (height - label.get_rect().height)/2 )
    screen.blit(label, labelPosition)

    # affiche la balle
    ballrect = ballrect.move(speed_vector)
    screen.blit(ball, ballrect)

    # Affiche l'image sur la fenêtre
    pygame.display.flip()

