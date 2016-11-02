# Afficher les instructions
import random, time, pygame

# défini le canvas d'affichage
pygame.init()
width = 600
height = 400
window_size = ( width, height )
game_surface = pygame.display.set_mode(window_size)

# couleurs
color_black = ( 0, 0, 0 )
color_white = ( 255, 255, 255 )

# textes
labelFont = pygame.font.SysFont("Helvetica", 32)

# charge l'image de la balle
ball_rect = pygame.Rect(0, 0, 28, 28)
ball_rect.center = (width/2, height/2)
ping_rect = pygame.Rect(10, 0, 15, 60)
ping_rect.y = height/2 - ping_rect.h/2
pong_rect = pygame.Rect(width - 10 - ping_rect.w, 0, ping_rect.w, ping_rect.h)
pong_rect.y = ping_rect.y

# intialise le vecteur de déplacement
ball_speed_vectors = [ [5, 5], [-5, 5], [5, -5], [-5, -5] ]
ball_speed_vector = ball_speed_vectors[ random.randint(0,3) ]
ping_speed_vector = [0, 0]
pong_speed_vector = [0, 0]
X = 0
Y = 1

ping_score = 0
pong_score = 0
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
           if event.key == pygame.K_Q:
              ping_speed_vector = [0, -20]
           if event.key == pygame.K_W:
              ping_speed_vector = [0, 20]
           if event.key == pygame.K_J:
              pong_speed_vector = [0, -20]
           if event.key == pygame.K_N:
              pong_speed_vector = [0, 20]
        if event.type == pygame.KEYUP:
              ping_speed_vector = [0, 0]
              pong_speed_vector = [0, 0]


    # reaffiche le fond et les lignes
    game_surface.fill(color_black)
    pygame.draw.lines(game_surface, color_white, False, [[0, 10], [width, 10]], 10)
    pygame.draw.lines(game_surface, color_white, False, [[0, height - 10], [width, height - 10]], 10)
    pygame.draw.lines(game_surface, color_white, False, [[width/2, 20], [width/2, height - 20]], 1)

    # affiche les raquettes
    ping_rect = ping_rect.move(ping_speed_vector)
    pong_rect = pong_rect.move(pong_speed_vector)
    pygame.draw.rect(game_surface, color_white, ping_rect)
    pygame.draw.rect(game_surface, color_white, pong_rect)

    # affiche la balle
    if not paused:
      ball_rect = ball_rect.move(ball_speed_vector)
      if ball_rect.colliderect(ping_rect) or ball_rect.colliderect(pong_rect):
          ball_speed_vector[X] = -ball_speed_vector[X]
      if ball_rect.left < 0:
          pong_score = pong_score + 1
          ball_rect.center = ( width/2, height/2 )
          ball_speed_vector = ball_speed_vectors[ random.randint(0,3) ]
          paused = True
      if ball_rect.right > width:
          ping_score = ping_score + 1
          ball_rect.center = ( width/2, height/2 )
          ball_speed_vector = ball_speed_vectors[ random.randint(0,3) ]
          paused = True
      if ball_rect.top < 0 or ball_rect.bottom > height:
          ball_speed_vector[Y] = -ball_speed_vector[Y]
    pygame.draw.circle(game_surface, color_white, ball_rect.center, round(ball_rect.width/2))

    # affiche le texte
    label1 = labelFont.render(str(ping_score), True, color_white)
    labelPosition = ( width/2 - 20 - label1.get_rect().width , 20 )
    game_surface.blit(label1, labelPosition)
    label2 = labelFont.render(str(pong_score), True, color_white)
    labelPosition = ( width/2 + 20, 20 )
    game_surface.blit(label2, labelPosition)

    # display buffer
    pygame.display.flip()

