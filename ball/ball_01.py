#
# Afficher la fenêtre
#

# initialise pygame
import sys, time, pygame
pygame.init()

# définir la largeur et la hauteur de la fenêtre
width = 320
height = 240

# print est une fonction qui affiche le contenu de la variable sur le terminal
print( width )

# window_size contient la paire de nombres largeur x hauteur
window_size = ( width, height )

# print affiche le contenu de window_size
print( window_size )

# screen représente l'écran
screen = pygame.display.set_mode(window_size)

# Si tu lances le programme tu va le voir s'afficher 5 secondes et s'arrêter
time.sleep(5)
quit()
