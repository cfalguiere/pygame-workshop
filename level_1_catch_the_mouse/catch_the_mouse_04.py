#
# Détecter la position de la souris et déplacer la balle avec la souris
# Si on clique sur la souris, elle fuit ailleurs
#

# initialise pygame
import random, pygame
pygame.init()

# défini la zone d'affichage et les couleurs
window_size = width, height = 320, 240
X = 0
Y = 1
color_white = ( 255, 255, 255 )
game_surface = pygame.display.set_mode(window_size)

# charge l'image de la souris
mouse_image = pygame.image.load("mouse_mini.png")
mouse_rect = mouse_image.get_rect()

# boucle infinie
running = True
grab = False
mouse_image_pos = [ width/2, height/2 ]
while running:
    for event in pygame.event.get():
        print (event)
        mouse_pos = pygame.mouse.get_pos()
        # pour le bouton de fermeture de la fenêtre, quitte le programme
        if event.type == pygame.QUIT: running = False
        # pour la souris
        if event.type == pygame.MOUSEMOTION:
           if grab:
              mouse_image_pos = mouse_pos
        if event.type == pygame.MOUSEBUTTONDOWN:
           if mouse_rect.collidepoint(mouse_pos):
              x = ( mouse_pos[X] + random.randint(80,250) ) % width
              y = ( mouse_pos[Y] + random.randint(60,200) ) % height
              mouse_image_pos = [ x, y ]
              grab = False
           else :
              grab = True
        if event.type == pygame.MOUSEBUTTONUP:
           if grab:
              mouse_image_pos = mouse_pos
           grab = False

    # repositionne l'image
    mouse_rect.center = mouse_image_pos

    # reaffiche le fond et la balle
    game_surface.fill(color_white)
    game_surface.blit(mouse_image, mouse_rect)
    pygame.display.flip()

