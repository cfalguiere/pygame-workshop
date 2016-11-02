#
# attribution des images : clipart.co
#

# initialisation
import random, pygame
pygame.init()

# défini le canvas d'affichage
width = 640
height = 480
window_size = ( width, height )
game_surface = pygame.display.set_mode(window_size)

# couleurs
color_black = ( 0, 0, 0 )
color_red = ( 255, 0, 0 )

# charge les images
rocket_image = pygame.image.load("images/rocket_mini.png")
rocket_rect = rocket_image.get_rect()

planet_image = pygame.image.load("images/planet.png")
planet_rect = planet_image.get_rect()

spaceship_images = [None, None, None, None]
spaceship_rects = [None, None, None, None]
spaceship_images[0] = pygame.image.load("images/spaceship1_mini.png")
spaceship_images[1] = pygame.image.load("images/spaceship2_mini.png")
spaceship_rects[0] = spaceship_images[0].get_rect()
spaceship_rects[1] = spaceship_images[1].get_rect()

# inialise les positions
# rocket au milieu vers le bas
rocket_rect.center = [ width/2, height - rocket_rect.height ]
# spaceship1 random
border = spaceship_rects[0].width
x = random.randint(border, width - border)
y = 50
spaceship_rects[0].center = [ x, y ]
border = spaceship_rects[1].width
x = random.randint(border, width - border)
y = 100
spaceship_rects[1].center = [ x, y ]

# intialise le vecteur de déplacement à immobile
speed_vector = [0, 0]
X = 0
Y = 1

running = True
while running:
    for event in pygame.event.get():
        # pour le bouton de fermeture de la fenêtre, quitte le programme
        if event.type == pygame.QUIT:
           running = False
        # pour l'utilisation des touches, modifie le vecteur de déplacement
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_RIGHT:
              speed_vector = [20, 0]
           if event.key == pygame.K_LEFT:
              speed_vector = [-20, 0]
        if event.type == pygame.KEYUP:
              speed_vector = [0, 0]

    # positionne la fusee
    speed_vector[Y] = random.randint(-1,0)
    if random.randint(0,10) < 2:
        speed_vector[Y] = random.randint(0,3)
    rocket_rect = rocket_rect.move(speed_vector)


    # positionne les obstacles
    x = (spaceship_rects[0].center[X] + random.randint(5,10)) % width
    y = (spaceship_rects[0].center[Y]+1) % height
    spaceship_rects[0].center = [x , y]
    x = (spaceship_rects[1].center[X] + random.randint(-10,-5)) % width
    y = (spaceship_rects[1].center[Y]+1) % height
    spaceship_rects[1].center = [x , y]

    # collisions
    if rocket_rect.colliderect(spaceship_rects[0]):
      game_surface.fill(color_red)
    else:
      if rocket_rect.colliderect(spaceship_rects[1]):
        game_surface.fill(color_red)
      else:
        # repeint le fond
        game_surface.fill(color_black)

    # repeint les obstacles
    game_surface.blit(planet_image, planet_rect)
    game_surface.blit(spaceship_images[0], spaceship_rects[0])
    game_surface.blit(spaceship_images[1], spaceship_rects[1])

    # déplace la fusée
    game_surface.blit(rocket_image, rocket_rect)


    # affiche
    pygame.display.flip()

