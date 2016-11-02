#
# Détecter la position de la souris et déplacer la balle avec la souris
#

# initialise pygame
import random, pygame
pygame.init()

# défini la zone d'affichage et les couleurs
window_size = width, height = 320, 240
X = 0
Y = 1
game_surface = pygame.display.set_mode(window_size)
color_white = ( 255, 255, 255 )

# charge l'image de la souris
mouse_image = pygame.image.load("mouse_mini.png")
mouse_rect = mouse_image.get_rect()

# boucle infinie
running = True
grab = False
mouse_image_pos = [ width/2, height/2 ]
while running:
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        # pour le bouton de fermeture de la fenêtre, quitte le programme
        if event.type == pygame.QUIT: running = False
        # pour la souris
        if event.type == pygame.MOUSEMOTION:
           mouse_image_pos = pygame.mouse.get_pos()

    # repositionne l'image
    mouse_rect.center = mouse_image_pos

    # reaffiche le fond et la balle
    game_surface.fill(color_white)
    game_surface.blit(mouse_image, mouse_rect)
    pygame.display.flip()

