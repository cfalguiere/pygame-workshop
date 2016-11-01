#
# Afficher une image
#

# initialise pygame
import sys, time, pygame
pygame.init()

# défini les dimensions de la fenêtre
width = 320
height = 240
window_size = ( width, height )

# affichage le fond d'écran
color_black = (  0,   0,   0)
screen = pygame.display.set_mode(window_size)
screen.fill(color_black)

# load crée une image en lisant le fichier image (ici ball.bmp)
# ball.get_rect() permet d'obtenir les dimensions de l'image chargée
# screen.blit est une fonction de Surface qui copie l'image dans le rectangle défini par ballrect
ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()
screen.blit(ball, ballrect)

# Déplace la balle au centre
centerX = (width - ballrect.width)/2
centerY = (height - ballrect.height)/2
ballrect = ballrect.move([centerX, centerY])
screen.blit(ball, ballrect)

# Déplace la balle de 100 pixels horizontalement et 80 pixels verticalement
ballrect = ballrect.move([100,80])
screen.blit(ball, ballrect)

# Affiche l'image sur la fenêtre
pygame.display.flip()

# Si tu lances le programme tu va le voir s'afficher 5 secondes et s'arrêter
# La balle ne disparaît pas quand elle se déplace pour le moment. On corrigera plus tard.
time.sleep(5)
quit()


