#
# Faire rebondir une balle
# 01 - Afficher la fenêtre
#

# initialise pygame
import time, pygame
pygame.init()

# défini la largeur et la hauteur de la fenêtre
width = 320
height = 240

# affiche le contenu de la variable sur le terminal
print( width )

# window_size contient la paire de nombres largeur x hauteur
window_size = ( width, height )

# affiche le contenu de window_size
print( window_size )

# défini la zone d'affichage
game_surface = pygame.display.set_mode(window_size)

# attend 5 seconde et ferme le programme
time.sleep(5)

