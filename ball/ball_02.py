#
# Afficher la fenêtre d'une certaine couleur et gérer la fermeture
#

# initialise pygame
import sys, time, pygame
pygame.init()

# défini les dimensions de la fenêtre
width = 320
height = 240
window_size = ( width, height )

# défini des couleurs en RGB
color_black = (  0,   0,   0)
color_red   = (255,   0,   0)
color_white = (255, 255, 255)

# obtient la surface de dessin
screen = pygame.display.set_mode(window_size)

# La fonction fill permet de remplir toute la surface
screen.fill(color_black)

# Dessine et peint un rectangle
pygame.draw.rect(screen, color_white, rect)

# met à jour l'écran
# cette ligne doit suivre TOUTES les instructions d'affichage
pygame.display.flip()

# Si tu lances le programme tu va le voir s'afficher 5 secondes et s'arrêter
time.sleep(5)
quit()

