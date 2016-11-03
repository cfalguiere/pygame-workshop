# Afficher les instructions
import random, time, pygame

# défini le canvas d'affichage
pygame.init()
width = 500
height = 300
window_size = ( width, height )
game_surface = pygame.display.set_mode(window_size)

# couleurs
color_black = ( 0, 0, 0 )
color_white = ( 255, 255, 255 )

# textes
labelFont = pygame.font.SysFont("Helvetica", 18)

# charge l'image de la balle
ball_rect = pygame.Rect(0, 0, 28, 28)
ball_rect.center = (width/2, height-34)
racket_rect = pygame.Rect(0, height - 20, 60, 15)
racket_rect.x = width/2 - racket_rect.w/2

colors = []
for c in range(0,10):
    colors.append(( random.randint(100,240), random.randint(60,210), random.randint(30,180) ))
bricks = []
for r in range(0,4):
  for i in range(0,10):
    bricks.append(pygame.Rect(i*50, 70 + r*20, 48, 19))


# intialise le vecteur de déplacement
ball_speed_vectors = [ [5, -5], [-5, -5] ]
ball_speed_vector = ball_speed_vectors[ random.randint(0,1) ]
racket_speed_vector = [0, 0]
X = 0
Y = 1

balls = 10
running = True
paused = False
while running:
    for event in pygame.event.get():
        # pour le bouton de fermeture de la fenêtre, quitte le programme
        if event.type == pygame.QUIT:
           running = False
        # pour l'utilisation des touches, modifie le vecteur de déplacement
        if pygame.mouse.get_pressed():
           paused = False
        if event.type == pygame.KEYDOWN:
           paused = False
           if event.key == pygame.K_LEFT:
              racket_speed_vector = [-20, 0]
           if event.key == pygame.K_RIGHT:
              racket_speed_vector = [20, 0]
        if event.type == pygame.KEYUP:
              racket_speed_vector = [0, 0]


    # reaffiche le fond et les lignes
    game_surface.fill(color_black)

    # affiche les raquettes
    racket_rect = racket_rect.move(racket_speed_vector)
    pygame.draw.rect(game_surface, color_white, racket_rect)

    for brick in bricks:
      color = colors[ round(brick.x / 50) ]
      pygame.draw.rect(game_surface, color, brick)
      c = c + 1

    # affiche la balle
    if not paused:
      ball_rect = ball_rect.move(ball_speed_vector)
      for brick in bricks:
        if ball_rect.colliderect(brick):
            ball_speed_vector[Y] = -ball_speed_vector[Y]
            bricks.remove(brick)
      if ball_rect.colliderect(racket_rect):
          ball_speed_vector[Y] = -ball_speed_vector[Y]
      if ball_rect.bottom > height:
          balls = balls - 1
          ball_rect.center = (width/2, height-34)
          ball_speed_vector = ball_speed_vectors[ random.randint(0,1) ]
          paused = True
      if ball_rect.top < 0:
          ball_speed_vector[Y] = -ball_speed_vector[Y]
      if ball_rect.left < 0 or ball_rect.right > width:
          ball_speed_vector[X] = -ball_speed_vector[X]
    pygame.draw.circle(game_surface, color_white, ball_rect.center, round(ball_rect.width/2))

    # affiche le texte
    label = labelFont.render("balls {0}".format(balls), True, color_white)
    labelPosition = ( 10, 10 )
    game_surface.blit(label, labelPosition)

    # display buffer
    pygame.display.flip()

